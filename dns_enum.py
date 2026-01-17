import dns.resolver

def dns_enumeration(domain):
    try:
        # A Record
        print("\n[+] A Records:")
        for ip in dns.resolver.resolve(domain, 'A'):
            print(ip.to_text())

        # MX Record
        print("\n[+] MX Records:")
        for mx in dns.resolver.resolve(domain, 'MX'):
            print(mx.exchange.to_text(), "Priority:", mx.preference)

        # NS Record
        print("\n[+] NS Records:")
        for ns in dns.resolver.resolve(domain, 'NS'):
            print(ns.to_text())

    except dns.resolver.NoAnswer:
        print("[-] No DNS records found")
    except dns.resolver.NXDOMAIN:
        print("[-] Domain does not exist")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    domain = input("Enter domain name: ")
    dns_enumeration(domain)
