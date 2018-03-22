#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    ipscan_graph.py
    
    A program to build on  network scanning and 
    present the information in a graphical manner.

    To see the valid IP of your local area network, 
    and the IP addresses are not occupied.
"""

import platform 
import sys 
import os 
import time 
import thread
import numpy as np            
import matplotlib.pyplot as plt 

countList = []
    
def get_os(): 
    os = platform.system() 
    if os == "Windows": 
        return "n"
    else: 
        return "c"
        
def ping_ip(ip_str): 
    cmd = ["ping", "-{op}".format(op=get_os()), 
            "1", ip_str] 
    output = os.popen(" ".join(cmd)).readlines() 
    flag = False
    for line in list(output):
        if not line: 
            continue
        if str(line).upper().find("TTL") >=0: 
            flag = True
            countList.append(1)
            break     
    if flag: 
        print "ip: %s is valid ********"%ip_str 
    
def find_ip(ip_prefix): 
    for i in range(1,256): 
        ip = '%s.%s'%(ip_prefix,i) 
        thread.start_new_thread(ping_ip, (ip,)) 
        time.sleep(0.3) 
        
if __name__ == "__main__": 
    print "start time %s"%time.ctime() 
    commandargs = sys.argv[1:] 
    args = "".join(commandargs)     
        
    ip_prefix = '.'.join(args.split('.')[:-1]) 
    find_ip(ip_prefix) 
    print "end time %s"%time.ctime()

    print "Total valid ip : %s" %len(countList)
    i = 255
    j = len(countList)

    labels = 'Valid ip = ' + str(j), 'Invalid ip = ' + str(i - j)
    fracs = [j, i - j]
    plt.axes(aspect=1)
    plt.pie(x=fracs, labels=labels,autopct='%3.2f %%',
            shadow=True, labeldistance=1.1, startangle = 90,pctdistance = 0.6)
    plt.title("Valid ip pie chart")    
    plt.savefig("pieChart.jpg")        
    plt.show()        
