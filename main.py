from Modules.SubDomains import *
import sys



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py domain.com")
        sys.exit(1)

    domain = sys.argv[1]

    print("Target domain: ", domain)
    print("Starting Recon: ", domain)
    program = SubToolKit(f"{domain}")
