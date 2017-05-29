# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:12:00 2017

@author: Administrator
"""

import math
dayup = math.pow(1.0 + 0.001,365)
daydown = math.pow(1.0 - 0.001, 365)
print("向上：{:.2f}, 向下：{:.2f}".format(dayup, daydown))
