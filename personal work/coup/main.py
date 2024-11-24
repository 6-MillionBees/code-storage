# Arden Boettcher
# 11/23/24
# Coup Main

import pygame
from pygame.locals import *
pygame.init()


window = pygame.display.set_mode([500, 500])
pygame.display.set_caption('Coup')

running = True
rect = Rect(200, 200, 50, 50)
number = 0
white = [255, 255, 255]
black = [0, 0, 0]

def outline(rect, color = black):
    outline_rect = rect
    outline_rect = Rect(outline_rect[0], outline_rect[1], outline_rect[2] + 2, outline_rect[3] + 2)
    outline_rect.center = rect.center
    pygame.draw.rect(window, color, outline_rect)

def render_text(words, pos_x, pos_y, size = 50, color = black, rect_color = white):
    font = pygame.font.Font('CascadiaCodeNF.ttf', size)
    text = font.render(str(words), True, color, rect_color)
    text_rect = text.get_rect()
    text_rect.center = [pos_x, pos_y]
    return text, text_rect

while running:
    text1 = render_text(str(number), 250, 250)

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False
            continue

        if event.type == MOUSEBUTTONDOWN:
            if text1[1].collidepoint(event.pos):
                number += 1

    window.fill(white)
    # pygame.draw.rect(window, white, rect)
    outline(text1[1])
    window.blit(text1[0], text1[1])


    pygame.display.flip()

pygame.quit()