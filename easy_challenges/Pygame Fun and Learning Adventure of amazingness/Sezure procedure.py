import pygame
import sys
import pygame.mixer

pygame.init()

sound = pygame.mixer.Sound('start.wav.wav')
sound.play()

size = width,height = 600,400
black = 0,0,0
screen = pygame.display.set_mode(size)


img = pygame.image.load('pokemon.png')
img2 = pygame.image.load('pokemon2.png')

x = 0
y = 0
x2 = 200
y2 = 200
r = 0

while 1:
    for event in pygame.event.get():
        #event = User input
        if event.type == pygame.QUIT:sys.exit()

    screen.fill((r,0,0))
    screen.blit(img2,(x2,y2))
    screen.blit(img,(x,y))
    pygame.display.flip()
    x += 1
    y += 1
    x2 = x2 - 1
    y2 = x2 + 1

    if r == 255:
        r1 = -1
    elif r == 0:
        r1 = 1

    r = r + r1
