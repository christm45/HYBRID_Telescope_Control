@echo off
REM ================================================================================
REM Script d'initialisation des modèles ML
REM Génère tous les modèles Machine Learning nécessaires
REM ================================================================================

echo.
echo ================================================================================
echo INITIALISATION DES MODELES MACHINE LEARNING
echo ================================================================================
echo.
echo Ce script va generer tous les modeles ML necessaires pour le tracking avance.
echo.
echo Duree estimee : 1-2 minutes
echo.

REM Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH
    echo.
    echo Installez Python 3.10+ depuis : https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python detecte
echo.

REM Vérifier si le script existe
if not exist "initialize_ml_models.py" (
    echo [ERREUR] Le fichier initialize_ml_models.py est introuvable
    echo.
    echo Assurez-vous d'executer ce script depuis le dossier principal
    echo de l'application.
    echo.
    pause
    exit /b 1
)

echo [OK] Script d'initialisation trouve
echo.

REM Exécuter le script d'initialisation
echo Lancement de l'initialisation...
echo.
python initialize_ml_models.py

REM Vérifier le résultat
if errorlevel 1 (
    echo.
    echo ================================================================================
    echo [ERREUR] L'initialisation a echoue
    echo ================================================================================
    echo.
    echo Consultez les messages d'erreur ci-dessus pour plus d'informations.
    echo.
) else (
    echo.
    echo ================================================================================
    echo [SUCCES] Initialisation terminee !
    echo ================================================================================
    echo.
)

echo.
echo Appuyez sur une touche pour fermer cette fenetre...
echo.
pause >nul
exit /b

