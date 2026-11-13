# Security Scripting Labs

Weekly lab work from the **Advanced Scripting for Cyber Security** module, BSc Applied
Cybersecurity & Digital Forensics, TU Dublin (Year 2, Sept to Dec 2025). Python and PowerShell
for everyday security tasks: parsing logs, hashing files and checking indicators against threat
intelligence APIs.

**Individual work.** The lecturer set the exercises; this repo holds my own work through them, week by week. The module's pair project, built on these labs, is [BeSecure](https://github.com/awensiscc/BeSecure).

| Folder | What it covers |
|---|---|
| `01-python-basics` | Warm-up exercises (A1 to C3), parsing JSON/CSV/log files |
| `02-files-and-data` | Reading and writing files, simple data processing |
| `03-virustotal-api` | Querying the VirusTotal API from Python |
| `04-csv-and-log-parsing` | Naive vs regex log parsers, counting failed logins, CSV read/write |
| `05-subprocess-and-hashing` | Running system commands with `subprocess`, SHA-256 hashing, VT file lookups |
| `06-hash-and-ip-reputation` | Bulk hash lookups (VirusTotal) and IP reputation (AbuseIPDB) |
| `07-powershell-python-workflow` | PowerShell collects connections/users/system info, Python enriches IPs; `orchestrator.ps1` runs it all |

## API keys
Scripts read keys from environment variables, never from the code:
```powershell
$env:VT_API_KEY = "<virustotal key>"
$env:ABUSEIPDB_API_KEY = "<abuseipdb key>"
```
