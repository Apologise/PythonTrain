# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:07:48 2017

@author: Administrator
"""

def reverse(s):
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]
str = input("请输入一个字符串：")
print(reverse(str))