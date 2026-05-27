@echo off
REM ======================================
REM Run Single Test Case
REM ======================================

cd /d "%~dp0"

echo.
echo [INFO] ========================================
echo [INFO] Running Single Test: testLoginPageLoad
echo [INFO] ========================================
echo.

call mvn test -Dtest=LoginTestValid#testLoginPageLoad -X

if %errorlevel% equ 0 (
    echo.
    echo [SUCCESS] Test completed successfully!
    echo [INFO] View logs: logs\automation-framework.log
) else (
    echo.
    echo [ERROR] Test execution failed!
    echo [INFO] Check logs\automation-framework.log for details
)

pause
