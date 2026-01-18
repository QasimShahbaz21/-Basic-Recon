import requests
import re

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from crt.sh")
        return []

    subdomains = []
    try:
        data = response.json()
        for entry in data:
            name = entry.get("name_value", "")
            subdomains.extend(name.split("\n"))

    except Exception as e:
        print("Error parsing JSON:", e)
        return []

    return subdomains

def clean_subdomains(subdomains):
    cleaned = set()

    for sub in subdomains:
        sub = sub.strip()

        # Remove wildcard subdomains
        sub = sub.replace("*.", "")

        # Validate and avoid empty
        if sub and sub.count(".") >= 2:
            cleaned.add(sub)

    return sorted(cleaned)

if __name__ == "__main__":
    domain = input("Enter domain name: ")
    subdomains = get_subdomains(domain)
    cleaned_subdomains = clean_subdomains(subdomains)

    print("\nFound Subdomains:")
    for sub in cleaned_subdomains:
        print(sub)
