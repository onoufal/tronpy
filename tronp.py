import requests
from tronpy.keys import PrivateKey
from pyfiglet import Figlet
import time
import requests
from colorama import Fore,Style


print (Fore.YELLOW,'Programer website => https://Mmdrza.com')
print (Fore.WHITE,'please wait .........')
time.sleep(2)
#fg= Figlet('roman')
#fgx= fg.renderText('Mmdrza')
#print(fgx,Fore.CYAN,'\n------------------------------------')
time.sleep(4)
count=0
while True:
    count+=1
    priv_key=PrivateKey.random()
    addr=priv_key.public_key.to_base58check_address()

    Hexer=priv_key.hex()

    req= requests.get("https://apilist.tronscan.org/api/account?address="+addr)
    rat = req.json()
    value= dict(rat)["balance"]
    print (Fore.MAGENTA,'TRON Wallet Scan Number:' , str(count),Fore.LIGHTWHITE_EX,'\nADDRESS =',Fore.GREEN,str(addr),Fore.LIGHTYELLOW_EX,'\nPrivate Key =: ',Fore.GREEN, str(priv_key),Fore.YELLOW , '\nHEX =',Fore.MAGENTA,str(Hexer),Fore.RED,' BAL:',Fore.WHITE,str(value),Fore.CYAN,'\n========================[M M D R A Z A . C O M]=======================',Style.RESET_ALL)

    if value >0:
        print('Winner Save Information Wallet Here File >>>> Winner.txt ')
        f=open(u"Winner.txt" , "a")
        f.write(f'\nAddress: {addr}')
        f.write(f'\nPrivate Key : {priv_key}')
        f.write('\n=====================================')
        f.close()

