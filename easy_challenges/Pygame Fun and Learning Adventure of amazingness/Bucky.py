import pygame, sys
from pygame.locals import *



pygame.init()

screen = pygame.display.set_mode((640,360),0,32)

colors = (200,222,114)
points = []


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)

    if len(points) > 1:
        pygame.draw.lines(screen,colors,True,points,5)
        



        pygame.display.update()
