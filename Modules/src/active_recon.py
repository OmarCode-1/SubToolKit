import dns.resolver
import concurrent.futures

class ActiveRecon:
    def __init__(self, domain:str):
        self.domain = domain

    def resolve_subdomain(self, subdomain):
        try:
            answers = dns.resolver.resolve(subdomain, 'A')
            for rdata in answers:
                return subdomain, rdata.to_text()
        except:
            return None

    def active_subdomain_enum(self, threads=50):
        found = []

        with open(r"Modules/req/subdomains2.txt", "r") as f:
            words = [line.strip() for line in f]

        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            for word in words:
                subdomain = f"{word}.{self.domain}"
                futures.append(executor.submit(self.resolve_subdomain, subdomain))

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    sub, ip = result
                    found.append(sub)

        return found
