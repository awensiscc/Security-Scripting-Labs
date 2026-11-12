import json
import os
import requests


def request():
    response = requests.request(
        method='GET',
        url=ABUSEIPDB_URL,
        headers=headers,
        params=querystring
    )
    decoded_response = json.loads(response.text)
    if os.path.exists("results.json"):
        with open("results.json", "a") as file:
            file.write(",\n")
            json.dump(
                decoded_response["data"],
                file,
                indent=3,
                separators=(", ", ": ")
            )
    else:
        with open("results.json", "w") as file:
            file.write('{ "data": [\n')
            json.dump(
                decoded_response["data"],
                file,
                indent=3,
                separators=(", ", ": ")
            )
    ### With the following .json file is not even needed, as we are not reading from it, but alas...
    print(f"Data for {ip_address}:\n")
    print(f"     Confidence score: {decoded_response["data"]["abuseConfidenceScore"]}")
    print(f"     Country of origin: {decoded_response["data"]["countryCode"]}")
    print(f"     If the IP is whitelisted: {decoded_response["data"]["isWhitelisted"]}")
    print("\n\n")

ABUSEIPDB_API_KEY = os.environ.get("ABUSEIPDB_API_KEY", "MY_ABUSEIPDB_API_KEY")
ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"
target_file = "../ip_list.txt"

querystring = {
    "ipAddress": ""
    ### Uncomment the following to get full info on IP
    # ,
    # "maxAgeInDays": 1,
    # "verbose": True
    ###
}
headers = {
    'Accept': 'application/json',
    'Key': ABUSEIPDB_API_KEY
}

if os.path.exists("results.json"):
    os.remove(path="results.json")

with open(target_file, "r") as target:
    ips = target.read().splitlines()
    for i in range(len(ips)):
        ### Comment the following if statement for the full json file
        if i == 3:
            with open("results.json", "a") as file:
                file.write("]}")
            break
        ###
        ip_address = ips[i]
        querystring["ipAddress"] = ip_address
        request()
        if i == len(range(len(ips) - 1)):
            with open("results.json", "a") as file:
                file.write("]}")