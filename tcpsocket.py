# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 18:48:16 2019

@author: Rachel Rajan
"""

# resources: https://docs.python.org/3/howto/sockets.html
import socket, select
import time

# constants used in tcpsocket.py
BUF_SIZE = 2048
TIMEOUT = 10 # timeout duration in select() in seconds
# Define class (instance variables and methods)
class TCPsocket:
# Constructor: create an object
    def __init__(self):
        self.sock = None # instance variables
        self.host = "" # remote host name
# Create a TCP socket
    def createSocket(self):   
        try:
            start = time.time()
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            end = time.time()
            print("Connecting on robots... done in ", (end-start)*1000, "ms")                           
        except socket.error as e:
            print("Failed to create a TCP socket {}".format(e))           
            self.sock = None
            
# Return the ip of input hostname. Both ip and hostname in string
    def getIP(self, hostname): 
        start = time.time()
        self.host = hostname
        try:
            ip = socket.gethostbyname(hostname) # ip is a local variable to getIP(hostname)     
            end = time.time()
            print("Checking Host uniqueness... passed")
            print("Doing DNS... done in ", (end-start)*1000, "ms")
        except socket.gaierror:
            print("Failed to gethostbyname")
            return None
        return ip

    def connect(self, ip, port):
        if self.sock is None or ip is None:
            return
        try: # server address is defined by pair (ip, port)
            self.sock.connect((ip, port))
            print("Successfully connect to host:", ip)
            print("Checking IP uniqueness... passed")
        except socket.error as e:
            print("Failed to connect: {}".format(e))
            self.sock.close()
            self.sock = None
            
    