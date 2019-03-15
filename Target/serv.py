#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import ctypes
import os
import platform
import time
import subprocess
port=1100
sock = socket.socket()
sock.bind(('', port))
while True:
 sock.listen(1)
 conn, addr = sock.accept()
 data = conn.recv(1024)
 addlen=len(data)-3
 add=data[:-addlen]
#edit from this------------------------------------ x='buffalo'    
#                                                                  exec("%s = %d" % (x,2))
#                                                                  print buffalo ; rfind()
 if data=='cdopen':
  os.system("eject /dev/sr0")
  conn.send('Ready')
 elif data=='os':
  conn.send(platform.system())
 elif data=='help':
    conn.send('cdopen\nos\nhelp\nstop')
 elif data=='stop':
    conn.close()
    break
 elif add=='add':
   valpos=data.rfind('-')+1
   valend=data[valpos:len(data)]
   valend=int(valend)
   pos=data.rfind('-',0,valpos-2)+1
   space=data.rfind(' ',pos)
   variablename=data[pos:space]
   exec("%s = %d" % (variablename,valend))
   conn.send('this func is not ready')
 elif data=='reload':
   conn.send("i can't find solution for this:(")
 elif data=='syscmd':
   conn.send('what to do?')
   cmd=str(conn.recv(1024))
   print cmd
   conn.send('making')
   process = subprocess.Popen("python2","test.py")
   code = process.wait()
   conn.send(str(code))
 else:
  conn.send('Error: Unknow command')
#
#to this----------------------------------------------
