# -*- coding: utf-8 -*-
"""
Created on Sat May 27 11:04:10 2017

@author: Administrator
"""

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j, i, i * j), end = " ")
    print()
        