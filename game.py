import pygame
import sys

from pygame.locals import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
bg = black

fps = 30
dispWidth = 800
dispHeight = 600
cellsize = 10

UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

def runGame():
    startx = 3
    starty = 3
    coords = [{'x': startx, 'y': starty}]
    direction = RIGHT

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = LEFT
                elif event.key == K_RIGHT:
                    direction = RIGHT
                elif event.key == K_DOWN:
                    direction = DOWN
                elif event.key == K_UP:
                    direction = UP

        if direction == UP:
            newCell = {'x': coords[0]['x'], 'y': coords[0]['y']-1}

        if direction == DOWN:
            newCell = {'x': coords[0]['x'], 'y': coords[0]['y']+1}

        if direction == LEFT:
            newCell = {'x': coords[0]['x']-1, 'y': coords[0]['y']}

        if direction == RIGHT:
            newCell = {'x': coords[0]['x']+1, 'y': coords[0]['y']}

        del coords[-1]

        coords.insert(0, newCell)
        setDisplay.fill(bg)
        drawCell(coords)
        pygame.display.update()
        fpsTime.tick(fps)

def drawCell(coords):
    for coords in coords:
        x = coords['x']*cellsize
        y = coords['y']*cellsize
        makeCell = pygame.Rect(x, y, cellsize, cellsize)
        pygame.draw.rect(setDisplay, white, makeCell)

while True:
    global fpsTime
    global setDisplay

    fpsTime = pygame.time.Clock()
    setDisplay = pygame.display.set_mode((dispWidth, dispHeight))
    pygame.display.set_caption('controlling')
    runGame()
