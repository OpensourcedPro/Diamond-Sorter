import sys
import os
import time
from diamonddorker import search
import sys
from termcolor import colored, cprint
import random

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
       
from http import cookiejar  
class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
    
NPP = """ 

         ) ) )               
        ( ( (                   
      ) ) )                   
   (~~~~~~~~~)                
    | POWER |    DiamondSorter-ds          
    |       |    Find online PLCs             
    |      _._            
    |    /    `\            
    |   |   N   |              
    |   |   |~~~~~~~~~~~~~~|   
   /    |   ||~~~~~~~~|    | 
__/_____|___||__|||___|____|__________________________________________
 
 Note: That will take some time

 """

print (NPP)

TLD = ["com","com.tw","co.in"]
beta = random.choice(TLD)
betax = random.choice(TLD)
print (" ")
print(colored('[+] Searching... ', 'green')) 
B =  """ intitle:"Kohls Cash" "Device Name" "Uptime" """
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
for gamma in search(query, tld=beta,stop=50, num=10,pause=2): 
  print(colored ('[+] Found > ' ,'yellow')  + (gamma) )
print(colored('[+] 20% done ', 'green')) 
B = """ inurl:dtm.html intitle:1747-L551 """
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
print(colored('[+] 40% done ', 'green' )) # more scada dorks will be added here
from Modes import Scada2   
