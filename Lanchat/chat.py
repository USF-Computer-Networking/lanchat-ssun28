#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    chat.py

    A program that supports sending text messages carried 
    in UDF packets

    specify an address and port from which to receive data

"""

import socket
import threading

def print_menu():
    print("Select the operation you want: 1 send　２ receive　")


def recv_data(udp_socket):
    data, remote_address = udp_socket.recvfrom(4096)

    print("receive the data from %s-----%s" % (remote_address, data.decode()))


def send_data(udp_socket):
    data = input("Please type the data you want send:")
    ip = input("IP Address:")
    port = int(input("Port:"))

    udp_socket.sendto(data.encode(), (ip, port))

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    recv_thd = threading.Thread(target=recv_data, args=(udp_socket,))
    recv_thd.start()

    udp_socket.bind(('', 8888))
    while True:
        print_menu()
        op = input("Please select:")
        if op == '1':
            send_data(udp_socket)
        elif op == '2':
            recv_data(udp_socket) 
        else:
            print("error")
    udp_socket.close()

if __name__ == '__main__':
    main()