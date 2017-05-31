# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:31:58 2017

@author: Administrator
"""

f = lambda x,y: x + y
print(type(f))
print(f(1,2))
def f1():
    f2()
def f2():
    print("函数f2()")
f1()

def vfunc(a, *b):
    print(type(b))
    for n in b:
        a += n
    return a
result = vfunc(1,2,3,4,5)
print(result)