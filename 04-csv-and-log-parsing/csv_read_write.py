import csv

# --- Writing to a CSV file (list-based) ---
# with open("security_incidents.csv", "w", newline="") as f: # note: newline="" stops blank lines being inserted
#     writer = csv.writer(f)
#
#     # Write header row
#     writer.writerow(["timestamp", "host", "user", "ip", "event"])
#
#     # Write some sample rows
#     writer.writerow(["2025-01-01 10:05", "server1", "root", "203.0.113.55", "Failed password"])
#     writer.writerow(["2025-01-01 10:06", "server1", "student", "192.168.1.15", "Accepted password"])
#
# print("logs_simple.csv created")

# --- Re
# ading from a CSV file (list-based) ---
incidents_amount = 0
with open("security_incidents.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        incidents_amount += 1

print("Total amount of incidents:", incidents_amount)


