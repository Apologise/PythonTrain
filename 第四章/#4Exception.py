# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:26:29 2017

@author: Administrator
"""

try:
    num = eval(input("请输入一个整数："))
    print(num*2)
except NameError:
    print("输入错误，请输入一个整数！")