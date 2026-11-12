import json
with open("vulnerabilities.json") as emp:

    data = json.load(emp)

    for i in range(len(data['findings'])):
     print("host:", data['findings'][i]['host'])
     print("vulnerability:", data['findings'][i]['vulnerability'])
     print("severity:", data['findings'][i]['severity'])
     print("cvss_score:", data['findings'][i]['cvss_score'])
     print("\n")