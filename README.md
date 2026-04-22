# YouTube Video Downloader

A full-stack web application that allows users to download YouTube videos directly to their local device with a modern, user-friendly interface.

## Features

✅ **Easy Download**: Paste YouTube URLs and download videos with a single click
✅ **Video Management**: View all downloaded videos with metadata (title, size, download date)
✅ **Direct Downloads**: Download videos stored on the server to your device
✅ **Delete Videos**: Remove downloaded videos to free up space
✅ **Modern UI**: Dark theme with YouTube-inspired design
✅ **Responsive Design**: Works seamlessly on desktop and mobile devices
✅ **Error Handling**: Comprehensive error messages and validation
✅ **Real-time Updates**: Automatic video list refresh

## Quick Start

### Windows Users
1. Double-click `setup.bat` to install dependencies
2. Double-click `run.bat` to start the server
3. Open http://127.0.0.1:5000 in your browser

### Manual Setup
```bash
cd backend
python -m pip install -r requirements.txt
python app.py
```

## Project Structure

```
YOUTUBE_VIDEO_DOWNLOADER/
├── backend/
│   ├── app.py                 # Flask backend application
│   ├── requirements.txt        # Python dependencies
│   ├── .env                   # Configuration file
│   ├── templates/
│   │   └── index.html         # Main HTML template
│   └── static/
│       ├── css/
│       │   └── style.css      # Styling
│       └── js/
│           └── script.js      # Frontend logic
├── downloads/                  # Downloaded videos storage
├── setup.bat                   # Windows setup script
├── run.bat                     # Windows run script
├── README.md                   # This file
├── QUICKSTART.md              # Quick start guide
└── ARCHITECTURE.md            # Technical architecture
```

## Requirements

- Python 3.8+
- Modern web browser
- Internet connection
- 20GB+ disk space for downloads

## Installation

1. Install Python from https://www.python.org (if not installed)
2. Navigate to the project folder
3. For Windows: Run `setup.bat`
4. For others: Run `python -m pip install -r backend/requirements.txt`

## Usage

### Start the Server
```bash
cd backend
python app.py
```

### Download a Video
1. Paste a YouTube URL in the input field
2. Click "Download"
3. Wait for completion
4. Video appears in the "Downloaded Videos" section

### Manage Downloads
- **Download to Device**: Click ⬇ Download on any video
- **Delete Video**: Click 🗑 Delete on any video

## API Endpoints

### POST /api/download
Download a YouTube video
```json
{"url": "https://www.youtube.com/watch?v=..."}
```

### GET /api/videos
Get list of downloaded videos

### DELETE /api/delete/<filename>
Delete a downloaded video

### GET /api/download-file/<filename>
Download video file to device

## Troubleshooting

### Port Already in Use
- Change the port in `backend/app.py` line 214

### Download Fails
- Verify the YouTube URL is correct
- Check internet connection
- The video might be restricted

### No Videos Appearing
- Ensure backend is running
- Check if downloads folder exists
- Refresh the page

## Configuration

Edit `backend/.env` to modify:
- Server host and port
- Download folder location
- Video format settings

## Technology Stack

- **Backend**: Python, Flask, yt-dlp
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Storage**: JSON file database
- **API**: RESTful architecture

## Performance Tips

1. Use wired connection for faster downloads
2. Close other applications
3. Ensure sufficient disk space
4. Download during off-peak hours

## Security Notes

⚠️ This application is for personal use only
- Respect copyright laws
- Only download content you have rights to
- Use responsibly

## Future Enhancements

- [ ] Batch download functionality
- [ ] Download quality selection
- [ ] Subtitle download support
- [ ] Audio-only extraction
- [ ] Database storage instead of JSON

## License

MIT License - Personal use only

## Support

For issues:
1. Check the QUICKSTART.md file
2. Review ARCHITECTURE.md for technical details
3. Check browser console (F12) for errors

## Disclaimer

This tool is for personal, non-commercial use only. Ensure you have rights to download any content. Developers are not responsible for misuse.

---

**Version**: 1.0.0
**Created**: April 2024
