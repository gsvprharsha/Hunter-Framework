#!usr/bin/env python
# Made by: @gsvprharsha(github)
# Still under development.....Feel free to contribute to this repo

import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest='target', help="Target IP/ IP Range")
    (options,arguments) = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/ arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False) [0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "MAC": element[1].hwsrc}
        client_list.append(client_dict)
    return (client_list)

def print_result(result_list):
    print("IP address\t\t\tMAC Address\n-----------------------------------------")
    for client in result_list:
        print(client["ip"]+ "\t\t" + client["MAC"])

scan_result = scan("10.0.2.1/24")
print_result(scan_result)
