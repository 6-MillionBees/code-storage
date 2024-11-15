# Arden Boettcher
# 11/15/24
# Pygame Practice

from random import randint
import pygame
from pygame.locals import *
from sys import exit
pygame.init()


X = 400
Y = 400
width = 50
height = 50
screen = pygame.display.set_mode((X, Y))
rect = Rect(200, 80, width, height)
running = True
score = 0
font = pygame.font.Font('CascadiaCodeNF.ttf', 15)
text1 = font.render(f'click', True, (255, 255, 255), None)
text2 = font.render(f'me!', True, (255, 255, 255), None)

while running:
    for event in pygame.event.get():

        if event.type == QUIT:
            print(score)
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                score += 1
                rect = Rect(randint(width, X - width), randint(height, Y - height), width, height)

        # elif event.type == MOUSEMOTION:
        #     mouse_pos = pygame.mouse.get_pos()
        #     print(f'({mouse_pos[0]}, {mouse_pos[1]})')
        #     rect = Rect(mouse_pos[0], mouse_pos[1], 50, 60)

    screen.fill((127,127,127))
    pygame.draw.rect(screen, (255,0,0), rect)
    screen.blit(text1, (rect[0] + 3, rect[1] + 9))
    screen.blit(text2, (rect[0] + 14, rect[1] + 23))
    pygame.display.set_caption(f'score: {score}')
    pygame.display.flip()

pygame.quit()