# Salesforce Selenium Framework - Run Single Test
# Run with: powershell -ExecutionPolicy Bypass -File run-single-test.ps1

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Salesforce Selenium - Run Single Test" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

Set-Location $PSScriptRoot

Write-Host "[INFO] Test: LoginTestValid#testLoginPageLoad" -ForegroundColor Yellow
Write-Host "[INFO] Description: Verify login page loads successfully" -ForegroundColor Yellow
Write-Host ""
Write-Host "[INFO] Executing test..." -ForegroundColor Yellow
Write-Host ""

mvn test -Dtest=LoginTestValid#testLoginPageLoad -X

Write-Host ""
if ($LASTEXITCODE -eq 0) {
    Write-Host "[SUCCESS] Test completed successfully!" -ForegroundColor Green
    Write-Host "[INFO] View logs: logs\automation-framework.log" -ForegroundColor Cyan
} else {
    Write-Host "[ERROR] Test execution failed!" -ForegroundColor Red
    Write-Host "[INFO] Check logs\automation-framework.log for details" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
