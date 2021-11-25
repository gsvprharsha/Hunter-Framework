import subprocess
import termcolor
import portscanner
import hunter_server
import arp_spoof
import sys

print(" ")
print(termcolor.colored("The ",'red', attrs=['bold']))
print(termcolor.colored("██╗  ██╗██╗   ██╗███╗  ██╗████████╗███████╗██████╗ ",'red'))
print(termcolor.colored("██║  ██║██║   ██║████╗ ██║╚══██╔══╝██╔════╝██╔══██╗",'red'))
print(termcolor.colored("███████║██║   ██║██╔██╗██║   ██║   █████╗  ██████╔╝",'red'))
print(termcolor.colored("██╔══██║██║   ██║██║╚████║   ██║   ██╔══╝  ██╔══██╗",'red'))
print(termcolor.colored("██║  ██║╚██████╔╝██║ ╚███║   ██║   ███████╗██║  ██║",'red'))
print(termcolor.colored("╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ Script V1.0",'red'))
print(" ")
print(termcolor.colored("\nNote: Run this tool as ROOT User as it needs superuser permissions.", 'yellow', attrs=['bold']))
print(termcolor.colored("1] Port Scanner \t\t\t 2]SSH Bruteforce", 'green', attrs=['bold']))
print(termcolor.colored("3] ARP Spoof \t\t\t\t 4]Backdoor", 'green', attrs=['bold']))
print(termcolor.colored("5] Password Sniffer\n", 'green', attrs=['bold']))
print(termcolor.colored("[=] Press 0 to exit\n",'magenta', attrs=['bold']))
option = input("Choose an Option: ")

if option == "0":
    print(termcolor.colored("[**] Exiting...",'red',attrs=['bold']))
    subprocess.call("exit", shell=True)
if option == "1":
    portscanner.hunt_open_ports()
elif option =="2":
    print("SSH Bruteforce")
elif option =="3":
    arp_spoof.hunt_arp_spoofer()
elif option =="4":
    hunter_server.hunt_server()
elif option =="5":
    print("Password Sniffer")
