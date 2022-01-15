#!usr/bin/env python
import subprocess
import paramiko
import arp_spoofer
#from pip._vendor.distlib.compat import raw_input
import os
import termcolor
import manager
import portscanner

os.system("clear")
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
print(termcolor.colored("1] Port Scanner \t\t\t 2] SSH Bruteforce", 'green', attrs=['bold']))
print(termcolor.colored("3] ARP Spoof \t\t\t\t 4] Backdoor", 'green', attrs=['bold']))
print(termcolor.colored("5] Password Cracker \t\t\t 6] Network Scanner\n", 'green', attrs=['bold']))
print(termcolor.colored("7] MAC Changer\n", 'green', attrs=['bold']))
print(termcolor.colored("[=] Press 0 to exit\n",'magenta', attrs=['bold']))
option = input("Choose an Option: ")


if option == "0":
    os.system("exit")
elif option == "1":
    portscanner.lame_open_ports()
elif option =="2":
    os.system("sudo python3 main.py")
elif option =="3":
    arp_spoofer.lame_arp_spoofer()
elif option =="4":
    manager.lame_server()
elif option =="5":
    os.system("sudo python3 cracker-password.py")
elif option =="6":
    os.system("sudo python3 networkscanner.py")
elif option =="7":
    os.system("sudo python3 macchanger.py")
