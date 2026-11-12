# basic TCP port sweep
import socket

ips = ["64.13.134.52","45.33.32.156"]  # change to your router or another local host
ports = [22, 80, 443, 2376]

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    for ip in ips:
        try:
            s.connect((ip, port))
            print(f"Port {port} open on {ip}")
        except:
            print(f"Port {port} closed on {ip}")
        finally:
            s.close()


