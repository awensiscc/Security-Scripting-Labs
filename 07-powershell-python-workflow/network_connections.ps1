# network_connections.ps1
$connections = Get-NetTCPConnection

$results = @()
foreach ($conn in $connections) {
    $process = Get-Process -Id $conn.OwningProcess -ErrorAction SilentlyContinue
    
    $result = [PSCustomObject]@{
        LocalPort = $conn.LocalPort
        RemoteAddress = $conn.RemoteAddress
        RemotePort = $conn.RemotePort
        State = $conn.State
        ProcessId = $conn.OwningProcess
        ProcessName = if ($process) { $process.ProcessName } else { "unknown" }
        ProcessPath = if ($process) { $process.Path } else { "unknown" }
    }
    
    $results += $result
}

$results | ConvertTo-Json -Depth 3 | Out-File network_connections.json