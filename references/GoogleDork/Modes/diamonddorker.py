import argparse
from os import system, name 
import os 
import sys
def clear(): 
    return os.system('cls' if os.name == 'nt' else 'clear')
import argparse
from Modes import Gmode, PLCs, Scada2, Scada3, Tor, Proxy

print ("")
A = """             
                    |
  ,_._._._._._._._._T__________________________________________________________
  |G|o|o|g|l|e|_|_|_O_________________________________________________________/
                    R                                                           V1.5.3
                    |
                    
    Diamond Sorter - Dork Scanner (DS-DS) coded by CashOutGang
    please use -h to see help
    """
print ("")
print(A)

parser = argparse.ArgumentParser("katana-ds.py",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-g","--google", help="google mode", action='store_true' )
parser.add_argument("-s","--scada", help="scada mode ", action='store_true' )
parser.add_argument("-s2","--scada2", help="scada mode 2 ", action='store_true' )
parser.add_argument("-s3","--scada3", help="scada mode 3", action='store_true' )
parser.add_argument("-t","--tor", help="Tor mode ", action='store_true' )
parser.add_argument("-p","--proxy", help="Proxy mode ", action='store_true' )


args = parser.parse_args()

if args.google :
 clear() 
 from Modes import Gmode
 
if args.scada :
  clear ()
  from Modes import Scada

if args.scada2 :
  clear ()
  from Modes import Scada2

if args.scada3 :
  clear ()
  from Modes import Scada3
 
if args.tor :
  clear ()
  from Modes import Tor
  
if args.proxy :
 clear ()
 from Modes import Proxy

