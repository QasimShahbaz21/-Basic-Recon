import whois

def main():
    domain = input("Enter domain (e.g., example.com): ")

    try:
        w = whois.whois(domain)

        print("\n--- WHOIS Information ---")
        print("Registrar:", w.registrar)
        print("Creation Date:", w.creation_date)
        print("Expiry Date:", w.expiration_date)
        print("Name Servers:", w.name_servers)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
