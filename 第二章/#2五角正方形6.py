# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:05:29 2017

@author: Administrator
"""

import  turtle
turtle.fd(140)
turtle.up()
turtle.fd(60)
for angel in [90, 180,-90]:
    turtle.seth(angel)
    turtle.fd(60)
    turtle.down()
    turtle.fd(140)
    turtle.up()
    turtle.fd(60)