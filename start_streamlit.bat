@echo off
setlocal
cd /d "%~dp0"
if "%~1"=="" (
    echo Drag a Streamlit Python file onto this batch file, or pass its path.
    pause
    exit /b 1
)
".venv\Scripts\python.exe" -m streamlit run "%~f1"
if errorlevel 1 pause
