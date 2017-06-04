# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:29:37 2017

@author: Administrator
"""

Money = input('请输入金钱：')
if Money[-1] in ['$']:
    result = eval(Money[0:-1])*6
    print("美元转为人民币为：{:.2f}".format(result))
else:
    result = eval(Money[0:-1])/6
    print("人民币转为美元为：{:.2f}".format(result))