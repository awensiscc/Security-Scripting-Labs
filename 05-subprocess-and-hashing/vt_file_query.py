import os
import sys
import requests
import json

# set your API key as an environment variable for security - see instructions.
VT_API_KEY = os.environ.get('VT_API_KEY', 'YOUR_API_KEY_HERE')
print(VT_API_KEY)
# VT API endpoint for file reports
VT_API_URL = 'https://www.virustotal.com/api/v3/files/'
hash1 = 'f6e1a146543d2903146698da5698b2a214201720c0be756c6e8d2a2f27dcfaff'

def query_virustotal(file_hash):
    """
    Query VirusTotal API with the hash
    """
    headers = {
        'x-apikey': VT_API_KEY
    }

    try:
        response = requests.get(
            f"{VT_API_URL}{file_hash}",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(e)




if __name__ == "__main__":

   # if len(sys.argv) != 2:
    #    print(f"Usage: {sys.argv[0]} <file_hash>", file=sys.stderr)
     #   sys.exit(1)

   # file_hash = sys.argv[1]  # hash from command line argument

    # Query VT and capture the results
    vt_results = query_virustotal(hash1)

    print
    if vt_results is None:
        sys.exit(0)  # No results or error already printed
    with open('vt_output.json', 'w') as f:
        json.dump(vt_results, f, indent=4)

    attributes = vt_results['data']['attributes']
    stats = attributes.get('last_analysis_stats', {})

    malicious = stats.get('malicious', 0)
    suspicious = stats.get('suspicious', 0)
    undetected = stats.get('undetected', 0)

    total = malicious + suspicious + undetected + stats.get('harmless', 0)

    print(f"\n[+] Detections: {malicious}/{total}")
    print(f"    Malicious:   {malicious}")
    print(f"    Suspicious:  {suspicious}")
    print(f"    Undetected:  {undetected}")