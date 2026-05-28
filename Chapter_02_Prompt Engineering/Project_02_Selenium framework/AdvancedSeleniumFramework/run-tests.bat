@echo off
REM ======================================
REM Run Selenium Tests
REM ======================================

cd /d "%~dp0"

echo.
echo [INFO] ========================================
echo [INFO] Running Salesforce Login Tests
echo [INFO] ========================================
echo.

REM Check if Constants need credentials
find /i "your-valid-email" src\main\java\com\salesforce\config\Constants.java >nul 2>&1
if %errorlevel% equ 0 (
    echo [WARNING] Test credentials not configured!
    echo [WARNING] Please update Constants.java with valid credentials:
    echo [INFO] Edit: src\main\java\com\salesforce\config\Constants.java
    echo [INFO] Update VALID_USERNAME and VALID_PASSWORD
    exit /b 1
)

echo [INFO] Running all tests...
echo.
call mvn test -X

if %errorlevel% equ 0 (
    echo.
    echo [SUCCESS] Tests completed!
    echo [INFO] View logs: logs\automation-framework.log
    echo [INFO] View report: target\surefire-reports\index.html
) else (
    echo.
    echo [ERROR] Test execution failed!
    echo [INFO] Check logs\automation-framework.log for details
)

pause
