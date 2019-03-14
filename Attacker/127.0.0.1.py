import socket
import os
sock = socket.socket()
sock.connect(('127.0.0.1',1100))
comnd=raw_input('Command: ')
if comnd=='exit':
  a=6
elif comnd=='stop':
  sock.send(comnd)
  sock.close()
else:
  sock.send(comnd)
  data = sock.recv(1024)#continue this
  print data
os.system('python 127.0.0.1.py')
