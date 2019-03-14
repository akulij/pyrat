#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import ctypes
import os
import platform
sock = socket.socket()
sock.bind(('', 1100))
while True:
 sock.listen(1)
 conn, addr = sock.accept()
 data = conn.recv(1024)
#edit from this------------------------------------
#
 if data=='cdopen':
  os.system("eject /dev/sr0")
  conn.send('Ready')
 elif data=='os':
  conn.send(platform.system())
 elif data=='help':
    conn.send('cdopen\nos\nhelp\nstop')
 elif data=='stop':
    break
 else:
  conn.send('Error: Unknow command')
#
#to this----------------------------------------------

conn.close()
