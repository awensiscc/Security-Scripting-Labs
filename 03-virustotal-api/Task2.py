import requests
import json
import os

ABUSEIPDB_API_KEY = os.environ.get("ABUSEIPDB_API_KEY", "your_abuse_key_here")

ABUSEIPDB_API_URL = 'https://api.abuseipdb.com/api/v2/check'

with open ('ip_list.txt','r') as file:
    lines = file.read().splitlines()

url = ABUSEIPDB_API_URL
for line in lines:

    querystring = {
            'ipAddress': line,
            'maxAgeInDays': '90'
    }

    headers = {
            'Accept': 'application/json',
            'Key': ABUSEIPDB_API_KEY
    }

    response = requests.request(method='GET', url=url, headers=headers, params=querystring)


    data = json.loads(response.text)

    print(f"IP {line}:","\nConfidence score:",data["data"]["abuseConfidenceScore"])
    print("Country:",data["data"]["countryCode"])
    print("Is IP whitelisted:", data['data']["isWhitelisted"])
    print("\n")
