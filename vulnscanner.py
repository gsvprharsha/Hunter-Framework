import socket
from IPy import IP
from termcolor import colored
#testphp.vulnweb.com ip = 18.192.172.30

class Port_scan():
    banner = []
    open_ports = []
    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num       
    
    def scan(self):
        for port in range(1, 500):
            self.scan_port(port)

    def check_ip(self):
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.9)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip("\n").strip("\r")
                self.banner.append(banner)
            except:
                self.banner.append(' ')
            sock.close()
        except:
            pass