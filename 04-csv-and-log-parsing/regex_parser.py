# regex_parser.py
import sys
import re
from collections import Counter

if len(sys.argv) < 2:
    print("Usage: python regex_parser.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

# Regex patterns
ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')   # IPv4
user_pattern = re.compile(r'Failed password for (\w+)')  # Extract username

ips = []
users = []

with open(logfile, "r") as f:
    for line in f:
        if "Failed password" in line:
            ip_match = ip_pattern.search(line)
            user_match = user_pattern.search(line)
            
            if ip_match:
                ips.append(ip_match.group())
            if user_match:
                users.append(user_match.group(1))

# Summaries
print("Top IPs with failed logins:")
for ip, count in Counter(ips).most_common():
    print(f"{ip}: {count} attempts")

print("\nTop usernames targeted:")
for user, count in Counter(users).most_common():
    print(f"{user}: {count} attempts")
