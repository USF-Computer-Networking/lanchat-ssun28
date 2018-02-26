#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
	ipscan.py

	A program that discovers other computers 
	on the same LAN

	In a local area network, the Mac is requested for 
	all IP addresses in the network segment. 
	In Ethernet, the host is in this way to determine 
	if the IP address is occupied.
"""

import sys, os
from scapy.all import *

if os.geteuid() != 0:
    print "This program must be run as root. Aborting."
    sys.exit()
if len(sys.argv) < 2:
    print "Please Use %s x.x.x" % (sys.argv[0])
    exit()
conf.verb = 0
ipscan = sys.argv[1] + ".0/24"
f = file("Mac_list.txt", 'w')
ans, unans = srp(Ether(dst = "FF:FF:FF:FF:FF:FF")/ARP(pdst = ipscan), timeout = 2)
print ans[0]
for snd, rcv in ans:
    print rcv
    list_mac = rcv.sprintf("%Ether.src% -> %ARP.psrc%")
    print rcv.sprintf("%Ether.src% -> %ARP.psrc%")
    f.write(list_mac+'\n')
f.close()