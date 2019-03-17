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
 sotest='heelo'
 conn, addr = sock.accept()
 data = conn.recv(1024)
 addlen=len(data)-3
 add=data[:-addlen]
 showlen=len(data)-4
 show=data[:-showlen]
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
 elif show=='show':
   shower='showing'
   pos=data.rfind('-')+1
   end=data[pos:len(data)]
   exec("%s=%s" % (shower,end))
   if showing!=str(showing):
     showing=str(showing)
   conn.send(showing)
 elif add=='add':
   valpos=data.rfind('-')+1
   valend=data[valpos:len(data)]
   valend=int(valend)
   pos=data.rfind('-',0,valpos-2)+1
   space=data.rfind(' ',pos)
   variablename=data[pos:space]
   exec("%s = %d" % (variablename,valend))
   conn.send('ready')
 elif data=='reload':
   conn.send("i can't find solution for this:(")
 else:
  conn.send('Error: Unknow command')
#
#to this----------------------------------------------
