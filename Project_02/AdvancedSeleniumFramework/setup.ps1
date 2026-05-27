# Salesforce Selenium Framework - Setup Script
# Run with: powershell -ExecutionPolicy Bypass -File setup.ps1

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Salesforce Selenium Framework - Setup" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Check Java
Write-Host "[INFO] Checking Java installation..." -ForegroundColor Yellow
try {
    $javaVersion = java -version 2>&1
    Write-Host "[OK] Java found:" -ForegroundColor Green
    Write-Host $javaVersion[0] -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Java not found!" -ForegroundColor Red
    Write-Host "[INFO] Please install Java 11+ from: https://www.oracle.com/java/technologies/downloads/" -ForegroundColor Yellow
    exit 1
}

# Check Maven
Write-Host ""
Write-Host "[INFO] Checking Maven installation..." -ForegroundColor Yellow
try {
    $mavenVersion = mvn -version 2>&1 | Select-Object -First 1
    Write-Host "[OK] Maven found:" -ForegroundColor Green
    Write-Host $mavenVersion -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Maven not found!" -ForegroundColor Red
    Write-Host "[INFO] Please install Maven from: https://maven.apache.org/download.cgi" -ForegroundColor Yellow
    exit 1
}

# Build project
Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Installing Framework Dependencies" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

Set-Location $PSScriptRoot
Write-Host "[INFO] Building project..." -ForegroundColor Yellow

mvn clean install

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "[SUCCESS] Framework setup complete!" -ForegroundColor Green
    Write-Host "[INFO] To run tests, execute: run-tests.ps1" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "[ERROR] Maven build failed!" -ForegroundColor Red
    exit 1
}
