import pygame
import sys
from pygame.locals import *

white = (255, 255, 255)
red = (255, 0, 0)

windowWidth = 600
windowHeight = 400

gameName = "DRK GAME"

setDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('drk game')

img = pygame.image.load('assets/boy.png')

imgWidth = 50
imgHeight = 66

#frames per second
FPS = 30
