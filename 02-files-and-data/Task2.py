import socket

# Write a Python script that performs a TCP scan your local machine for the following ports
# and prints out whether the ports are open or closed:
# 80, 8080, 3306, 22,443
# scans a target IP and list of ports
def port_scanner(target, ports):

    try:
        target_ip = socket.gethostbyname(target)
        print(f"Resolved {target} to {target_ip}\n")
    except socket.gaierror:
        print(f"Error: Cannot resolve hostname {target}")
        return
    
    open_ports = []
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
            open_ports.append(port)
        else:
            print(f"[-] Port {port}: CLOSED")
        
        sock.close()
    
    print(f"\n{'='*60}")
    print(f"Scan completed. {len(open_ports)} open port(s) found")
    print(f"{'='*60}\n")
    
    return open_ports

if __name__ == "__main__":
    # Example usage
    common_ports = [ 80, 8080, 3306, 22,443]
    port_scanner('localhost', common_ports)