#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,time
os.system('python client.py')
while True:
  os.system('python serv.py')
  time.sleep(10)
