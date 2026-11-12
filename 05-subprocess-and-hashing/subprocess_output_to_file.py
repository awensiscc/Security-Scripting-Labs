import subprocess
import sys

with open("output.txt", "w") as f:
    if sys.platform == "win32": # Windows
        subprocess.run(["cmd", "/c", "dir"], stdout=f)
    else:
        subprocess.run(["ls", "-la"], stdout=f) # Unix-like systems


