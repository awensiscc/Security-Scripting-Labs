# ip_lookup.py
import requests
import json
import os


api = os.environ.get("ABUSEIPDB_API_KEY")
url = "https://api.abuseipdb.com/api/v2/check"

with open("ip_list.txt", "r") as f:
    ips = f.read().splitlines()

results = []
for ip in ips:
    if ip and ip != "0.0.0.0":
        headers = {"Key": api, "Accept": "application/json"}
        params = {"ipAddress": ip, "maxAgeInDays": "90"}
        
        result = requests.get(url, headers=headers, params=params)
        if result.status_code == 200:
            data = result.json()
            results.append({
                "IP addr": ip,
                "Abuse_Score": data["data"]["abuseConfidenceScore"],
                "Country code": data["data"]["countryCode"]
            })

with open("ip_report.json", "w") as f:
    json.dump(results, f, indent=2)