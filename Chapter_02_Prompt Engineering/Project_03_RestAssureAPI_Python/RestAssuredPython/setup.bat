@echo off
REM setup.bat - Initialize REST Assured Python framework for Windows

echo Setting up REST Assured Python Framework...

REM Create directories
if not exist src\config mkdir src\config
if not exist src\assertions mkdir src\assertions
if not exist src\data mkdir src\data
if not exist src\endpoints mkdir src\endpoints
if not exist tests mkdir tests
if not exist logs mkdir logs
if not exist reports mkdir reports

echo Project structure created

REM Install dependencies
echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Installation complete!
echo.
echo Next steps:
echo 1. Configure .env file (if needed)
echo 2. Run: pytest -v
echo 3. Check logs in logs directory
echo 4. View report in reports\report.html
echo.
pause
