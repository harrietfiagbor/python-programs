# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:31:28 2021

@author: Harriet Figabor 
"""

# This is a super stupid basic die rolling program

import random

die1 = random.randrange(6) + 1

die2 = random.randrange(6) + 1

total = die1 + die2

print("you rolled a", die1, "and a", die2, "for the total of ", total)

s = input("\n\n Press Enter to exit")

#raw_input for python version == 2.x

print(s)

