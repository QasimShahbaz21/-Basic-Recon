import socket

def grab_banner(ip, port):
    try:
        # Create TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)

        # Connect to target
        s.connect((ip, port))

        # Send a simple request (works for many services)
        s.sendall(b"Hello\r\n")

        # Receive banner
        banner = s.recv(1024)

        if banner:
            print("\n[+] Banner received:")
            print(banner.decode(errors="ignore"))
        else:
            print("\n[-] No banner received")

        s.close()

    except socket.timeout:
        print("\n[!] Connection timed out")
    except socket.error as e:
        print(f"\n[!] Socket error: {e}")

if __name__ == "__main__":
    ip = input("Enter target IP: ")
    port = int(input("Enter target port: "))

    grab_banner(ip, port)
