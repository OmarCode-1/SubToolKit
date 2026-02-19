# SubToolKit 🔎
Subdomain Reconnaissance Automation Tool

## 📌 Overview

SubToolKit is an automated reconnaissance tool designed to enumerate subdomains using multiple OSINT and active discovery techniques.  
It aggregates results from different sources, removes duplicates, identifies alive hosts, and tracks the origin of each discovered subdomain.

Built for security researchers, bug bounty hunters, and penetration testers.

---

## ⚙️ Features

- Subdomain brute force
- Certificate Transparency enumeration (crt.sh)
- HackerTarget integration
- Wayback Machine enumeration
- Google dorking automation
- Automatic deduplication
- Live host detection
- Source tracking for each subdomain
- Structured output directory

---

## 🛠 Enumeration Sources

The tool collects subdomains from:

- crt.sh
- HackerTarget
- Wayback Machine
- Google Dorking
- Custom brute-force wordlist

Each discovered subdomain is tagged with its source in `info.json`.

---

## 📂 Output Structure
Out/
└── domainname_timestamp/
    ├── alive.txt
    ├── findings.txt
    ├── subdomains.txt
    └── info.json


### File Description

- **subdomains.txt**  
  Contains unique (deduplicated) subdomains.

- **alive.txt**  
  Contains only reachable/live subdomains.

- **findings.txt**  
  Contains all discovered subdomains.

- **info.json**  
  JSON file containing:
  - subdomain
  - discovery source (crt, hackertarget, brute, wayback, google)
---

## 🚀 Usage

Basic usage:

```bash
python main.py example.com
```
```bash
Out/target.com_21-33_10/
```


## 👤 Author
Omar Ibrahim

Security Researcher | Junior Red Teamer
