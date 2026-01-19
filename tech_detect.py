import requests
import re
from bs4 import BeautifulSoup

def tech_detect(url):
    try:
        response = requests.get(url, timeout=10)

        print("\n[+] HTTP Headers Analysis")

        # Server header
        server = response.headers.get("Server")
        if server:
            print("Server:", server)

        # X-Powered-By header
        powered_by = response.headers.get("X-Powered-By")
        if powered_by:
            print("X-Powered-By:", powered_by)

        # Cookies
        cookies = response.headers.get("Set-Cookie")
        if cookies:
            print("Cookies:", cookies)

        print("\n[+] HTML Analysis")

        soup = BeautifulSoup(response.text, "html.parser")

        # Meta generator tag
        generator = soup.find("meta", attrs={"name": re.compile("generator", re.I)})
        if generator and generator.get("content"):
            print("Generator:", generator["content"])

        # Basic CMS detection
        html = response.text.lower()
        if "wp-content" in html:
            print("Detected CMS: WordPress")
        if "drupal" in html:
            print("Detected CMS: Drupal")
        if "joomla" in html:
            print("Detected CMS: Joomla")

    except requests.exceptions.RequestException as e:
        print("[!] Request Error:", e)

if __name__ == "__main__":
    url = input("Enter target URL (http/https): ")
    tech_detect(url)
