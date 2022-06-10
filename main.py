from asyncio.subprocess import PIPE
import random  #for generating random numbers
import sys
from pip import main
import pygame
import pygame.locals import *

#Global Variables for the game

FPS = 32 
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) # initializes a screen/window for display
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = '/gallery/sprites/bird.png'
BACKGROUND = '/gallery/sprites/background.png'
PIPE = '/gallery/sprites/pipe.png'

if __name__=="__main__":
    # this will be the main point where the game will start