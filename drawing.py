# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:00:00 2021

@author: Harriet Fiagbor

Title : pygame drawing
"""

import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, RED,  ((146, 0), (291, 106), (236, 277),(56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, GREEN, (60,60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, GREEN, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, GREEN, (60, 120), (120,120 ),4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 60), 20 )
pygame.draw.ellipse(DISPLAYSURF, BLACK, (300, 250, 50, 60))
pygame.draw.rect(DISPLAYSURF, GREEN,(200, 150, 150, 100))

#this is assigning a pixel to a color
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj 



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()