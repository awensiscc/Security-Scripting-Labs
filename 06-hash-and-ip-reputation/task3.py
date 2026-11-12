import os
import requests
import json


def request():
    response = requests.get(
        VIRUSTOTAL_URL,
        headers=headers
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

VT_API_KEY = os.environ.get("VT_API_KEY", "MY_VT_API_KEY")
VIRUSTOTAL_URL = ""
target_file = "../suspect_hashes.txt"

headers = {
    "accept": "application/json",
    "x-apikey": VT_API_KEY
}

if os.path.exists("results.json"):
    os.remove(path="results.json")

with open(target_file, "r") as target:
    hashes = target.read().splitlines()
    for i in range(len(hashes)):
        VIRUSTOTAL_URL = f"https://www.virustotal.com/api/v3/files/{hashes[i]}"
        request()
        if i == len(range(len(hashes) - 1)):
            with open("results.json", "a") as file:
                file.write("]}")

vendors_analysis = {}
category_list = ["malicious", "suspicious"]

with open("results.json", "r") as file:
    data = json.load(file)
    for o in range(len(data["data"])):
        for i in range(len(data["data"][1]["attributes"]["last_analysis_results"])):
            for key, value in data["data"][1]["attributes"]["last_analysis_results"].items():
                if value["category"] in category_list:
                    vendors_analysis[value["engine_name"]] = value["category"]
        print("\n")
        print(f"Hash ID: {data["data"][o]["id"]}")
        print("Vendor engines that detected the malware and what they have labelled the malware as: \n")
        for key, value in vendors_analysis.items():
            print(f"     {key} : {value}")