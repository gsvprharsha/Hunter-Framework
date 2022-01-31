import socket
from IPy import IP
from termcolor import colored
#testphp.vulnweb.com ip = 18.192.172.30

def hunter_open_ports():
    def scan(target, port_range):
        converted_ip = check_ip(target)
        print(colored("\n" + "[-_0]Scanning the target " + str(target), "yellow", attrs=['bold']))
        for port in range(1, port_range):
            scan_port(converted_ip, port)

    def check_ip(ip):
        try:
            IP(ip)
            return(ip)
        except ValueError:
            return socket.gethostbyname(ip)

    def get_banner(s):
        return s.recv(1024)

    def scan_port(ipaddress, port):
        try:
            sock = socket.socket()
            sock.settimeout(0.9)
            sock.connect((ipaddress, port))
            try:
                banner = get_banner(sock)
                print(colored("[+]Open Port " + str(port) + " " + str(banner.decode().strip("\n")), "green", attrs=['bold']))
            except:
                print(colored("[+]Open Port " + str(port), "green", attrs=['bold']))
        except:
            pass


    targets = input("[+]Enter the Target/s to initiate Scan(Split Multiple Targets with , ): ")
    port_range = int(input("Enter the range of ports to scan(500 for first 500 ports): "))
    if ',' in targets:
        for ip_add in targets.split(","):
            scan(ip_add.strip(" "), port_range)
    else:
        scan(targets, port_range)
