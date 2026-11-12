# naive_parser_count.py
import sys

if len(sys.argv) < 2:
    print("Usage: python naive_parser_count.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]
fail_count = 0

with open(logfile, "r") as f:
    for line in f:
        if "Failed password" in line:
            print(line.strip())   # show matching lines
            fail_count += 1 # count the number of failed password entries

print(f"\nTotal failed login attempts: {fail_count}")


