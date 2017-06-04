# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:04:56 2017

@author: Administrator
"""

def fac(n):
    if n == 0:
        return 1
    else:
        return n*fac(n-1)