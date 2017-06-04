# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:10:38 2017

@author: Administrator
"""

import time
scale = 50
print("执行开始".center(scale//2,'-'))
t = time.clock()
for i in range(scale + 1):
    a = '*' * i
    b = '.'*(scale - i)
    c = (i / scale) * 100
    t -= time.clock()
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,-t), end = '')
    time.sleep(0.05)
print("\n" + "执行结束".center(scale//2,'-'))
    
    