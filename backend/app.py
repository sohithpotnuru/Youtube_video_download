from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
import json
import base64
import tempfile
import yt_dlp
from pathlib import Path
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
BASE_DIR = Path(__file__).parent
# Use a 'downloads' folder relative to the backend — works on any server
DOWNLOADS_DIR = BASE_DIR / "downloads"
VIDEOS_DB = BASE_DIR / "videos_list.json"

# Ensure downloads directory exists
DOWNLOADS_DIR.mkdir(exist_ok=True)

# Initialize videos database
if not VIDEOS_DB.exists():
    with open(VIDEOS_DB, 'w') as f:
        json.dump([], f)


def get_videos_list():
    """Get list of downloaded videos"""
    try:
        if VIDEOS_DB.exists():
            with open(VIDEOS_DB, 'r') as f:
                return json.load(f)
    except Exception as e:
        logger.error(f"Error reading videos list: {e}")
    return []


def save_video_info(video_info):
    """Save video info to database"""
    try:
        videos = get_videos_list()
        videos.append(video_info)
        with open(VIDEOS_DB, 'w') as f:
            json.dump(videos, f, indent=2)
    except Exception as e:
        logger.error(f"Error saving video info: {e}")


def delete_video(filename):
    """Delete video file and update database"""
    try:
        video_path = DOWNLOADS_DIR / filename
        if video_path.exists():
            video_path.unlink()
        
        videos = get_videos_list()
        videos = [v for v in videos if v['filename'] != filename]
        with open(VIDEOS_DB, 'w') as f:
            json.dump(videos, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error deleting video: {e}")
        return False


@app.route('/')
def index():
    """Serve the main HTML file"""
    return render_template('index.html')


@app.route('/api/download', methods=['POST'])
def download_video():
    """Download video from YouTube URL"""
    try:
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Validate URL
        if 'youtube.com' not in url and 'youtu.be' not in url:
            return jsonify({'error': 'Please enter a valid YouTube URL'}), 400
        
        # --- Cookie resolution (priority: env var > local files) ---
        cookie_path = None
        _temp_cookie_file = None  # track temp file for cleanup

        # 1. Railway / production: YOUTUBE_COOKIES_BASE64 env var
        cookies_b64 = os.environ.get('YOUTUBE_COOKIES_BASE64', '').strip()
        if cookies_b64:
            try:
                cookie_data = base64.b64decode(cookies_b64).decode('utf-8')
                _temp_cookie_file = tempfile.NamedTemporaryFile(
                    mode='w', suffix='.txt', delete=False
                )
                _temp_cookie_file.write(cookie_data)
                _temp_cookie_file.flush()
                cookie_path = Path(_temp_cookie_file.name)
                logger.info("Using cookies from YOUTUBE_COOKIES_BASE64 env var")
            except Exception as e:
                logger.warning(f"Failed to decode YOUTUBE_COOKIES_BASE64: {e}")

        # 2. Local development: cookies.txt file on disk
        if not cookie_path:
            project_root = Path(__file__).parent.parent
            downloads_folder = Path.home() / 'Downloads'
            for candidate in [downloads_folder / 'cookies.txt', project_root / 'cookies.txt']:
                if candidate.exists():
                    cookie_path = candidate
                    logger.info(f"Using cookies from: {cookie_path}")
                    break

        # Configure yt-dlp options
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': str(DOWNLOADS_DIR / '%(title)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
            'socket_timeout': 30,
            'noplaylist': True,
            'http_chunk_size': 10485760,  # 10MB chunks
            # Use Android/iOS player to bypass datacenter IP bot-detection
            'extractor_args': {
                'youtube': {
                    'player_client': ['android', 'ios', 'web'],
                }
            },
        }

        if cookie_path:
            ydl_opts['cookiefile'] = str(cookie_path)
            logger.info(f"Cookie file set: {cookie_path}")
        
        video_title = None
        filename = None
        
        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=True)
            finally:
                # Clean up temp cookie file if created
                if _temp_cookie_file:
                    try:
                        _temp_cookie_file.close()
                        Path(_temp_cookie_file.name).unlink(missing_ok=True)
                    except Exception:
                        pass
            video_title = info.get('title', 'Unknown')
            # Extract final filename correctly
            filename = ydl.prepare_filename(info)
            # Sometimes yt-dlp changes extension during post-processing
            if 'requested_downloads' in info and info['requested_downloads']:
                filename = info['requested_downloads'][0]['filepath']
            filename = os.path.basename(filename)
        
        # Get file size
        video_path = DOWNLOADS_DIR / filename
        
        if not video_path.exists():
            # Try to find the file if extension changed
            base_name = os.path.splitext(filename)[0]
            for ext in ['.mp4', '.webm', '.mkv']:
                if (DOWNLOADS_DIR / (base_name + ext)).exists():
                    filename = base_name + ext
                    video_path = DOWNLOADS_DIR / filename
                    break

        if not video_path.exists():
            raise Exception("File was downloaded but could not be located on disk.")

        file_size = video_path.stat().st_size
        file_size_mb = round(file_size / (1024 * 1024), 2)
        
        # Save video info
        video_info = {
            'title': video_title,
            'filename': filename,
            'size_mb': file_size_mb,
            'download_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'url': url
        }
        save_video_info(video_info)
        
        logger.info(f"Video downloaded successfully: {filename}")
        
        return jsonify({
            'success': True,
            'title': video_title,
            'filename': filename,
            'size_mb': file_size_mb
        }), 200
    
    except yt_dlp.utils.DownloadError as e:
        logger.error(f"Download error: {e}")
        # Send the exact yt-dlp error to the frontend so the user can see what's wrong
        return jsonify({'error': str(e)}), 400
    
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Unexpected error during download: {e}")
        return jsonify({'error': f'Download failed: {error_msg}'}), 500


@app.route('/api/videos', methods=['GET'])
def get_videos():
    """Get list of downloaded videos"""
    try:
        videos = get_videos_list()
        return jsonify(videos), 200
    except Exception as e:
        logger.error(f"Error getting videos: {e}")
        return jsonify({'error': 'Failed to retrieve videos'}), 500


@app.route('/api/delete/<filename>', methods=['DELETE'])
def delete_video_endpoint(filename):
    """Delete a downloaded video"""
    try:
        if delete_video(filename):
            return jsonify({'success': True, 'message': 'Video deleted'}), 200
        else:
            return jsonify({'error': 'Failed to delete video'}), 500
    except Exception as e:
        logger.error(f"Error in delete endpoint: {e}")
        return jsonify({'error': 'Failed to delete video'}), 500


@app.route('/api/download-file/<filename>', methods=['GET'])
def download_file(filename):
    """Download a video file"""
    try:
        video_path = DOWNLOADS_DIR / filename
        
        if not video_path.exists():
            return jsonify({'error': 'File not found'}), 404
        
        return send_file(
            video_path,
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        logger.error(f"Error downloading file: {e}")
        return jsonify({'error': 'Failed to download file'}), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    logger.info(f"Starting YouTube Video Downloader")
    logger.info(f"Downloads directory: {DOWNLOADS_DIR}")
    # Use PORT env var (set by Railway/Render) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=port)
