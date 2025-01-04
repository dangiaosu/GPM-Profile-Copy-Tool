@echo off
:: Kiểm tra Python đã được cài đặt hay chưa
echo Checking if Python is installed...
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python before proceeding.
    pause
    exit /b
)
echo Python is installed.
echo ================================================

:: Kiểm tra kết nối mạng
echo Checking network connectivity...
ping www.google.com -n 1 >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo No network connection detected. Please check your internet connection and try again.
    pause
    exit /b
)
echo Network connection is active.
echo ================================================

:: Kiểm tra nếu pip chưa được cài đặt
echo Ensuring pip is available...
python -m ensurepip --default-pip >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Failed to ensure pip is available. Please check your Python installation.
    pause
    exit /b
)
echo Pip is available.
echo ================================================

:: Cài đặt các thư viện cần thiết
echo Installing required Python libraries...
pip install pandas >nul
pip install openpyxl >nul
python -c "import tkinter" >nul 2>&1 || (
    echo Tkinter is missing. Please install or enable it manually.
    pause
    exit /b
)
echo All required libraries are installed.
echo ================================================

:: Chạy script chính
echo Running the application...
python copy_dangiaosu.py
if %ERRORLEVEL% NEQ 0 (
    echo An error occurred while running the script.
    pause
    exit /b
)
pause
