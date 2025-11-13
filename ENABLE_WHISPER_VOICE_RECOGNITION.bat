@echo off
REM Enable Whisper Voice Recognition - Download Model
REM This script downloads the Whisper model for best voice recognition

title Whisper Model Downloader
color 0A

echo ========================================================================
echo.
echo                  WHISPER MODEL DOWNLOADER
echo                  For Best Voice Recognition
echo.
echo ========================================================================
echo.
echo This will download the OpenAI Whisper model for voice recognition.
echo.
echo BENEFITS:
echo   - Best voice recognition accuracy (90%+ for English)
echo   - Offline operation (no internet needed after download)
echo   - Noise resistant
echo   - Natural language understanding
echo.
echo REQUIREMENTS:
echo   - Internet connection (for download only)
echo   - 75-500 MB disk space (depending on model)
echo   - Download time: 1-5 minutes
echo.
echo ========================================================================
echo.
pause
echo.

REM Run the Python downloader script
python download_whisper_model.py

echo.
echo ========================================================================
echo.
if %ERRORLEVEL% EQU 0 (
    echo SUCCESS! Whisper model downloaded.
    echo.
    echo NEXT: Restart the application to use Whisper voice recognition!
) else (
    echo ERROR: Download failed. Check error messages above.
)
echo.
echo ========================================================================
echo.
echo Appuyez sur une touche pour fermer cette fenetre...
echo.
pause >nul
exit /b

