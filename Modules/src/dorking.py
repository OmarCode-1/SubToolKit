import requests
import re
from urllib.parse import quote
class Dorking:
    def __init__(self, domain: str):
        self.domain = domain

    def google_dork_subdomains(self) -> list:
        query = quote(f"site:*.{self.domain} -www")
        url = f"https://www.google.com/search?q={query}&num=100"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-US,en;q=0.9"
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)

            if "Our systems have detected unusual traffic" in response.text:
                print("[!] Google blocked the request.")
                return []

            pattern = rf'([a-zA-Z0-9-]+\.)+{re.escape(self.domain)}'
            matches = re.findall(pattern, response.text)

            return matches

        except requests.RequestException as e:
            print(f"[!] Request failed: {e}")
            return []
