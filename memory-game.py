# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:31:27 2021

@author: Harriet Fiagbor

Title : Memory Puzzle
"""
import pygame, sys, random
from pygame.locals import *

WINDOWHEIGHT = 640 #size of window's height in pixels
WINDOWWIDTH  = 480 #size of window's width in pixels
BOARDHEIGHT  = 7   #number of rows of boxes
BOARDWIDTH   = 10  # number of clumns of boxes
BOXSIZE      = 40  # size of each box that contains shape
GAPSIZE      = 10  # the gap between each
REVEALSPEED  = 8   # the rate at which box reveals shape
FPS          = 30   #frames per second
assert(BOARDHEIGHT * BOARDWIDTH) % 2 == 0, 'Board needs an even number of boxes for pairs'
XMARGIN     = int(WINDOWWIDTH -(BOARDWIDTH * (BOXSIZE + GAPSIZE)))
YMARGIN     = int(WINDOWHEIGHT -(BOARDHEIGHT * (BOXSIZE + GAPSIZE)))

#setting up the colors
# Color      =    R     G     B
NAVYBLUE     =  ( 60,   60,   100)
WHITE        =  (255,   255,  255)
RED          =  (255,    0,    0)
GREEN        =  (0,     255,   0)
YELLOW       =  (255,   255,   0)
ORANGE       =  (255,   128,   0)
PURPLE       =  (255,    0,   255)
CYAN         =  (0,     255,  255)
BLUE         =  (0,      0,   255)
GRAY         =  (128,   128,  128)

BOXCOLOR     = WHITE #COVER BOX 
HIGHLIGHTCOLOR = BLUE #TELLS WHAT YOUR MOUSE IS ON
BGCOLOR      = NAVYBLUE #BACKGROUND
LIGHTBGCOLOR = GRAY

#Setting up shapes
DONUT      = 'donut'
DIAMOND    = 'diamond'
OVAL       = 'oval'
SQUARE     = 'square'
LINES      = 'lines'

ALLCOLORS  = (RED, GREEN, PURPLE, CYAN, YELLOW, ORANGE, BLUE)
ALLSHAPES  = (DONUT, DIAMOND, OVAL, SQUARE, LINES)
assert len(ALLSHAPES) * len(ALLCOLORS) * 2 >= BOARDHEIGHT * BOARDWIDTH, "Board is too small for variety of shapes and colors"

def main():
    global FPSCLOCK, DISPLAYSURF
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    revealedBoxes = generaterevealedBoxesData(False)
    
    mousex = 0 # x coordinate of mouse
    mousey = 0 # y coordinate of mouse
    pygame.display.set_caption('The Memory Game')
  
    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None # stores the (x, y) of the first box clicked.
    DISPLAYSURF.fill(BGCOLOR)
    
    startGameAnimation(mainBoard)
    
    while True: # main game loop
        mouseClicked = False
        
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)
        
        for event in pygame.event.get(): #event handling
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
                
            elif event.type == MOUSEMOTION:
                mousex , mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked == True
                
                
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy !=None: # mouse is currenctly over a box
            
                
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    
def generaterevealedBoxesData(val): # Boxes that have been revealed
    revealedBoxes= []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val]*BOARDHEIGHT)
    return revealedBoxes
    

def getRandomizedBoard(): # gets possible shapes and colors
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))
            
                   
    random.shuffle(icons)
    numIconUsed = int(BOARDHEIGHT * BOARDWIDTH / 2) 
    # make two of each
    icons = icons[:numIconUsed] * 2
    random.shuffle(icons)
         
    #creating the board structure and placing random icons on it
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del(icons[0])#delete icons from front as it shuffles them to the column
                 
    board.append(column)
         
    return board
    
def leftTopCoordsofBox(x, y):
    return
    
    
    
def getBoxAtPixel(x, y):
    return
    
             
                
                
    