# system_info.ps1
$report = [PSCustomObject]@{
    ComputerName = $env:COMPUTERNAME
    OS = (Get-ComputerInfo | Select-Object -ExpandProperty WindowsProductName) + " " + (Get-ComputerInfo | Select-Object -ExpandProperty WindowsVersion)
    CurrentUser = $env:USERNAME
    IPAddresses = Get-NetIPAddress | Where-Object { $_.AddressFamily -eq "IPv4" } | Select IPAddress, InterfaceAlias
}

$report | ConvertTo-Json | Out-File system_info.json