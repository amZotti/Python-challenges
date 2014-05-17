import pygame
import sys
import pygame.mixer
from pygame.locals import *
pygame.init()

sound = pygame.mixer.Sound('start.wav.wav')
thunder = pygame.mixer.Sound('thunder.wav')
clock = pygame.time.Clock()
sound.play()


size = width,height = 600,400
black = 0,0,0
screen = pygame.display.set_mode(size)


img = pygame.image.load('pokemon.png')
img2 = pygame.image.load('pokemon2.png')
img = pygame.transform.scale(img,(100,100))


x = 0
y = 0
x2 = 200
y2 = 200
r = 0

while 1:
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        #event = User input
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            thunder.play()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            pygame.image.save(screen, "screenshot.png")

            



    clock.tick(60)
    screen.fill((r,0,0))
    screen.blit(img2,(x2,y2))
    screen.blit(img,(mx-50,my-50))
    pygame.display.flip()
 
    x2 = x2 - 1
    y2 = x2 + 1

    if r == 255:
        r1 = -1
    elif r == 0:
        r1 = 1

    r = r + r1
    print(mx,my)
