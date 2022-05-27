import time
import random
import string
import os
import socket
import subprocess, requests
from colorama import init, Fore
init(convert=True)

print(f"""

  ______      _  ________  __          __     _      _      ______ _______   __  __ _____ _   _ ______ _____  
 |  ____/\   | |/ /  ____| \ \        / /\   | |    | |    |  ____|__   __| |  \/  |_   _| \ | |  ____|  __ \ 
 | |__ /  \  | ' /| |__     \ \  /\  / /  \  | |    | |    | |__     | |    | \  / | | | |  \| | |__  | |__) |
 |  __/ /\ \ |  < |  __|     \ \/  \/ / /\ \ | |    | |    |  __|    | |    | |\/| | | | | . ` |  __| |  _  / 
 | | / ____ \| . \| |____     \  /\  / ____ \| |____| |____| |____   | |    | |  | |_| |_| |\  | |____| | \ \ 
 |_|/_/    \_\_|\_\______|     \/  \/_/    \_\______|______|______|  |_|    |_|  |_|_____|_| \_|______|_|  \_\


you can get wallet text from this website, just replace this entire line with the text: https://patorjk.com/software/taag/#p=display&f=BIG&t=FAKE%20WALLET%20MINER

""")
time.sleep(1.8)

os.system("cls")

hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
site = requests.get("https://pastebin.com/raw/yourpastebinlinkhere")

try:
    if hardwareid in site.text:
        pass
    else:
        print("You are not Whitelisted!")
        print(f"Your HWID is {hardwareid}")
        input()
        exit()
except:
    print("Failed to connect to database")
    input()
    exit()
    
# Start of Internal computer IP check (to disable just put the symbol "#" at the start of the 14 lines below and they'll be commented out.)

IPAddr = socket.gethostbyname(socket.gethostname())
site = requests.get("https://pastebin.com/raw/yourpastebinlinkhere")

try:
    if IPAddr in site.text:
        pass
    else:
        print("Your Computer is not whitelisted on the IP database.")
        print(f"Your computer IP address is: " + IPAddr)
        input()
        exit()
except:
    print("Failed to connect to database")
    input()
    exit()

# End of Internal Computer IP Check

LicenseKey = input(Fore.RED + "Input License Key >" + Fore.RESET + " ")
if LicenseKey == "fSNdnw24ajTud9NvgaL7vGuHy4ksKnSZ3LbZaeMwPkXj8gh":
    print(Fore.BLUE + "One second while I check if the key is valid on our servers!")
    time.sleep(5)
    print(Fore.GREEN + "The key is valid!")
    time.sleep(2.5)
else:
    print(Fore.BLUE + "One second while I check if the key is valid on our servers!")
    time.sleep(5)
    print(Fore.RED + "The key is invalid!")
    print("Exiting...")
    time.sleep(2)
    exit()

os.system("cls")
Wallet = input(Fore.RED + "Your BTC Wallet address >" + Fore.RESET + " ")
print(Fore.CYAN + "Checking if Wallet exists... ")
time.sleep(1)
walletCheck = requests.get("https://blockchain.info/q/addressbalance/ " + Wallet)
if walletCheck.status_code == 200:
    print(Fore.GREEN + "Wallet Found!")
else:
    print(Fore.RED + "Wallet not found!")
    time.sleep(3.2)
    exit()
time.sleep(0.2)
print(Fore.BLUE + "Checking if everything is okay...")
time.sleep(3)

def file_len():
    with open("proxies.txt") as f:
        for i, _ in enumerate(f):
            pass
    return i

print(f"""
[1] Use Proxies
[2] Don't use Proxies
""")

proxies = input("Do you want to use Proxies?: ")
if proxies == "1":
    print(Fore.GREEN + "Imported " + str(file_len()) + " Proxies")
else:
    print("Not using Proxies")
time.sleep(3)

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

tries = 0

while True:
    if tries > random.randint(100000000000, 100000000000000):  # chance to get fake btc
        print(Fore.CYAN + "[+]" + Fore.RED + " bc3" + id_gen() + Fore.GREEN +" |  Valid  |  " + str(round(random.uniform(0,2), 4)), "BTC")
        print(Fore.GREEN + "Withdrawing to your address...")
        time.sleep(7.5)
        tries = 0
        print(Fore.GREEN + "Done!")
        time.sleep(1)
    else:
        print(Fore.MAGENTA +"[-]"+ Fore.RED + " bc1" + id_gen() + Fore.CYAN +" | Invalid |  " + "0.0000 BTC")
        print(Fore.MAGENTA +"[-]"+ Fore.RED + " bc2" + id_gen() + Fore.CYAN +" | Invalid |  " + "0.0000 BTC")
        print(Fore.MAGENTA +"[-]"+ Fore.RED + " bx3" + id_gen() + Fore.CYAN +" | Invalid |  " + "0.0000 BTC")
        print(Fore.MAGENTA +"[-]"+ Fore.RED + " dc2" + id_gen() + Fore.CYAN +" | Invalid |  " + "0.0000 BTC")
        tries += 1
