@echo off
TITLE YouTube Video Downloader - Setup
echo.
echo ================================
echo YouTube Video Downloader Setup
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [OK] Python found
python --version

echo.
echo Installing dependencies...
cd backend
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo To start the application:
echo 1. Navigate to the backend folder
echo 2. Run: python app.py
echo 3. Open browser to: http://127.0.0.1:5000
echo.
pause
