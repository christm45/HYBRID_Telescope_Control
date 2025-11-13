@echo off
setlocal enabledelayedexpansion

echo.
echo ================================================================================
echo DIAGNOSTIC SIMPLE - HYBRID Telescope Control
echo ================================================================================
echo.
echo Ce script va afficher des informations pour diagnostiquer le probleme.
echo.
echo Appuyez sur une touche pour continuer...
pause >nul

echo.
echo [1/5] Repertoire actuel :
cd
echo.

echo [2/5] Presence de NSIS :
if exist "C:\Program Files (x86)\NSIS\makensis.exe" (
    echo [OK] NSIS trouve dans C:\Program Files (x86)\NSIS\
    "C:\Program Files (x86)\NSIS\makensis.exe" /VERSION
) else if exist "C:\Program Files\NSIS\makensis.exe" (
    echo [OK] NSIS trouve dans C:\Program Files\NSIS\
    "C:\Program Files\NSIS\makensis.exe" /VERSION
) else (
    echo [ERREUR] NSIS n'est pas installe
    echo.
    echo Telechargez-le depuis : https://nsis.sourceforge.io/Download
)
echo.

echo [3/5] Fichier installer_v7_complete.nsi :
if exist "installer_v7_complete.nsi" (
    echo [OK] Fichier trouve
    for %%A in ("installer_v7_complete.nsi") do echo Taille: %%~zA octets
) else (
    echo [ERREUR] Fichier introuvable
)
echo.

echo [4/5] Fichiers critiques :
if exist "voice_control_hybrid.py" (echo [OK] voice_control_hybrid.py) else (echo [X] voice_control_hybrid.py MANQUANT)
if exist "ml_model_trainer.py" (echo [OK] ml_model_trainer.py) else (echo [X] ml_model_trainer.py MANQUANT)
if exist "initialize_ml_models.py" (echo [OK] initialize_ml_models.py) else (echo [X] initialize_ml_models.py MANQUANT)
if exist "requirements.txt" (echo [OK] requirements.txt) else (echo [X] requirements.txt MANQUANT)
if exist "LICENSE.txt" (echo [OK] LICENSE.txt) else (echo [X] LICENSE.txt MANQUANT)
if exist "README.md" (echo [OK] README.md) else (echo [X] README.md MANQUANT)
if exist "icon.ico" (echo [OK] icon.ico) else (echo [ATTENTION] icon.ico MANQUANT - NSIS echouera!)
echo.

echo [5/5] Fichiers .bat dans ce dossier :
dir /b *.bat
echo.

echo ================================================================================
echo DIAGNOSTIC TERMINE
echo ================================================================================
echo.
echo Si vous voyez [ERREUR] ci-dessus, c'est la cause du probleme.
echo.
echo Copiez ces informations si vous avez besoin d'aide.
echo.
echo Appuyez sur une touche pour fermer cette fenetre...
echo.
pause >nul
exit /b

