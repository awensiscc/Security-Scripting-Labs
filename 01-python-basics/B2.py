import csv

brutef_attack = 0
sqli_attack = 0
ports_attack = 0
ddos_attack = 0
malw_attack = 0
with open("security_incidents.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["attack_type"] == "Brute Force":
            brutef_attack += 1
        elif row["attack_type"] == "SQL Injection":
            sqli_attack += 1
        elif row["attack_type"] == "Port Scan":
            ports_attack += 1
        elif row["attack_type"] == "DDoS":
            ddos_attack += 1
        elif row["attack_type"] == "Malware":
            malw_attack += 1

print("Brute Force attacks performed:", brutef_attack)
print("SQL Injection attacks performed:", sqli_attack)
print("Port Scan attacks performed:", ports_attack)
print("DDoS attacks performed:", ddos_attack)
print("Malware attacks performed:",malw_attack)

print("Total amount of attacks performed",brutef_attack+sqli_attack+ports_attack+ddos_attack+malw_attack)


