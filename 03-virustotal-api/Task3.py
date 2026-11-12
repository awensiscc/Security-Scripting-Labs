import os
import requests
import json


VT_API_KEY = os.environ.get('VT_API_KEY', 'YOUR_API_KEY_HERE')


VT_API_URL = 'https://www.virustotal.com/api/v3/files/'


data={}
with open ('suspect_hashes.txt','r') as file:
    lines = file.read().splitlines()
for line in lines:

    headers = {
        'x-apikey': VT_API_KEY
    }

    response = requests.get(url=f"{VT_API_URL}{line}", headers=headers, timeout = 10)

    data = json.loads(response.text)

    print(f"""HASH: /{line}/ :""")

    attributes = data['data']['attributes']
    stats = attributes.get('last_analysis_results', {})

    for key,value in stats.items():
        print(key,": ",value.get('result'))

    print('\n')
