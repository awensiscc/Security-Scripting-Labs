import json
with open("vulnerabilities.json") as emp:

    data = json.load(emp)
    vuln_count = 0
    for i in range(len(data['findings'])):
     print(data['findings'][i])
     vuln_count += 1
print("Found:",vuln_count,"vulnerabilities")
