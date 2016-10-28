#!/usr/bin/python

from scapy.all import sniff,ARP
from signal import signal,SIGINT

ip_mac = {}

def watchARP(pkt):
    if pkt[ARP].op == 2:
        print pkt[ARP].hwsrc + " " +pkt[ARP].psrc
    if ip_mac.get(pkt[ARP].psrc) == None:
        print 'Find new device '+\
        pkt[ARP].hwsrc + " " +\
        pkt[ARP].psrc
        ip_mac[pkt[ARP].psrc] = pkt[ARP].hwsrc
    elif ip_mac.get(pkt[ARP].psrc) and ip_mac[pkt[ARP].psrc]!=pkt[ARP].hwsrc:
        print pkt[ARP].hwsrc + \
        " has get new ip: " +\
        pkt[ARP].psrc +\
        "(old is " + ip_mac[pkt[ARP].hwsrc] + ")"

        ip_mac[pkt[ARP].hwsrc]=pkt[ARP].psrc
 

sniff(prn=watchARP,filter="arp",iface="eth0",store=0)


