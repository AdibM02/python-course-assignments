@echo off
REM Batch script to deploy UniProtKB Protein Finder to GitHub
REM Usage: deploy_to_github.bat "C:\path\to\uniprotkb-protein-finder"

setlocal enabledelayedexpansion

if "%~1"=="" (
    echo Usage: deploy_to_github.bat "path\to\destination"
    echo.
    echo Example:
    echo   deploy_to_github.bat "C:\Users\YourName\Documents\GitHub\uniprotkb-protein-finder"
    exit /b 1
)

set DEST=%~1
set SOURCE=%cd%

echo.
echo ════════════════════════════════════════════════════════
echo Deploying UniProtKB Protein Finder
echo ════════════════════════════════════════════════════════
echo.
echo Source: %SOURCE%
echo Destination: %DEST%
echo.

REM Create destination if needed
if not exist "%DEST%" (
    mkdir "%DEST%"
    echo Created destination directory
)

REM Copy files
echo.
echo Copying files...
for %%F in (main.py ui.py logic.py config.py requirements.txt .env.example LICENSE README.md .gitignore) do (
    if exist "%%F" (
        copy "%%F" "%DEST%\%%F" >nul
        echo   OK - %%F
    ) else (
        echo   SKIP - %%F ^(not found^)
    )
)

REM Copy .github directory
echo.
echo Copying directories...
if exist ".github" (
    xcopy ".github" "%DEST%\.github" /I /E /Y >nul
    echo   OK - .github/
) else (
    echo   SKIP - .github/ ^(not found^)
)

echo.
echo ════════════════════════════════════════════════════════
echo Deployment complete!
echo ════════════════════════════════════════════════════════
echo.
echo Next steps:
echo.
echo 1. Navigate to repository:
echo    cd "%DEST%"
echo.
echo 2. Initialize git:
echo    git init
echo.
echo 3. Add all files:
echo    git add .
echo.
echo 4. Create initial commit:
echo    git commit -m "Initial commit: UniProtKB Protein Finder"
echo.
echo 5. Add remote:
echo    git remote add origin https://github.com/yourusername/uniprotkb-protein-finder.git
echo.
echo 6. Set branch to main:
echo    git branch -M main
echo.
echo 7. Push to GitHub:
echo    git push -u origin main
echo.
pause
