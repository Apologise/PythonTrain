# -*- coding: utf-8 -*-
"""
Created on Sun May 28 09:28:18 2017

@author: Administrator
"""
#e2DrawPython.py
'''
import turtle

turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40*2/3)
'''
from turtle import *

setup(650,350,200,200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor('purple')
seth(-40)
for i in range(4):
    circle(40,80)
    circle(-40,80)
circle(40,80/2)
fd(40)
circle(16, 180)
fd(40*2/3)


