# Quick Start Guide

## Installation & Running (Windows Users)

### Option 1: Automatic Setup (Recommended)
1. Double-click \setup.bat\
2. Wait for installation to complete
3. Double-click \un.bat\ to start the server
4. Open http://127.0.0.1:5000 in your browser

### Option 2: Manual Setup
1. Open Command Prompt or PowerShell
2. Navigate to the project folder
3. Run:
   \\\
   cd backend
   python -m pip install -r requirements.txt
   python app.py
   \\\
4. Open http://127.0.0.1:5000 in your browser

## Using the Application

### Downloading a Video
1. Find the YouTube video you want to download
2. Copy the URL from the address bar
3. Paste it into the URL input field on the website
4. Click the **Download** button
5. Wait for the download to complete (usually 1-10 minutes depending on video size)
6. You'll see a success message with the video details

### Viewing Downloaded Videos
- All your downloaded videos appear in the "Downloaded Videos" section
- Each video card shows:
  - Video title
  - File size (MB)
  - Download date
  - Two action buttons

### Downloading a Video to Your Device
- Click the **⬇ Download** button on any video card
- This will download the video file to your default downloads folder

### Deleting a Video
- Click the **🗑 Delete** button on any video card
- Confirm the deletion in the popup
- The video will be removed from storage

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| Enter | Submit download (when URL field is focused) |
| Ctrl+A | Select all text in URL field |

## Common Issues & Solutions

### Issue: Server won't start
**Solution:**
- Make sure port 5000 is not in use
- Try changing the port in \ackend/app.py\ line 214
- Check Python is properly installed: \python --version\

### Issue: Download fails
**Solution:**
- Check if the YouTube URL is correct
- Verify your internet connection
- Try a different video
- Check if the video is available in your country

### Issue: Website looks broken
**Solution:**
- Hard refresh the page: Ctrl+F5 (or Cmd+Shift+R on Mac)
- Clear browser cache
- Try a different browser

### Issue: Can't see downloaded videos
**Solution:**
- Make sure the backend is running
- Check if the downloads folder exists
- Refresh the page

### Issue: Files won't delete
**Solution:**
- Make sure the file is not in use elsewhere
- Check file permissions
- Restart the server and try again

## Tips for Best Performance

1. **Use a wired connection**: Faster and more stable than WiFi
2. **Close other applications**: Frees up system resources
3. **Choose quality appropriately**: 1080p videos take longer to download
4. **Check available disk space**: Ensure you have enough storage
5. **Use during off-peak hours**: Better speeds when less network congestion

## Supported Video Formats

- MP4 (recommended)
- WebM
- MKV
- FLV
- And many more (auto-detected by yt-dlp)

## Storage Locations

### Downloaded Videos
- Windows: \C:\\Users\\[YourUsername]\\Downloads\\YOUTUBE_VIDEO_DOWNLOADER\\downloads\\\
- Videos are stored in the \downloads\ folder

### Video Database
- A \ideos_list.json\ file maintains the list of all downloaded videos

---

**Need more help?** Check the main README.md file for detailed documentation.
