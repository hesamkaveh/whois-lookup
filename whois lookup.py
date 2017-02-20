'''
developed by HesamKaveh
hk.hesam.hk@gmail.com
version 0.1
'''
import pythonwhois  # i'm using this http://cryto.net/pythonwhois


class bcolors:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"


fo = open("domains.txt", 'r')
domains = fo.readlines()
fo.close()
prefix = ['com', 'ir', 'net']
for pre in prefix:
    print("********************* " + bcolors.RED + '.' + pre + bcolors.RESET + " *********************")
    for domain in domains:
        domain = str(domain).replace('\n', '') + '.' + pre
        details = pythonwhois.get_whois(domain)
        print('>>', bcolors.BLUE + domain + bcolors.RESET)
        if (str(details['contacts']['registrant'])) != 'None':
            print(details['contacts']['registrant'], '\n')
        else:
            print(bcolors.CYAN + "Available!\n" + bcolors.RESET)
