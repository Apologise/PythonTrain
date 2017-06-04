# -*- coding: utf-8 -*-
"""
Created on Sun May 28 16:33:57 2017

@author: Administrator
"""

import turtle

turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.down()
turtle.pensize(25)
turtle.seth(-40)
turtle.pencolor("yellow")
for i in range(4):
    turtle.pencolor("black")
    turtle.circle(40, 80)
    turtle.pencolor("green")
    turtle.circle(-40, 80)
turtle.pencolor("silver")
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 200)
turtle.fd(40*2/3)
