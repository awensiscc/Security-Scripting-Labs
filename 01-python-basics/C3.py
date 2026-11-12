import json
from collections import Counter

with open("vulnerabilities.json") as emp:

    data = json.load(emp)
    list_host = {}
    for i in range(len(data['findings'])):
        host = (data['findings'][i]['host'])
        vulnerability = (data['findings'][i]['vulnerability'])
        list_host[host] = vulnerability

print(list_host)
# for vulnebs, count in Counter(list_host).most_common():
#     print(f"{vulnebs}: {count} attempts")

#2 web 01
#1 web 02
#1 db 01
#1 mail 01