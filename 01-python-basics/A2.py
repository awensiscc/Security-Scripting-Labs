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


ips = []


with open(logfile, "r") as f:
    for line in f:
        if "[BLOCK]" in line:
            ip_match = ip_pattern.search(line)
            if ip_match:
                ips.append(ip_match.group())


# Summaries
print("IPS in blocked attempts:")
for ip, count in Counter(ips).most_common():
    print(f"{ip}: {count} attempts")

