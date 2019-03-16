#!/usr/bin/env python

import socket
import subprocess
import os , sys
import shutil
import time
sock = socket.socket()
sock.bind(('', 8181))
port=1100
print os.listdir(os.getcwd())
while True:
 print ' '
 sock.listen(1)
 conn, addr = sock.accept()
 print 'connected:', addr
 data = conn.recv(1024)
 #conn.send(data.upper())
 conn.send('connected')
 print data
