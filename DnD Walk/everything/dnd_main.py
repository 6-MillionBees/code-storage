# Arden Boettcher
# Start: 10/9/24
# A Hike Through The Woods

import random
from colorama import Fore
from colorama import Back
from time import sleep

from starting_functions import cont, invalid, confirm, rolling

# Dice
from dice import *



days = 0
difficulty = 1 + days / 25


name = input(Fore.GREEN +'\nWhat is your name?\n' + Fore.RESET)



from player_stats import define_class

player_class = define_class()



print('Please assign your stats')
cont()

from player_stats import define_stats

stats = define_stats()

from player_stats import player_mods, initiative_bonus

print(f'''
str mod: {player_mods["str mod"]}
dex mod: {player_mods["dex mod"]}
end mod: {player_mods["end mod"]}
int mod: {player_mods["int mod"]}
wis mod: {player_mods["wis mod"]}
cha mod: {player_mods["cha mod"]}''')

print(initiative_bonus)
cont()





# Chances & encounters
from player_stats import *
from chances import *
from world import *

while distance > distance_traveled:
    # if d20() <= 10:
    #     is_encounter = True
    # else:
    #     is_encounter = False
    # if d20() >= 10:
    #     is_chance = True
    # else:
    #     is_chance = False
    is_chance = True # REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING
    is_encounter = False # REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING

    if is_chance == True and is_encounter == True:
        roll_enocounter = d100()
        roll_chance = d100()

    elif is_encounter == True:
        roll_encounter = d100()

    elif is_chance == True:
        roll_chance = d100()
        roll_chance = 1 # REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING

        if roll_chance == 1 and chance[1] == False:
            chance1()

        elif roll_chance == 1 and chance[1] == True:
            roll_chance = 90 + d10()
        elif roll_chance == 2 and chance[2] == False:
            print('work in progress')