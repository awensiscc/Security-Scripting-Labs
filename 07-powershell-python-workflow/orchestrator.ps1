# orchestrator.ps1
Write-Host "[*] Collecting IP addresses..."
.\ip_list.ps1

Write-Host "[*] Running IP lookup..."
python .\ip_lookup.py

Write-Host "[+] Workflow complete. Check ip_report.json for results."