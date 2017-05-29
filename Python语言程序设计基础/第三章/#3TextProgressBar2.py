# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:08:41 2017

@author: Administrator
"""

import time
for i in range(101):
    print("\r{:2}%".format(i),end='')
    time.sleep(0.1)