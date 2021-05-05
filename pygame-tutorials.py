"""
Author: Harriet Fiabor
Monday 5/3/21

"""

import pygame, sys # import pygame and sys modules
from pygame.locals import * # import pygame modules that are easily recognizable

pygame.init() # start pygame
DISPLAYSURF = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Hello World!')

while True: # this is the main loop the game will take
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
