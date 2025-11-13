@echo off
REM ========================================
REM Install psutil for System Monitoring
REM HYBRID Telescope Control v7.0
REM ========================================

TITLE Install psutil - System Monitoring

REM Force window to stay open
setlocal

color 0B

echo.
echo ========================================
echo   INSTALL PSUTIL
echo   System Monitoring Module
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found!
    echo.
    echo Please install Python 3.10+ from python.org
    echo.
    echo Appuyez sur une touche pour fermer...
    pause >nul
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Check if psutil already installed
echo [*] Checking if psutil is already installed...
python -c "import psutil; print(f'psutil version {psutil.__version__} already installed')" >nul 2>&1
if %errorlevel%==0 (
    echo.
    echo [OK] psutil is already installed!
    python -c "import psutil; print(f'     Version: {psutil.__version__}')"
    echo.
    echo No action needed.
    echo.
    goto :SUCCESS
)

echo [INFO] psutil not found, installing...
echo.

REM Install psutil
echo ========================================
echo [*] Installing psutil...
echo ========================================
echo.

python -m pip install --upgrade pip
python -m pip install psutil>=5.9.0

if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo [ERROR] Installation failed!
    echo ========================================
    echo.
    echo Possible solutions:
    echo 1. Run as Administrator
    echo 2. Check internet connection
    echo 3. Try: python -m pip install --user psutil
    echo.
    echo Appuyez sur une touche pour fermer...
    pause >nul
    exit /b 1
)

echo.
echo ========================================
echo [SUCCESS] psutil installed!
echo ========================================
echo.

REM Verify installation
python -c "import psutil; print(f'Version: {psutil.__version__}')"
python -c "import psutil; print(f'CPU cores: {psutil.cpu_count()} logical')"
python -c "import psutil; print(f'Memory: {psutil.virtual_memory().total / (1024**3):.1f} GB')"

echo.

:SUCCESS
echo ========================================
echo.
echo psutil is now ready!
echo.
echo Benefits:
echo   ✅ Real-time CPU usage monitoring
echo   ✅ Memory usage tracking
echo   ✅ System performance metrics
echo   ✅ Better diagnostics
echo.
echo Next step:
echo   Restart HYBRID Telescope Control to see system info
echo.
echo ========================================
echo.
echo Appuyez sur une touche pour fermer cette fenetre...
echo.

pause >nul

