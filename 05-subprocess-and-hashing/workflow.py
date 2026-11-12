# pipeline_hash_to_vt.py
# Purpose: Chain the output of file_hash.py into vt_file_query.py using subprocess.

import subprocess
import sys

# 1) Run the hasher script and capture its stdout}
hash_proc = subprocess.run(
    [sys.executable, "file_hash.py"],
    capture_output=True,
    text=True
)

file_hash = hash_proc.stdout.strip()

print(f"[*] Hash from hasher: {file_hash}")

# 2) Call the VT script with that hash as an argument   :contentReference[oaicite:3]{index=3}
vt_proc = subprocess.run(
    [sys.executable, "vt_file_query.py", file_hash],
    text=True
)



