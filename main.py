from Modules.SubDomains import *
import sys
from colorama import Fore, Style, init



banner = r"""
{cyan}======================================================================
{yellow}   ____        _    _______    _ _    _ _ _ _ _   
{yellow}  / ___| _   _| |__|__  / |__| | | _(_) | (_) |_ 
{yellow}  \___ \| | | | '_ \ / /| '_ \ | |/ / | | | __|
{yellow}   ___) | |_| | |_) / /_| | | |   <| | | | |_ 
{yellow}  |____/ \__,_|_.__/____|_| |_|_|\_\_|_|_|\__|
{magenta}
               SubToolKit
               Coded by Omar Ibrahim
               CTF: 0x4FMR
{cyan}======================================================================
""".format(cyan=Fore.CYAN, yellow=Fore.YELLOW, magenta=Fore.MAGENTA)

if __name__ == '__main__':
    init(autoreset=True)
    print(banner)

    if len(sys.argv) != 2:
        print("Usage: python main.py domain.com")
        sys.exit(1)

    domain = sys.argv[1]

    print("Target domain: ", domain)
    print("Starting Recon: ", domain)
    SubToolKit(f"{domain}")
