import subprocess
ips = ["64.13.134.52","45.33.32.156"]

for ip in ips:
    result = subprocess.run(["ping", "-n", "1", ip], capture_output=True)
    if result.returncode == 0:
        print(f"{ip} is alive")
    else:
        print(f"{ip} no response")


