# -*- coding: utf-8 -*-
"""
Created on Sat May 27 16:46:21 2017

@author: Administrator
"""

diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']
for i in range(0,5):
    for j in range(0,5): 
        if (i != j):
            print('{}{}'.format(diet[i], diet[j]))