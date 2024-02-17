import requests 
import proxybroker 
from googlesearch import search
import sys
import sys
from termcolor import colored, cprint
import warnings
import random
from http import cookiejar  
class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
    
def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()

def clear(): 
    return os.system('cls' if os.name == 'nt' else 'clear')
        
    
print ("")

A = """
,_._._._._._._._._|__________________________________________________________
|G|o|o|g|l|e|_|_|_|_________________________________________________________/
                  |
    DiamondSorter dork scanner (DiamondSorter-DS)
    Google Mode
"""
print ("")
print(A)
TLD = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
s = requests.Session()
s.cookies.set_policy(BlockAll())
alpha = input (colored('[>] Please set a Dork : ', 'green' )) 
query = alpha
tld =  random.choice(TLD)   
# print("")
# print(colored(tld , 'green'))

    
for gamma in search(query, tld , num=10 , stop=95 , pause=2): 
    print(colored ('[+] Found > ' ,'yellow')  + (gamma) )
print(colored ('[+] Done  ' ,'green'))
print(colored ('[! >] delete .google-cookie file in Katana DIR  ' ,'red')) 
