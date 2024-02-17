import sys
import os
import time
from googlesearch import search
import sys
from termcolor import colored, cprint
import random
from http import cookiejar
import subprocess
from urllib.parse import quote



class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
    
TLD = [".com", ".org", ".net", ".gov", ".edu", ".co", ".io", ".uk", ".ca", ".au"]
beta = random.choice(TLD)
betax = random.choice(TLD)
lux = random.choice(TLD)

B =  """ intitle:"Miniweb Start Page"  """
query = B
#*****
#*****
for gamma in search(query, tld=beta,stop=50, num=10,pause=2): 
  print(colored ('[+] Found > ' ,'yellow')  + (gamma) ) 
print(colored('[+] 60% done ', 'green')) #####
print(colored('[+] Sleeping for 10s...', 'green'))
time.sleep(5)

luxs = random.choice(TLD)
B = """ inurl:"Portal/Portal.mwsl" """
query = B
# ****
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(100):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
#*****
for gamma in search(query, tld=betax, num=10,stop=50,pause=2): 
     print(colored ('[+] Found > ' ,'yellow')  + (gamma) )
    
print(colored('[+] 80% done ', 'green' )) 
from Modes import Scada3