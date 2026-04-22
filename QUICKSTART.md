# Quick Start Guide - YouTube Video Downloader

## 📋 Installation & Setup (Windows)

### Option 1: Automatic Setup (Recommended)
1. **Extract the project** to any folder
2. **Double-click `setup.bat`** 
   - This will automatically install Python dependencies
   - Wait for completion
3. **Double-click `run.bat`**
   - Server will start
   - A command window will appear
4. **Open your browser**: http://127.0.0.1:5000
5. **Start downloading!**

### Option 2: Manual Setup (Command Prompt)
1. Press `Win + R`, type `cmd`, press Enter
2. Navigate to the project folder:
   ```
   cd Downloads\YOUTUBE_VIDEO_DOWNLOADER
   ```
3. Install dependencies:
   ```
   cd backend
   python -m pip install -r requirements.txt
   cd ..
   ```
4. Start the server:
   ```
   cd backend
   python app.py
   ```
5. Open browser: http://127.0.0.1:5000

### Option 3: Using PowerShell
1. Open PowerShell
2. Navigate to project folder
3. Run: `.\setup.bat`
4. Run: `.\run.bat`
5. Open browser: http://127.0.0.1:5000

## 🎬 How to Download a Video

### Step 1: Get the YouTube URL
- Go to youtube.com
- Find the video you want to download
- Copy the URL from the address bar (e.g., https://www.youtube.com/watch?v=...)

### Step 2: Paste and Download
- Return to http://127.0.0.1:5000
- Paste the URL in the input field
- Click the **Download** button (or press Enter)

### Step 3: Wait
- Green progress bar will appear
- "Downloading..." message shows progress
- Wait 1-10 minutes depending on video size

### Step 4: Success!
- Green success message appears
- Video title and size are shown
- Video appears in "Downloaded Videos" section below

## 📦 Manage Your Downloads

### Download Video to Your Computer
1. Find the video in "Downloaded Videos" section
2. Click the **⬇ Download** button
3. Choose where to save (default: Downloads folder)
4. Video is now on your computer!

### Delete a Video
1. Find the video in "Downloaded Videos" section
2. Click the **🗑 Delete** button
3. Confirm deletion
4. Video is removed and disk space is freed

## ⌨️ Keyboard Shortcuts

| Shortcut | What it does |
|----------|-------------|
| **Enter** | Download (when URL field is focused) |
| **Ctrl+F5** | Hard refresh page (clears cache) |
| **F12** | Open developer tools (for troubleshooting) |

## 🔧 Troubleshooting

### ❌ Problem: "Server not running" or page won't load

**Solution:**
- Make sure `run.bat` is running (check for open command window)
- If no window appears, try manual setup with PowerShell
- Check that port 5000 is not blocked by another application

### ❌ Problem: Download button doesn't work

**Solution:**
- Check if URL is a valid YouTube link
- Try copying URL again carefully
- Make sure internet connection is working
- Try a different YouTube video

### ❌ Problem: "Download failed" error message

**Solutions:**
- Verify the YouTube URL is correct
- Check your internet connection
- Try a different video (might be restricted)
- Check available disk space (videos need space)
- The video might be unavailable in your region

### ❌ Problem: Can't see downloaded videos

**Solutions:**
- Make sure server is still running
- Refresh the page: **F5** or **Ctrl+R**
- Hard refresh: **Ctrl+F5**
- Check if downloads folder exists
- Restart the server

### ❌ Problem: File won't delete

**Solution:**
- Make sure the file isn't being used by another program
- Close any media players
- Restart the server and try again

### ❌ Problem: "Port 5000 already in use"

**Solution:**
- Close any other running Flask applications
- Or change port in `backend/app.py`:
  ```python
  # Find this line:
  app.run(debug=True, host='127.0.0.1', port=5000)
  # Change 5000 to another number like 5001
  ```

### ❌ Problem: Website looks broken (no colors, misaligned)

**Solution:**
- Hard refresh: **Ctrl+F5**
- Clear browser cache:
  - Chrome: Ctrl+Shift+Delete
  - Firefox: Ctrl+Shift+Delete
  - Edge: Ctrl+Shift+Delete
- Try a different browser
- Check browser console (F12) for errors

### ❌ Problem: Python/dependencies error

**Solution:**
- Make sure Python 3.8+ is installed: `python --version`
- Reinstall dependencies:
  ```
  cd backend
  python -m pip install --upgrade -r requirements.txt
  ```

## ⚡ Performance Tips

1. **Use wired connection**: Faster than WiFi for large downloads
2. **Close other applications**: Frees up RAM and bandwidth
3. **Check disk space**: Ensure you have 10GB+ free
4. **Download during off-peak**: Typically faster at night
5. **Don't close browser**: During download, keep browser open
6. **Use recent browser**: Newer browsers work better

## 🎯 Best Practices

✅ **DO:**
- Download content you have rights to
- Check video length before downloading
- Keep an eye on disk space
- Use standard YouTube URLs

❌ **DON'T:**
- Download copyrighted content without permission
- Leave server running 24/7 (unless needed)
- Download entire channels without permission
- Download too many videos at once

## 💾 Storage Information

### Where are videos saved?
- **Location**: `YOUTUBE_VIDEO_DOWNLOADER/downloads/`
- **Database**: Videos list in `downloads/videos_list.json`

### How much space does a video take?
- **Typical SD (480p)**: 50-150 MB
- **Typical HD (720p)**: 200-500 MB
- **Typical Full HD (1080p)**: 500-1500 MB
- **Typical 4K**: 2000+ MB

### Storage Management
- Videos folder can be safely moved
- Delete videos using the delete button
- Or manually delete from `downloads` folder

## 🌐 Accessing from Other Devices

### Same WiFi Network:
- Find your computer IP: `ipconfig` in Command Prompt
- Look for "IPv4 Address" (e.g., 192.168.1.100)
- From other device, visit: http://192.168.1.100:5000

### Note**: Only accessible if server is running

## 🔒 Security & Privacy

- Videos are stored on your computer
- No data is sent to any external server
- Your URLs are not logged or shared
- Only works for personal use

## 📞 Getting More Help

1. **Check README.md** - Comprehensive documentation
2. **Check ARCHITECTURE.md** - Technical details
3. **Browser Console (F12)** - See error messages
4. **Server Output** - Check command window for logs

## ✨ Common Use Cases

### Use Case 1: Download educational content
```
✓ Great for: Tutorials, lectures, documentaries
✓ Tip: Check if creator allows downloads
```

### Use Case 2: Offline viewing
```
✓ Great for: Travel, places without internet
✓ Tip: Download in advance
```

### Use Case 3: Backup personal videos
```
✓ Great for: Your own uploads
✓ Tip: Keep backups in multiple locations
```

---

**Need Help?** Check the troubleshooting section above or review the main README.md

**Version**: 1.0.0
**Last Updated**: April 2024
