# user_audit.ps1
$threshold = (Get-Date).AddDays(-28)
$users = Get-LocalUser | Where-Object { 
    $_.LastLogon -gt $threshold -or $_.PasswordLastSet -gt $threshold 
}
$admins = Get-LocalGroupMember -Group "Administrators"

$output = [PSCustomObject]@{
    SuspiciousUsers = $users
    Administrators = $admins
}

$output | ConvertTo-Json -Depth 4 | Out-File user_audit.json