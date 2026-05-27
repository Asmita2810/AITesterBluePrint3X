# Salesforce Selenium Framework - Run Tests
# Run with: powershell -ExecutionPolicy Bypass -File run-tests.ps1

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Salesforce Selenium Framework - Run Tests" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

Set-Location $PSScriptRoot

# Check credentials
Write-Host "[INFO] Checking test credentials configuration..." -ForegroundColor Yellow
$constantsFile = "src\main\java\com\salesforce\config\Constants.java"

if (Select-String -Path $constantsFile -Pattern "your-valid-email" -Quiet) {
    Write-Host "[WARNING] Test credentials not configured!" -ForegroundColor Red
    Write-Host "[INFO] Please update Constants.java with valid credentials:" -ForegroundColor Yellow
    Write-Host "[INFO] Edit: $constantsFile" -ForegroundColor Yellow
    Write-Host "[INFO] Update VALID_USERNAME and VALID_PASSWORD" -ForegroundColor Yellow
    Write-Host ""
    exit 1
}

Write-Host "[OK] Credentials configured" -ForegroundColor Green
Write-Host ""
Write-Host "[INFO] Running all tests..." -ForegroundColor Yellow
Write-Host ""

mvn test -X

Write-Host ""
if ($LASTEXITCODE -eq 0) {
    Write-Host "[SUCCESS] Tests completed successfully!" -ForegroundColor Green
    Write-Host "[INFO] View logs: logs\automation-framework.log" -ForegroundColor Cyan
    Write-Host "[INFO] View report: target\surefire-reports\index.html" -ForegroundColor Cyan
} else {
    Write-Host "[ERROR] Test execution failed!" -ForegroundColor Red
    Write-Host "[INFO] Check logs\automation-framework.log for details" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
