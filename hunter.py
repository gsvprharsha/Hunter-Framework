import itertools
import os
import threading
import time
import sys
import start
from termcolor import colored

done = False

def animation():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(colored('\r[+] Starting The Hunter Framework...' + c, 'yellow', attrs=['bold']))
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(0.2)
    os.system("clear")
    start.start_off()
    
    
t = threading.Thread(target=animation)
t.start()
time.sleep(3)
done = True