import sys
import requests
import threading
import time

searchlist = []
listfilepath = ""

def findDomainInfo():
    while True:
        try:
            name = searchlist[0]
            searchlist.remove(name)
            request = requests.get("https://unstoppabledomains.com/api/search?q=" + name.replace("'", "")).json()["exact"]
            if(".crypto" in request[1]["productCode"]):
                request[0], request[1] = request[1], request[0]

            # CRYPTO
            # Protected
            if(("-C" in sys.argv or "-c" in sys.argv or "--crypto" in sys.argv) or ("-Z" not in sys.argv and "-z" not in sys.argv and "--zil" not in sys.argv)):
                if("-P" in sys.argv or "-p" in sys.argv or "--all" in sys.argv):
                    if(getProtectedStatus(request[0]["status"]) == "Protected"):
                        print("Protected:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Not Protected
                elif("-NP" in sys.argv or "-np" in sys.argv or "--all" in sys.argv):
                    if(getProtectedStatus(request[0]["status"]) == "Not Protected"):
                        print("Not Protected:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Resvered
                if("-RS" in sys.argv or "-rs" in sys.argv or "--all" in sys.argv):
                    if(getReservedStatus(request[0]["status"]) == "Reserved"):
                        print("Reserved:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Not Reserved
                elif("-NRS" in sys.argv or "-nrs" in sys.argv or "--all" in sys.argv):
                    if(getReservedStatus(request[0]["status"]) == "Not Reserved"):
                        print("Not Reserved:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Premium
                if("-PR" in sys.argv or "-pr" in sys.argv or "--all" in sys.argv):
                    if(getPremiumStatus(request[0]["status"]) == True):
                        print("Premium:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Not Premium
                elif("-NPR" in sys.argv or "-npr" in sys.argv or "--all" in sys.argv):
                    if(getPremiumStatus(request[0]["status"]) == False):
                        print("Premium:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Registered
                if("-R" in sys.argv or "-r" in sys.argv or "--all" in sys.argv):
                    if(getRegisteredStatus(request[0]["status"]) == "Reserved"):
                        print("Registered:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Not Registered
                elif("-NR" in sys.argv or "-nr" in sys.argv or "--all" in sys.argv):
                    if(getRegisteredStatus(request[0]["status"]) == "Not Reserved"):
                        print("Not Registered:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Available
                if("-A" in sys.argv or "-a" in sys.argv or "--all" in sys.argv):
                    if(isAvailable(request[0]["availability"]) == True):
                        print("Avalaible:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # Not Available
                elif("-NA" in sys.argv or "-na" in sys.argv or "--all" in sys.argv):
                    if(isAvailable(request[0]["availability"]) == False):
                        print("Not Avalaible:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))
                # For Sale
                if("-FS" in sys.argv or "-fs" in sys.argv or "--all" in sys.argv):
                    if(isForSale(name) == True):
                        print("For Sale:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                elif("-NFS" in sys.argv or "-nfs" in sys.argv or "--all" in sys.argv):
                    if(isForSale(name) == False):
                        print("Not For Sale:", request[0]["productCode"].ljust(len(request[0]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[0]["price"]) / 100))

            # ZIL
            # Protected
            if(("-Z" in sys.argv or "-z" in sys.argv or "--zil" in sys.argv) or ("-C" not in sys.argv and "-c" not in sys.argv and "--crypto" not in sys.argv)):
                if("-P" in sys.argv or "-p" in sys.argv or "--all" in sys.argv):
                    if(getProtectedStatus(request[1]["status"]) == "Protected"):
                        print("Protected:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Not Protected
                elif("-NP" in sys.argv or "-np" in sys.argv or "--all" in sys.argv):
                    if(getProtectedStatus(request[1]["status"]) == "Not Protected"):
                        print("Not Protected:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Premium
                if("-PR" in sys.argv or "-pr" in sys.argv or "--all" in sys.argv):
                    if(getPremiumStatus(request[1]["status"]) == True):
                        print("Premium:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Not Premium
                elif("-NPR" in sys.argv or "-npr" in sys.argv or "--all" in sys.argv):
                    if(getPremiumStatus(request[1]["status"]) == False):
                        print("Premium:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Registered
                if("-R" in sys.argv or "-r" in sys.argv or "--all" in sys.argv):
                    if(getRegisteredStatus(request[1]["status"]) == "Registered"):
                        print("Registered:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Not Registered
                elif("-NR" in sys.argv or "-nr" in sys.argv or "--all" in sys.argv):
                    if(getRegisteredStatus(request[1]["status"]) == "Not Registered"):
                        print("Not Registered:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Reserved
                if("-RS" in sys.argv or "-rs" in sys.argv or "--all" in sys.argv):
                    if(getReservedStatus(request[1]["status"]) == "Reserved"):
                        print("Reserved:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Not Reserved
                elif("-NRS" in sys.argv or "-nrs" in sys.argv or "--all" in sys.argv):
                    if(getReservedStatus(request[1]["status"]) == "Not Reserved"):
                        print("Not Reserved:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Available
                if("-A" in sys.argv or "-a" in sys.argv or "--all" in sys.argv):
                    if(isAvailable(request[1]["availability"]) == True):
                        print("Avalaible:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # Not Available
                elif("-NA" in sys.argv or "-na" in sys.argv or "--all" in sys.argv):
                    if(isAvailable(request[1]["availability"]) == False):
                        print("Not Avalaible:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                # For Sale
                if("-FS" in sys.argv or "-fs" in sys.argv or "--all" in sys.argv):
                    if(isForSale(name) == True):
                        print("For Sale:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
                elif("-NFS" in sys.argv or "-nfs" in sys.argv or "--all" in sys.argv):
                    if(isForSale(name) == False):
                        print("Not For Sale:", request[1]["productCode"].ljust(len(request[1]["productCode"]) + 5).ljust(25), end="")
                        print("Price:", "${:,.2f}".format(int(request[1]["price"]) / 100))
        except:
            break

def getProtectedStatus(status):
    if(status == "protected"):
        return "Protected"
    else:
        return "Not Protected"
    
def getRegisteredStatus(status):    
    if(status == "registered"):
        return "Registered"
    else:
        return "Not Registered"

def getReservedStatus(status):    
    if(status == "reserved"):
        return "Reserved"
    else:
        return "Not Reserved"
    
def getPremiumStatus(status):
    if(status == "reserved" or status == "protected"):
        return True
    else:
        return False
    
def isAvailable(availability):
    if(availability == True):
        return True
    else:
        return False       

def isForSale(name):
    try:
        forsale = requests.get("https://unstoppabledomains.com/api/record/zil?domain=" + name + ".crypto").json()["whois"]["for_sale"]
        if(forsale == True):
            return True
        else:
            return False
    except KeyError:
        return False

def threadedPrint(object):
    screen_lock.acquire()
    print(object)
    screen_lock.release()


arguments = ["-p", "-a", "-c", "-r", "-z", "-rs", "-pr", "-np", "-na", "-fs", "-fs", "-nr", "-nfs", "-nrs", "-npr", "--all", "--crypto", "--zil"]

listfilepath = sys.argv[1]
sys.argv.remove(str(sys.argv[0]))
sys.argv.remove(str(sys.argv[0]))

if(len(sys.argv) == 0):
    print("No arguments given")
    exit()

for arg in sys.argv:
    if(arg.lower() not in arguments):
        print("ERROR:", arg, "is not a valid argument")
        print('Usage: python "C:/example/unstoppabledomains.py" "<filelist_path>" [options...]')
        print("\nOptions")
        print("-a or -A,".ljust(20), "Available Domains")
        print("--all or --ALL,".ljust(20), "No Filter")
        print("-c or --crypto".ljust(20), ".crypto Domains Only")
        print("-fs or -FS,".ljust(20), "For Sale Domains")
        print("-na or -NA,".ljust(20), "Not Available Domains")
        print("-nfs or -NFS,".ljust(20), "Not For Sale Domains")
        print("-np or -NP,".ljust(20), "Non-Protected Domains")
        print("-npr or -NPR,".ljust(20), "Non-Premium Domains (Not Reserved and Non-Protected Domains)")
        print("-nr, or -NR,".ljust(20), "Non-registered Domains")
        print("-nrs, or -NRS,".ljust(20), "Non-Reserved Domains")
        print("-p or -P,".ljust(20), "Protected Domains")
        print("-pr or -PR,".ljust(20), "Premium Domains (Reserved or Protected Domains)")
        print("-r or -R,".ljust(20), "Registered Domains")
        print("-rs or -RS,".ljust(20), "Reserved Domains")
        print("-z or --zil".ljust(20), ".zil Domains Only")
        exit()

with open(listfilepath.replace("/", "//")) as file:
    searchlist = file.readlines()
    
thread = threading.Thread(target=findDomainInfo).start()
thread = threading.Thread(target=findDomainInfo).start()
thread = threading.Thread(target=findDomainInfo).start()
thread = threading.Thread(target=findDomainInfo).start()
thread = threading.Thread(target=findDomainInfo).start()

