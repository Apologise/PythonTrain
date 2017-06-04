# -*- coding: utf-8 -*-
"""
Created on Mon May 29 08:11:34 2017

@author: Administrator
"""

import math

wordday = 120
for N in [0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.01]:
    dayup = math.pow((1+N), workday)
    print("answer:{:.2f}".format(dayup))