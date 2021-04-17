#!/usr/bin/python
# -*- coding: utf-8 -*-
# this file is executed automatically at startup
import math
import os
import time
import socket
import sys
from datetime import datetime
import glob

def ClientSocket():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    # Connect the socket to the port where the server is listening
    server_address = ('192.168.1.26', 5560)
    print >>sys.stderr, 'Connecting to: %s port: %s' % server_address
    
    try:
        sock.connect(server_address)
    except socket.timeout:
        print "timeout error"
    except:
        print "general connection error"

    os.chdir("/home/pi/rilevazioni/")
    x=0
    files = glob.glob("*.txt")
    files.sort()
    stringsToSend  = ""
    for file in files:
        x=x+1
        if(len(files) != x):
          print(file)
          f = open("/home/pi/rilevazioni/"+file, "r")
          for c in f:
              try:
                try:
                    if(c!=""):
                        sock.send(str.encode(c.replace("\n", "")))
                        print str.encode(c.replace("\n", ""))
                except:
                    print "general connection error"
              except:
                  print "file error"
          os.rename("/home/pi/rilevazioni/"+file, "/home/pi/inviate/"+file)
        else: 
            print "no useful files found"
    sock.close()

while 1==1:
      ClientSocket()
      time.sleep(3)
