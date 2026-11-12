# ip_list.ps1
$connections = Get-NetTCPConnection
$ips = $connections | Select-Object -ExpandProperty RemoteAddress -Unique
$ips | Out-File ip_list.txt