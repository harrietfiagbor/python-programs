# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:59:47 2021

@author: Harriet Fiagbor
"""

# this is a mood computer

import random

print("I sense your energy. Your true emotions are flowing and appearing on my screen")

print("You are ")

mood = random.randrange(3)

if mood == 0:
    #happy
    print(
 """               ---------------------
                |                      |
                |        o o           |
                |                      |
                |        <             |
                |     .......          |
                ------------------------
          """
        )