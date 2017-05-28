# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:27:57 2017

@author: Administrator
"""

import  turtle
turtle.pencolor("pink")
for i in range(1,160,4):
    turtle.seth(90)
    turtle.fd(i)
    turtle.seth(180)
    turtle.fd(i+1)
    turtle.seth(-90)
    turtle.fd(i+2)
    turtle.seth(0)
    turtle.fd(i+3)
turtle.seth(90)
turtle.fd(161)
turtle.seth(180)
turtle.fd(162)
turtle.seth(-90)
turtle.fd(163)
