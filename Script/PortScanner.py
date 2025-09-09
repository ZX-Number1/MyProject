import socket

target = "127.0.0.1"
#這裡可以更變目標主機

common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 3389]

print(f"Scanning {target}...\n")

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((target ,port))
        if result ==0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSE")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
    finally:
        sock.close()