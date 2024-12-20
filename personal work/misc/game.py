# Arden Boettcher
# 11/15/24
# Pygame Practice

from random import randint
import pygame
from pygame.locals import *
pygame.init()


X = 400
Y = 400
width = 50
height = 50
screen = pygame.display.set_mode((X, Y))

rect1 = Rect(300, 80, width, height)
rect2 = Rect(200, 80, width, height)
rect3 = Rect(100, 80, width, height)

rect1_hit = False
rect2_hit = False
rect3_hit = False


menu_basic_triple = Rect(100, 200, 200, 50)
menu_triple_combo = Rect(100, 275, 200, 50)

running = True
score = 0

# Colors
white = (255, 255, 255)

font = pygame.font.Font('CascadiaCodeNF.ttf', 15)
text1_rect1 = font.render('click', True, white, None)
text2_rect1 = font.render('me!', True, white, None)
text1_rect2 = font.render('click', True, white, None)
text2_rect2 = font.render('me!', True, white, None)
text1_rect3 = font.render('click', True, white, None)
text2_rect3 = font.render('me!', True, white, None)

text_triple_combo = font.render('Triple Combo', True, white, None)
text_basic_triple = font.render('Basic Triple', True, white, None)

gamemode = None

red = (255, 0, 0)

while running:

    if gamemode == 'triple combo':
        if rect1_hit and rect2_hit and rect3_hit:
            rect1 = Rect(randint(0, X - width), randint(0, Y - height), width, height)
            rect2 = Rect(randint(0, X - width), randint(0, Y - height), width, height)
            rect3 = Rect(randint(0, X - width), randint(0, Y - height), width, height)

            rect1_hit = False
            rect2_hit = False
            rect3_hit = False

        for event in pygame.event.get():

            if event.type == QUIT:
                print(score)
                running = False

            elif event.type == MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    score += 1
                    rect1[0] = 1000
                    rect1_hit = True

                elif rect2.collidepoint(event.pos):
                    score += 1
                    rect2[0] = 1000
                    rect2_hit = True

                elif rect3.collidepoint(event.pos):
                    score += 1
                    rect3[0] = 1000
                    rect3_hit = True

        screen.fill((127,127,127))

        pygame.draw.rect(screen, red, rect1)
        screen.blit(text1_rect1, (rect1[0] + 3, rect1[1] + 9))
        screen.blit(text2_rect1, (rect1[0] + 14, rect1[1] + 23))

        pygame.draw.rect(screen, red, rect2)
        screen.blit(text1_rect2, (rect2[0] + 3, rect2[1] + 9))
        screen.blit(text2_rect2, (rect2[0] + 14, rect2[1] + 23))

        pygame.draw.rect(screen, red, rect3)
        screen.blit(text1_rect3, (rect3[0] + 3, rect3[1] + 9))
        screen.blit(text2_rect3, (rect3[0] + 14, rect3[1] + 23))

        pygame.display.set_caption(f'score: {score}')
        pygame.display.flip()
        continue


    elif gamemode == 'basic triple':
        for event in pygame.event.get():

            if event.type == QUIT:
                print(score)
                running = False
                

            elif event.type == MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    score += 1
                    rect1 = Rect(randint(0, X - width), randint(0, Y - height), width, height)
                elif rect2.collidepoint(event.pos):
                    score += 1
                    rect2 = Rect(randint(0, X - width), randint(0, Y - height), width, height)
                elif rect3.collidepoint(event.pos):
                    score += 1
                    rect3 = Rect(randint(0, X - width), randint(0, Y - height), width, height)

            # elif event.type == MOUSEMOTION:
            #     mouse_pos = pygame.mouse.get_pos()
            #     print(f'({mouse_pos[0]}, {mouse_pos[1]})')
            #     rect = Rect(mouse_pos[0], mouse_pos[1], 50, 60)

        screen.fill((127,127,127))

        pygame.draw.rect(screen, red, rect1)
        screen.blit(text1_rect1, (rect1[0] + 3, rect1[1] + 9))
        screen.blit(text2_rect1, (rect1[0] + 14, rect1[1] + 23))

        pygame.draw.rect(screen, red, rect2)
        screen.blit(text1_rect2, (rect2[0] + 3, rect2[1] + 9))
        screen.blit(text2_rect2, (rect2[0] + 14, rect2[1] + 23))

        pygame.draw.rect(screen, red, rect3)
        screen.blit(text1_rect3, (rect3[0] + 3, rect3[1] + 9))
        screen.blit(text2_rect3, (rect3[0] + 14, rect3[1] + 23))

        pygame.display.set_caption(f'score: {score}')
        pygame.display.flip()
        continue

    for event in pygame.event.get():

        if event.type == QUIT:
            running = False
            continue

        elif event.type == MOUSEBUTTONDOWN:
            if menu_basic_triple.collidepoint(event.pos):
                gamemode = 'basic triple'
            elif menu_triple_combo.collidepoint(event.pos):
                gamemode = 'triple combo'



    screen.fill((127,127,127))
    pygame.draw.rect(screen, red, menu_basic_triple)
    screen.blit(text_basic_triple, (menu_basic_triple[0] + 50, menu_basic_triple[1] + 15))

    pygame.draw.rect(screen, red, menu_triple_combo)
    screen.blit(text_triple_combo, (menu_triple_combo[0] + 50, menu_triple_combo[1] + 15))

    pygame.display.flip()


pygame.quit()