# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:30:44 2017

@author: Administrator
"""
import time
scale = 10
print("Starting", end = '')
for i in range(scale+1):
    if i == 0:
        print("...", end = '')
    time.sleep(0.1)
print("Done!")