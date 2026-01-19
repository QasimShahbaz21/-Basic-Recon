import socket

def grab_banner(ip, port):
    try:
        # Create TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)

        # Connect to target
        sock.connect((ip, port))

        # Send basic request
        request = b"HEAD / HTTP/1.0\r\n\r\n"
        sock.sendall(request)

        # Receive banner
        banner = sock.recv(4096)

        if banner:
            clean_banner = banner.decode("utf-8", errors="ignore").strip()
            print("\n[+] Banner received:\n")
            print(clean_banner)
        else:
            print("\n[-] No banner received")

        sock.close()

    except socket.timeout:
        print("\n[!] Connection timed out")
    except ConnectionRefusedError:
        print("\n[!] Connection refused")
    except socket.gaierror:
        print("\n[!] Invalid IP or hostname")
    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    ip = input("Enter target IP or domain: ")
    try:
        port = int(input("Enter target port: "))
        grab_banner(ip, port)
    except ValueError:
        print("[!] Port must be a number")
