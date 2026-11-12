import csv
from collections import Counter


brutef_attack = 0
sqli_attack = 0
ports_attack = 0
ddos_attack = 0
malw_attack = 0
attacks = {}

with open("security_incidents.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["attack_type"] == "Brute Force":
            brutef_attack += 1
            attacks["Brute Force"] = brutef_attack
        elif row["attack_type"] == "SQL Injection":
            sqli_attack += 1
            attacks["SQL Injection"] = sqli_attack
        elif row["attack_type"] == "Port Scan":
            ports_attack += 1
            attacks["Port Scan"] = ports_attack
        elif row["attack_type"] == "DDoS":
            ddos_attack += 1
            attacks["DDoS"] = ddos_attack
        elif row["attack_type"] == "Malware":
            malw_attack += 1
            attacks["Malware"] = malw_attack



most_common = []
attacks_amount = []
for attacks, count in Counter(attacks).most_common(1):
    most_common = attacks
    attacks_amount = count

source_ip_list = []
with open("security_incidents.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["attack_type"] == most_common:
            source_ip = row["source_ip"]
            source_ip_list.append(source_ip)

print(f"IPs from which {attacks_amount} {most_common} attacks were launched:")
for source_ips, count in Counter(source_ip_list).most_common():
    print(f"{source_ips}: {count} attempts")
