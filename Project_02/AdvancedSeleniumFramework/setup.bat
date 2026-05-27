@echo off
REM ======================================
REM Salesforce Selenium Framework Setup
REM ======================================

echo.
echo [INFO] Checking Java installation...
java -version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Java is not installed!
    echo [INFO] Please install Java 11+ from: https://www.oracle.com/java/technologies/downloads/
    exit /b 1
)

echo [INFO] Java found successfully
echo.
echo [INFO] Checking Maven installation...
mvn -version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Maven is not installed!
    echo [INFO] Please install Maven from: https://maven.apache.org/download.cgi
    echo [INFO] Or use: choco install maven (if you have Chocolatey)
    exit /b 1
)

echo [INFO] Maven found successfully
echo.
echo [INFO] ========================================
echo [INFO] Installing Framework Dependencies
echo [INFO] ========================================
echo.

cd /d "%~dp0"
call mvn clean install

if %errorlevel% equ 0 (
    echo.
    echo [SUCCESS] Framework setup complete!
    echo [INFO] To run tests, execute: run-tests.bat
    exit /b 0
) else (
    echo [ERROR] Maven build failed!
    exit /b 1
)
