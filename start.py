from __future__ import unicode_literals, print_function
#from prompt_toolkit import print_formatted_text, HTML
from termcolor import colored
import portscanner
import Vulnscanner1
import feedback


def start_off():
    while True:
        print(" ")
        print(" ")
        print("\t\t     The Hunter Script ")
        print(" ")
        print(colored("                             ,-. ", 'red', attrs=['bold']))
        print(colored("        ___,---.__          /'|`\          __,---,___", 'red', attrs=['bold']))
        print(colored("     ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-. ", 'red', attrs=['bold']))
        print(colored("   ,'        |           ~'\     /`~           |        `. ", 'red', attrs=['bold']))
        print(colored("  /      ___//              `. ,'          ,  , \___      \ ", 'red', attrs=['bold']))
        print(colored(" |    ,-'   `-.__   _         |        ,    __,-'   `-.    | ", 'red', attrs=['bold']))
        print(colored(" |   /          /\_  `   .    |    ,      _/\          \   | ", 'red', attrs=['bold']))
        print(colored(" \  |           \ \`-.___ \   |   / ___,-'/ /           |  / ", 'red', attrs=['bold']))
        print(colored("  \  \           | `._   `\\   |  //'   _,' |           /  / ", 'red', attrs=['bold']))
        print(colored("   `-.\         /'  _ `---'' , . ``---' _  `\         /,-' ", 'red', attrs=['bold']))
        print(colored("      ``       /     \    ,='/ \`=.    /     \       '' ", 'red', attrs=['bold']))
        print(colored("              |__   /|\_,--.,-.--,--._/|\   __| ", 'red', attrs=['bold']))
        print(colored("              /  `./  \\`\ |  |  | /,//' \,'  \ ", 'red', attrs=['bold']))
        print(colored("             /   /     ||--+--|--+-/-|     \   \ ", 'red', attrs=['bold']))
        print(colored("            |   |     /'\_\_\ | /_/_/`\     |   | ", 'red', attrs=['bold']))
        print(colored("             \   \__, \_     `~'     _/ .__/   / ", 'red', attrs=['bold']))
        print(colored("              `-._,-'   `-._______,-'   `-._,-' ", 'red', attrs=['bold']))
        print(colored(""))
        print(colored("\n\nNote: Run this tool as ROOT User as it needs superuser permissions.", 'cyan', attrs=['bold']))   

        print(colored("1] MAC \t\t 2]Portscanning", 'green', attrs=['bold']))        
        options = int(input("Choose an Option: "))
        
        if options == 1:
            print("!")
            break        
        elif options == 2:
            portscanner.hunt_open_ports()
            break
        elif options == 3:
            Vulnscanner1.hunt_vuln()
            break
        elif options == 4:
            print("4")
        #elif options == 0:
         #   feedback.send_email()
          #  break
        else:
            print("COMPLETE")
            break

        #break
    
#The tool should consist of the following:
# 1] Trojan Creation    2] User should be able to choose the type of file
# 3] If user wants it should not embed the malware in any file
# 4] It should have a CVE exploitation option where all CVE automation will be possible.
# 5] If possible it should contain some open source Intelligence tools
# 6] 
#
#
#
#
#
#
#