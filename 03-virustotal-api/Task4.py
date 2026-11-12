
import os
import requests
import json
import base64


VT_API_KEY = os.environ.get('VT_API_KEY', 'YOUR_API_KEY_HERE')


VT_API_URL = "https://www.virustotal.com/api/v3/urls/"



def url_query(line):

    headers = {
        'x-apikey': VT_API_KEY
    }

    response = requests.get(url=f"{VT_API_URL}{line}", headers=headers)

    data = json.loads(response.text)

    attributes = data['data']['attributes']
    stats = attributes.get('last_analysis_stats', {})
    label = attributes.get('categories')

    file_type = data['data']['type']
    malicious = stats.get('malicious', 0)
    suspicious = stats.get('suspicious', 0)
    undetected = stats.get('undetected', 0)

    total = malicious + suspicious + undetected + stats.get('harmless', 0)

    print(f"\nFile type: {file_type}")
    print(f"[+] Detections: {malicious}/{total}")
    print(f"    Malicious:   {malicious}")
    print(f"    Suspicious:  {suspicious}")
    print(f"    Undetected:  {undetected}")
    print(f"Suggested threat labels: \n{label}")

def base64_encode(value: str) -> str:
    encoded = base64.urlsafe_b64encode(str.encode(value))
    result = encoded.rstrip(b"=")
    return result.decode()

prompt = str(input("Please enter a URL for scan:"))

result = base64_encode(prompt)
url_query(result)
