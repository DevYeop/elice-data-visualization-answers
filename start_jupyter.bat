@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
    echo Local Python environment was not found. See README.md.
    pause
    exit /b 1
)
".venv\Scripts\python.exe" -m notebook --ServerApp.root_dir="%~dp0." --ServerApp.ip=127.0.0.1
if errorlevel 1 pause
