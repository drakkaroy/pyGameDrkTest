import pygame
import sys

from pygame.locals import *

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)

windowWidth = 600
windowHeight = 400
setDisplay = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('drk game')

img = pygame.image.load('assets/boy.png')
img = pygame.transform.rotate(img, -90)
imgWidth = 50
imgHeight = 66

#frames per second
FPS = 30
imgx = 0
imgy = 0
pixMove = 5

movement = 'down'

fpsTime = pygame.time.Clock()


while True:
    setDisplay.fill(white)

    if movement == 'down':
        imgy += pixMove
        if imgy > (windowHeight - imgHeight):
            img = pygame.transform.rotate(img, 90)
            movement = 'right'

    if movement == 'right':
        imgx += pixMove
        if imgx > (windowWidth - imgHeight):
            img = pygame.transform.rotate(img, 90)
            movement = 'up'

    if movement == 'up':
        imgy -= pixMove
        if imgy == 0:
            img = pygame.transform.rotate(img, 90)
            movement = 'left'

    if movement == 'left':
        imgx -= pixMove
        if imgx == 0:
            img = pygame.transform.rotate(img, 90)
            movement = 'down'


    setDisplay.blit(img, (imgx, imgy))

    for event in pygame.event.get():
        #print event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsTime.tick(FPS)



