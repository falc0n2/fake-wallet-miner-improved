import time
import random
import string
import os
from colorama import init, Fore
init(convert=True)

print(Fore.MAGENTA + "Welcome to the Fake Wallet Miner")
time.sleep(1.8)

os.system("cls")
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
print(Fore.GREEN + "Wallet Found!")
time.sleep(0.2)
print(Fore.BLUE + "Checking if everything is okay...")
time.sleep(3)

def id_gen(size=40, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))

tries = 0

while True:
    if tries > random.randint(100000000000000, 100000000000000000):  # chance to get fake btc
        print(Fore.CYAN + "[+]" + Fore.RED + " bc3" + id_gen() + Fore.GREEN +" |  Valid  |  " + str(round(random.uniform(0,2), 4)), "BTC")
        print(Fore.GREEN + "Withdrawing to your address...")
        time.sleep(7.5)
        tries = 0
        print(Fore.GREEN + "Done!")
        time.sleep(1)
    else:
        print(Fore.MAGENTA +"[-]"+ Fore.RED + " bc1" + id_gen() + Fore.CYAN +" | Invalid |  " + "0.0000 BTC")
        print(Fore.MAGENTA +"[-]"+ Fore.RED + " bc2" + id_gen() + Fore.CYAN +" | Invalid |  4" + "0.0000 BTC")
        print(Fore.MAGENTA +"[-]"+ Fore.RED + " bx3" + id_gen() + Fore.CYAN +" | Invalid |  " + "0.0000 BTC")
        print(Fore.MAGENTA +"[-]"+ Fore.RED + " dc2" + id_gen() + Fore.CYAN +" | Invalid |  " + "0.0000 BTC")
        tries += 1
