import sys

if len(sys.argv) < 2:
    print("Usage: python naive_parser_count.py <firewall.log>")
    sys.exit(1)

logfile = sys.argv[1]
blocked = 0
with open(logfile, "r") as f:
    for line in f:
        if "[BLOCK]" in line:
            blocked += 1
print("BLOCKED connections found:",blocked)


