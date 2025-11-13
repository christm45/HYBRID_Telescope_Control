@echo off
REM ========================================
REM Install GPU Support (CuPy)
REM HYBRID Telescope Control v7.0
REM by Bogdan Craciun
REM ========================================

TITLE Install GPU Support - HYBRID Telescope Control

color 0B

echo.
echo ========================================
echo   GPU ACCELERATION SETUP
echo   HYBRID Telescope Control v7.0
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found!
    echo.
    echo Please install Python 3.10+ first
    echo.
    pause
    goto :END
)

echo [OK] Python found
python --version
echo.

REM Detect NVIDIA GPU
echo [*] Detecting NVIDIA GPU...
echo.

nvidia-smi >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] nvidia-smi not found
    echo.
    echo This means either:
    echo   1. You don't have NVIDIA GPU
    echo   2. NVIDIA drivers not installed
    echo.
    echo GPU acceleration requires NVIDIA GPU with CUDA support.
    echo.
    echo If you have NVIDIA GPU:
    echo   Download drivers from: https://www.nvidia.com/download/index.aspx
    echo.
    echo Appuyez sur une touche pour continuer sans GPU...
    pause
    goto :END
)

echo [OK] NVIDIA GPU detected
echo.
nvidia-smi --query-gpu=name,driver_version,cuda_version --format=csv,noheader
echo.

REM Get CUDA version
echo [*] Detecting CUDA version...
echo.

for /f "tokens=3 delims=," %%v in ('nvidia-smi --query-gpu^=cuda_version --format^=csv^,noheader') do set CUDA_VER=%%v

echo CUDA Version: %CUDA_VER%
echo.

REM Determine CuPy version to install
set CUPY_PACKAGE=cupy-cuda12x

if "%CUDA_VER:~0,2%"=="11" (
    set CUPY_PACKAGE=cupy-cuda11x
    echo [*] CUDA 11.x detected - will install cupy-cuda11x
) else if "%CUDA_VER:~0,2%"=="12" (
    set CUPY_PACKAGE=cupy-cuda12x
    echo [*] CUDA 12.x detected - will install cupy-cuda12x
) else (
    echo [WARNING] CUDA version not clearly detected
    echo             Defaulting to cupy-cuda12x
    echo.
    echo If you have CUDA 11.x, use: pip install cupy-cuda11x
)

echo.
echo ========================================
echo [*] Installing %CUPY_PACKAGE%...
echo ========================================
echo.
echo This may take 5-10 minutes...
echo.

REM Upgrade pip first
python -m pip install --upgrade pip

REM Install CuPy
python -m pip install %CUPY_PACKAGE%

if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo [ERROR] Installation failed!
    echo ========================================
    echo.
    echo Possible solutions:
    echo.
    echo 1. Install CUDA Toolkit:
    echo    https://developer.nvidia.com/cuda-downloads
    echo.
    echo 2. Update NVIDIA drivers:
    echo    https://www.nvidia.com/download/index.aspx
    echo.
    echo 3. Try alternative installation:
    echo    pip install cupy-cuda11x  (for CUDA 11.x)
    echo    pip install cupy-cuda12x  (for CUDA 12.x)
    echo.
    echo 4. Or use CPU mode (GPU optional, not required)
    echo.
    goto :END
)

echo.
echo ========================================
echo [SUCCESS] GPU support installed!
echo ========================================
echo.

REM Test installation
echo [*] Testing GPU...
python -c "import cupy as cp; device = cp.cuda.Device(); props = cp.cuda.runtime.getDeviceProperties(0); print('[OK] GPU Name:', props['name'].decode('utf-8')); print('[OK] CUDA Compute:', str(props['major']) + '.' + str(props['minor'])); print('[OK] Memory:', round(device.mem_info[1] / (1024**3), 1), 'GB')"

if %errorlevel%==0 (
    echo.
    echo ========================================
    echo ✅ GPU ACCELERATION READY!
    echo ========================================
    echo.
    echo Benefits:
    echo   ✅ 5-10x faster star detection
    echo   ✅ Parallel plate solving
    echo   ✅ Real-time image processing
    echo   ✅ ML acceleration
    echo.
    echo Next step:
    echo   Restart HYBRID Telescope Control
    echo   GPU will be automatically detected and used
    echo.
) else (
    echo.
    echo [WARNING] GPU installed but test failed
    echo            The application will work but GPU may not be available
    echo.
)

:END
echo.
echo ========================================
echo.
echo Appuyez sur une touche pour fermer cette fenetre...
echo.
pause >nul
exit /b

