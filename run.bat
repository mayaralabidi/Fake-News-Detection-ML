@echo off
REM Quick Start Installation and Run Script for Windows
REM Run this to set up and start both frontend and backend

echo.
echo =====================================================
echo FAKE NEWS DETECTION - Quick Start Setup (Windows)
echo =====================================================
echo.

REM Check Python
echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python 3.8+
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do echo [OK] %%i
echo.

REM Check Node.js
echo Checking Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not found. Please install Node.js 18+
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('node --version') do echo [OK] Node.js %%i
for /f "tokens=*" %%i in ('npm --version') do echo [OK] npm %%i
echo.

REM Install Python dependencies
echo Installing Python dependencies...
pip install flask flask-cors pandas numpy scikit-learn nltk
if errorlevel 1 (
    echo [ERROR] Failed to install Python dependencies
    pause
    exit /b 1
)
echo [OK] Python dependencies installed
echo.

REM Install Frontend dependencies
echo Installing Frontend dependencies...
cd frontend
call npm install
if errorlevel 1 (
    echo [ERROR] Failed to install npm dependencies
    pause
    exit /b 1
)
cd ..
echo [OK] Frontend dependencies installed
echo.

echo =====================================================
echo Setup Complete! 
echo =====================================================
echo.

echo Running Flask Backend (http://localhost:5000)...
start cmd /k python app.py

timeout /t 2 /nobreak

echo Running Next.js Frontend (http://localhost:3000)...
cd frontend
call npm run dev
