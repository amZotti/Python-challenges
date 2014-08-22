import pygame, sys
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,360),0,32)
'''
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            sys.exit()'''
while True:
    i = random.randint(2,226)
    k = random.randint(0,254)
    j = random.randint(0,253)
    clock.tick(5)
    
    pygame.draw.rect(screen, (i,j,k),Rect((i,j),(k,i)))


    pygame.display.update()
