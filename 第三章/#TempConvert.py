# -*- coding: utf-8 -*-
"""
Created on Sat May 27 22:08:33 2017

@author: Administrator
"""
#TempConvert.py
TempStr = input('请输入带有符号的温度值：')
if TempStr[-1] in ['F', 'f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print('转换后的温度是:{:.2f}C'.format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print('转换后的温度是:{:.2f}F'.format(F))
else:
    print('输入的格式错误')