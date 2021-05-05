# -*- coding: utf-8 -*-
"""
Created on Mon May  3 18:39:30 2021

@author: Harriet Fiagbor

Writing Words to pygame display
"""
import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello World")

GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32 )
textsurfaceObj = fontObj.render('Hello world', True, RED, GREEN)
textrectObj = textsurfaceObj.get_rect()
textrectObj.center = (200, 150)


while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textsurfaceObj,textrectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()