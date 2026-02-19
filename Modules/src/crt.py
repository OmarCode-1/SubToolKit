from pycrtsh import Crtsh
import requests
from urllib.parse import urlparse
import time

class SubDomainCRT:
    def __init__(self, domain: str) -> None:
        self.cleint = Crtsh()
        self.domain = domain

    def crt_sh_subdomains(self) -> list:
        url = f"https://crt.sh/?q=%25.{self.domain}&output=json"
        headers = {"User-Agent": "Mozilla/5.0"}

        for attempt in range(3):
            try:
                r = requests.get(url, headers=headers, timeout=15)
                if r.status_code == 200:
                    data = r.json()
                    return list({entry["name_value"] for entry in data})
            except Exception as e:
                print("Retrying...", e)
                time.sleep(2)
        return []


    def hackertarget_subdomains(self) -> list:
        url = f"https://api.hackertarget.com/hostsearch/?q={self.domain}"
        response = requests.get(url)
        if response.status_code == 200:
            return [line.split(',')[0] for line in response.text.strip().split('\n')]
        return []

    def wayback_subdomains(self) -> list:
        url = "https://web.archive.org/cdx/search/cdx"

        params = {
            "url": f"*.{self.domain}/*",
            "output": "json",
            "fl": "original",
            "collapse": "urlkey"
        }

        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            response = requests.get(url, params=params, headers=headers, timeout=20)
            response.raise_for_status()

            data = response.json()

            if len(data) <= 1:
                return []

            subdomains = []

            for entry in data[1:]:
                original_url = entry[0]
                parsed = urlparse(original_url)
                subdomains.append(parsed.hostname.lower())

            return subdomains

        except requests.RequestException as e:
            print(f"[!] Wayback request failed: {e}")
            return []
        except Exception as e:
            print(f"[!] Parsing error: {e}")
            return []

