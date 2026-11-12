import requests
import json
import os




# set your API key as an environment variable for security - see instructions.
ABUSEIPDB_API_KEY = os.environ.get("ABUSEIPDB_API_KEY", "your_abuse_key_here")
# VT API endpoint for file reports
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

        # Formatted output
    data = json.loads(response.text)

    print(data)
    print("IP{line}:","Confidence score:",data["data"]["abuseConfidenceScore"])
    print("Country:",data['data']["countryName"])
    print("Is IP whitelisted:", data['data']["isWhitelisted"])
