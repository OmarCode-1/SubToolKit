import json
import os
from datetime import datetime
from Modules.src.crt import *
from Modules.src.active_recon import *
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
        self.findingsFile = open(f"Out/{self.reconName}/findings.txt", 'w')
        self.infoFile = open(f"Out/{self.reconName}/info.json", 'w')

    def start_recon(self):
        self.crt_info = self.crtObj.crt_sh_subdomains()
        self.hacker_target_info = self.crtObj.hackertarget_subdomains()
        self.wayback_info = self.crtObj.wayback_subdomains()
        self.dork_info = Dorking(self.domain).google_dork_subdomains()

        self.passive_sub_domains = self.crt_info + self.hacker_target_info + self.wayback_info + self.dork_info
        # self.active_sub_domains = ActiveRecon(self.domain).active_subdomain_enum()

        self.all_subdomains = self.passive_sub_domains + []

        self.save_findings_subdomains()
        self.save_subdomains_file()
        self.save_info_file()

    def save_findings_subdomains(self):
        for sub in self.all_subdomains:
            if sub[-1] == '\n':
                self.findingsFile.write(sub)
            else:
                self.findingsFile.write(f"{sub}\n")
        self.findingsFile.close()

    def save_subdomains_file(self):
        unique_subdomains = []
        reading_finding_file = open(f"Out/{self.reconName}/findings.txt", 'r')

        for sub in reading_finding_file.readlines():
            if sub not in unique_subdomains and sub[:-1].endswith(self.domain):
                self.subDomainsFile.write(sub)
        self.subDomainsFile.close()



    def save_info_file(self):
        dictOfInfo = {}
        reading_subdomains_file = open(f"Out/{self.reconName}/subdomains.txt", 'r')
        for sub in reading_subdomains_file.readlines():
            # findings = []
            #
            # if sub in ''.join(self.crt_info) :
            #     findings.append("crt")
            #
            # if sub in ''.join(self.wayback_info):
            #     findings.append("WayBack")
            #
            # if sub in ''.join(self.hacker_target_info):
            #     findings.append("Hacker Target")
            #
            # if sub in ''.join(self.dork_info):
            #     findings.append("Google Dorking")

            # if sub in ''.join(self.active_sub_domains):
            #     findings.append("Active Recon")

            dictOfInfo[sub] = 0

        json.dump(obj= dictOfInfo, fp=self.infoFile, indent=2)

    def clean_subdomains(self):
        cleaned = set()
        for subdomain in self.all_subdomains:
            sub = subdomain.lower()
            if sub.endswith(self.domain):
                cleaned.add(sub)
        return sorted(cleaned)
