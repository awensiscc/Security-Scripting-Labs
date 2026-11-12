# naive_parser.py
import sys

if len(sys.argv) < 2:
    print("Usage: python naive_parser.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

with open(logfile, "r") as f:
    for line in f:
        if "Failed password" in line:
            print(line.strip())
