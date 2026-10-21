@echo off
REM One-time setup for Windows: creates a virtual environment and installs dependencies.
echo Creating virtual environment...
py -3 -m venv .venv
if errorlevel 1 (
  echo Python launcher "py" not found. Install Python 3.11+ from python.org and tick "Add to PATH".
  exit /b 1
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo Setup complete. Run  run_app.bat  to start the application.
