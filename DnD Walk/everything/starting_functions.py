from random import randint
from time import sleep
from colorama import Fore

def game_over(bool):
    if bool:
        print('Game Over')
        exit()

def cont():
    input('\n' + Fore.GREEN + 'Press enter to continue.' + Fore.RESET)

def invalid():
    print(Fore.RED + 'Invalid Input: Please try again\n' + Fore.RESET)
    cont()

def confirm():
    while True:
        try:
            sure = int(input('''Are you sure?
        1.) Yes
        2.) No\n'''))
        except ValueError:
            invalid()
        else:
            return sure


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
        return f'''{idk}{padding} {round(current)}hp'''
    else:
        return f'''{arrow}{padding} {round(current)}hp'''