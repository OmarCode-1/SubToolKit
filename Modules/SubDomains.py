import json
import os
from datetime import datetime
from Modules.src.crt import *
from Modules.src.dorking import Dorking


class SubToolKit:
    def __init__(self, domain) -> None :
        self.domain = domain
        self.crtObj = SubDomainCRT(self.domain)
        self.reconName = f"{self.domain}_{datetime.now().strftime("%H-%M-%S")}"
        self.all_subdomains = []
        self.__init_files()
        self.start_recon()

    def __init_files(self):

        if not os.path.isdir("Out"):
            os.makedirs("Out", exist_ok=True)

        if os.access(os.path.dirname("Out") or '.', os.W_OK):
            os.makedirs(f"Out/{self.reconName}", exist_ok=True)

        self.subDomainsFile = open(f"Out/{self.reconName}/subdomains.txt", 'w')
        self.aliveFile = open(f"Out/{self.reconName}/alive.txt", 'w')
        self.techFile = open(f"Out/{self.reconName}/tech.txt", 'w')
        self.findingsFile = open(f"Out/{self.reconName}/findings.txt", 'w')
        self.infoFile = open(f"Out/{self.reconName}/info.json", 'w')

    def start_recon(self):
        self.crt_info = self.crtObj.crt_sh_subdomains()
        self.hacker_target_info = self.crtObj.hackertarget_subdomains()
        self.wayback_info = self.crtObj.wayback_subdomains()
        self.dork_info = Dorking(self.domain).google_dork_subdomains()
        self.passive_sub_domains = self.crt_info + self.hacker_target_info + self.wayback_info + self.dork_info

        print(self.passive_sub_domains)
        self.save_findings_subdomains()
        self.save_info_file()

    def save_findings_subdomains(self):
        for sub in self.passive_sub_domains:
            if sub[-1] == '\n':
                self.findingsFile.write(sub)
            else:
                self.findingsFile.write(f"{sub}\n")

    def save_info_file(self):
        dictOfInfo = {}
        for sub in self.passive_sub_domains:
            findings = []

            if sub in self.crt_info :
                findings.append("crt")

            if sub in self.wayback_info:
                findings.append("WayBack")

            if sub in self.hacker_target_info:
                findings.append("Hacker Target")

            if sub in self.dork_info:
                findings.append("Google Dorking")

            if sub[-1] == '\n':
                dictOfInfo[sub[:-1]] = findings
            else:
                dictOfInfo[sub] = findings

        json.dump(obj= dictOfInfo, fp=self.infoFile, indent=2)

    def clean_subdomains(self):
        cleaned = set()
        for subdomain in self.all_subdomains:
            sub = subdomain.lower()
            if sub.endswith(self.domain):
                cleaned.add(sub)
        return sorted(cleaned)
