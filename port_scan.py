import subprocess

def port_scan(target, ports, profile):
    command = ["nmap"]

    # Add scan profile
    if profile == "default":
        pass
    elif profile == "script":
        command.append("-sC")
    elif profile == "version":
        command.append("-sV")
    elif profile == "aggressive":
        command.append("-A")

    # Add ports if provided
    if ports:
        command.extend(["-p", ports])

    command.append(target)

    print("\n[+] Running command:", " ".join(command), "\n")

    try:
        subprocess.run(command)
    except Exception as e:
        print("[!] Error running nmap:", e)

if __name__ == "__main__":
    target = input("Enter domain or IP: ")

    print("\nPort Options:")
    print("1. Default ports")
    print("2. Custom ports (e.g. 22,80,443 or 1-1000)")
    port_choice = input("Choose (1/2): ")

    ports = None
    if port_choice == "2":
        ports = input("Enter ports: ")

    print("\nScan Profiles:")
    print("1. Default scan")
    print("2. Script scan (-sC)")
    print("3. Version scan (-sV)")
    print("4. Aggressive scan (-A)")
    profile_choice = input("Choose (1/2/3/4): ")

    profile_map = {
        "1": "default",
        "2": "script",
        "3": "version",
        "4": "aggressive"
    }

    profile = profile_map.get(profile_choice, "default")

    port_scan(target, ports, profile)
