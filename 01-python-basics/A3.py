
import sys
import re
from collections import Counter

if len(sys.argv) < 2:
    print("Usage: python regex_parser.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]
#apple\s*\d+

# Regex patterns
ip_pattern = re.compile(r'SRC=\s*(?:10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.(?:\d{1,3}\.)?\d{1,3})')



ips = []
blocked = 0
allowed = 0

with open(logfile, "r") as f:
    for line in f:
        if "[BLOCK]" in line:
            ip_match = ip_pattern.search(line)
            blocked += 1
            if ip_match:
                ips.append(ip_match.group())
        if "[ALLOW]" in line:
            ip_match = ip_pattern.search(line)
            allowed += 1
            if ip_match:
                
                ips.append(ip_match.group())

print("Ips attempts:")
for ip, count in Counter(ips).most_common():
    print(f"{ip}: {count} attempts")
print(allowed, "allowed")
print(blocked, "blocked")


