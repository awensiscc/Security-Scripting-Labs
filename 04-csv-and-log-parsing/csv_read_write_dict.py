import csv

# Read CSV log file
with open("csv_log.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["event"] == "Failed password":
            print(f"User: {row['user']} | IP: {row['ip']}")

