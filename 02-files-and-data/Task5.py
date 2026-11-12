import socket


ips = ["64.13.134.52","45.33.32.156"]


for ip in ips:
    data = socket.gethostbyaddr(ip)
    print(data)
