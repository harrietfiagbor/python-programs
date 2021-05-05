# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 01:55:57 2021

@author: Harriet Fiagbor
"""

#this is a turtle program
import turtle
window =turtle.Screen()

t = turtle.Pen()
t.reset()

for x in range(1, 38):
    t.forward(200)
    t.right(175)
     

window.exitonclick()
