from pycrtsh import Crtsh
import requests
from urllib.parse import urlparse

class SubDomainCRT:
    def __init__(self, domain: str) -> None:
        self.cleint = Crtsh()
        self.domain = domain

    def crt_sh_subdomains(self) -> list:
        self.ctrs = self.cleint.search(f'{self.domain}')
        subdomains = [sub["name"] for sub in self.ctrs]
        return subdomains

    def hackertarget_subdomains(self) -> list:
        url = f"https://api.hackertarget.com/hostsearch/?q={self.domain}"
        response = requests.get(url)
        if response.status_code == 200:
            return [line.split(',')[0] for line in response.text.strip().split('\n')]
        return []

    def wayback_subdomains(self) -> list:
        url = "http://web.archive.org/cdx/search/cdx"

        params = {
            "url": f"*.{self.domain}/*",
            "output": "json",
            "fl": "original",
            "collapse": "urlkey"
        }

        try:
            response = requests.get(url, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()

            subdomains = []

            for entry in data[1:]:
                original_url = entry[0]
                parsed = urlparse(original_url)

                hostname = parsed.hostname
                subdomains.append(hostname.lower())

            return subdomains

        except requests.RequestException as e:
            print(f"[!] Wayback request failed: {e}")
            return []
        except Exception as e:
            print(f"[!] Parsing error: {e}")
            return []
