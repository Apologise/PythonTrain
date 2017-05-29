# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:05:23 2017

@author: Administrator
"""

import time
scale = 10
print("-----Starting-----")
for i in range(scale+1):
    a, b = '**'*i,'..'*(scale - i)
    c = (i / scale)*100
    print("%{:^3.0f}[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("-----Ended-----")