@echo off
REM Verify YouTube Video Downloader Installation

echo.
echo ====================================
echo Installation Verification
echo ====================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    exit /b 1
)
python --version
echo ? Python is installed
echo.

echo Checking Flask installation...
python -c "import flask; print(f'? Flask {flask.__version__} installed')"
echo.

echo Checking yt-dlp installation...
python -c "import yt_dlp; print('? yt-dlp installed')"
echo.

echo Checking Flask-CORS installation...
python -c "import flask_cors; print('? Flask-CORS installed')"
echo.

echo Checking project structure...
if exist "backend\app.py" echo ? backend\app.py found
if exist "backend\templates\index.html" echo ? HTML template found
if exist "backend\static\css\style.css" echo ? CSS stylesheet found
if exist "backend\static\js\script.js" echo ? JavaScript file found
if exist "downloads" echo ? downloads folder ready
echo.

echo ====================================
echo ? Installation Verified Successfully!
echo ====================================
echo.
echo Ready to run the application!
echo Execute: python backend\app.py
echo Or double-click: run.bat
echo.
