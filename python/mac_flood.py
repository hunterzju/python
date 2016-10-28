#!/usr/bin/python

import sys
import time
from scapy.all import *

iface = "eth1"
if len(sys.argv)>=2:
    iface = argv[1]

while(1):
    packet = Ether(src=RandMAC("*:*:*:*:*:*"),
                   dst=RandMAC("*:*:*:*:*:*"))/\
             IP(src=RandIP("*.*.*.*"),
                dst=RandIP("*.*.*.*"))/\
             ICMP()
    time.sleep(0.5)
    sendp(packet,iface=iface,loop=0)