import sys
import os
import time
from googlesearch import search
import sys
from termcolor import colored, cprint
import random
from http import cookiejar  
class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
    
TLD = ["com.qa","ru","com.sa"]

lux = random.choice(TLD)

Vx = """ inurl:/Portal0000.htm """
query = Vx
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
for gamma in search(query, tld=lux, num=10,stop=50,pause=2): 
     print(colored ('[+] Found > ' ,'yellow')  + (gamma) )   
print(colored('[+] 90% done ', 'green' ))
print(colored('[+] 100% done ', 'green' ))
print(colored('[+] done ', 'green' ))
print(colored ('[! >] delete .google-cookie file in DS DIR  ' ,'red')) 






