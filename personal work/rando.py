# Arden Boettcher
# 10/9/24
# Random Practice

import random
import time
from colorama import Fore

rand1 = int(input('Please enter the floor: '))
rand2 = int(input('Please enter the ceiling: '))
num_of_guesses = 0

try:
    number = random.randint(rand1, rand2)
    guessing = rand1 - 1
except Exception:
    print('Something went wrong. Please check your input.')
    quit()

while guessing != number:
    guessing = random.randint(rand1, rand2)
#    print(f'\nfloor: {rand1}, ceil: {rand2}', end = '') # uncomment this line to see the floor/ceiling
    print(f'\ngoal: {number}, guess: {guessing}')
    num_of_guesses += 1
    if guessing < number:
        rand1 = guessing
        print('Too small!')
    elif guessing > number:
        rand2 = guessing
        print('Too big :/')
    elif guessing == number:
        print(Fore.GREEN + 'You win!')
        if num_of_guesses > 1:
            print(f"it took {num_of_guesses} guesses" + Fore.RESET)
        else:
            print(f'it took {num_of_guesses} guess. Wow!' + Fore.RESET)
        break
    time.sleep(1.5)