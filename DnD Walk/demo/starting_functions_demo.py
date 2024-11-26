from time import sleep
from colorama import Fore




# I don't want to type this out every time (or copy-paste)
# better on the fingers to have a tiny function do it
def cont(): 
    input('Press enter to continue')
    print()


def invalid(): # same use as cont()
    print(Fore.RED + 'Invalid Input: Please try again' + Fore.RESET)
    cont()

def confirm(): # used to confirm user input
    while True: # like if they make an important decision
        try:
            print('''Are you sure?
        1.) Yes
        2.) No''')
            sure = int(input())
            if sure not in range(1, 3):
                raise ValueError
        except ValueError:
            invalid()
        else:
            return sure




def rolling(rolling_for = ''): # this is used for drama *jazz hands*
    x =0
    while x <= 3:
        xperiod = x * '.'
        print(f'\rRolling {rolling_for}{xperiod}',end='')
        x += 1
        sleep(1)
    print()

def roll_to_hit(roll, dc, mod): # use this in combat to check if it hit
    rolling('to hit')
    print(f'{roll}')
    if roll + mod >= 20:
        print(Fore.RED + '\n!!!CRITICAL HIT!!!' + Fore.RESET)
        return 'crit'
    elif roll == 1:
        print('\nCritical Fail.')
        return False
    elif roll + mod < dc:
        print('\nFail.')
        return False
    elif roll + mod >= dc:
        print('\nSuccess!')
        return True

def bar(current, total, bar_length = 20): # This is a bar for health and other things (I'll see what I use it for)
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