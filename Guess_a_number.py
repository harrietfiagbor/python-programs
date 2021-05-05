# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 01:18:41 2021

@author: Harriet Fiagbor
"""
import random

#this is a guessing game
print("Hello You there, Welcome to my guessing Game")
print("I am thinking of a number between 0 and 100")
print("try to guess it in a few attempts as possible")

the_number = random.randrange(100) + 1
guess = int(input("Hey, Take a guess: "))

tries = 1

while(guess != the_number):
    if (guess < the_number):
        print("Upper...")
    else:
        print("Lower...")
    guess = int(input("Take a guess: "))
    tries +=1
    
    
if(guess == the_number):
    print("You guessed it!!! The number was", the_number, "and it only took you", tries, "tries!!")
        
