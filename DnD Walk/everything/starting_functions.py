from random import randint
from time import sleep
from colorama import Fore





def cont():
    input('Press enter to continue')



    # while True:
    #     font = pygame.font.Font('CascadiaCodeNF.ttf', 25)
    #     text = font.render('', True, black, white)
    #     text_rect = text.get_rect()
    #     text_rect.center = [center, center - 50]
    #     screen.blit(text, text_rect)
    #     for event in pygame.event.get():
    #         if event == MOUSEBUTTONDOWN:
    #             if text_rect.collidepoint(event.pos):
    #                 break


def invalid():
    print(Fore.RED + 'Invalid Input: Please try again\n' + Fore.RESET)
    cont()

def confirm():
    while True:
        try:
            print('''Are you sure?
        1.) Yes
        2.) No\n''')
            sure = int(input())
            if sure in range(1, 3):
                raise ValueError
        except ValueError:
            invalid()
        else:
            return sure



def int_input(words):
    while True:
        try:
            choice = int(input(words))
        except ValueError:
            invalid()
            continue
        else:
            break
    return choice


def rolling(rolling_for = ''):
    x =0
    while x <= 3:
        xperiod = x * '.'
        print(f'\rRolling {rolling_for}{xperiod}',end='')
        x += 1
        sleep(1)
    print()

def roll_to_hit(roll, dc, mod):
    rolling('to hit')
    print(f'{roll}')
    if roll + mod >= 20:
        print(Fore.RED + '\nCRITICAL HIT' + Fore.RESET)
        return 'crit'
    elif roll == 1:
        print('\nCritical Fail.')
        return False
    elif roll + mod < dc:
        print('\nfailed.')
        return False
    elif roll + mod >= dc:
        print('\nSuccess!')
        return True

def bar(current, total, bar_length = 20):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '█' + '▒'
    idk = int(fraction * bar_length) * '█'
    padding = int(bar_length - len(arrow)) * '-'
    if fraction >= .99:
        return f'{idk}{padding} {round(current)}hp'
    else:
        return f'{arrow}{padding} {round(current)}hp'


# WIP
# from player_stats import *
# from spells import *

# def rest():
#     print('working on it')