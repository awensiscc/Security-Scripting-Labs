import csv

incidents_amount = 0
with open("security_incidents.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        incidents_amount += 1
        print(row)
print("Total amount of incidents:", incidents_amount)


