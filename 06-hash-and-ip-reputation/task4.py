import base64
import os
import requests
import json


def base64_url(url):
    url_id = base64.urlsafe_b64encode(f"{url}".encode()).decode().strip("=")
    return url_id
def request():
    response = requests.get(
        VIRUSTOTAL_URL,
        headers=headers
    )
    decoded_response = json.loads(response.text)
    with open("results.json", "w") as file:
        json.dump(
            decoded_response,
            file,
            indent=3,
            separators=(", ", ": ")
        )
    print(f"Data for {url}:\n")
    print(f"     Number of detections: {decoded_response["data"]["attributes"]["last_analysis_stats"]["malicious"]}")
    print(f"     The file type: {decoded_response["data"]["type"]}")
    ### Don't know this part...
    # print(f"     Suggested threat label: {decoded_response["data"]["threat_names"]}")
    print("\n\n")

url = input("Enter a URL to check: ")
VT_API_KEY = os.environ.get("VT_API_KEY", "MY_VT_API_KEY")
VIRUSTOTAL_URL = f"https://www.virustotal.com/api/v3/urls/{base64_url(url)}"

headers = {
    "accept": "application/json",
    "x-apikey": VT_API_KEY
}

request()