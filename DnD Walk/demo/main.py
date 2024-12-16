# Arden Boettcher
# 11/26/24
# DnD walk demo (for class)

from time import sleep

from dice import *
from default_functions import *


# Getting this out of the way from the start:
# This is a demo for a project I've been working on for 2, almost 3, months
# Most of this code is copied from the main thing and was probably written a month ago
# Though a bunch of the important stuff is quite recent

# For example these are some recent things:
# Everything to do with spells
# Map navigation & generation
# The entire gameplay loop

# You might notice that there are multiple files
# This decision caused me so many problems and it was not worth it
# It might've been a little worth it solely for the learning experience
# Programming :D


name = input(Fore.GREEN +'\nWhat is your name?\n' + Fore.RESET)
name_title = name.title()

print()
print(Fore.GREEN + 'Welcome ' + name_title + '! To my RPG demo!')
print('I\'d say it\'s pretty good (I am very biased)' + Fore.RESET)
print()

cont()

print('To start we\'re going to assign your stats (this is permenent)')


import player_stats as player

print('Total Health: ', player.player_health)
print('Current Health: ', player.current_player_health)
cont()

from world import make_dungeon

dungeon = make_dungeon()
print(f'you are here > {Fore.GREEN}+{Fore.RESET}')
player_is_alive = True

import world as w

w.player_equipment['equipped weapon'] = 'handaxe'

w.fight(w.slime, w.slime, w.slime, w.slime)

while player_is_alive:

    w.print_dungeon(dungeon)
    dungeon = w.movement_menu(dungeon)
    print()
    effects = w.dungeon_effects(dungeon)
    cont()

    if player.player_exp >= player.exp_needed:
        player.level_up()

    if effects == True:
        dungeon = make_dungeon()
        rested = False

    from world import player_is_alive


from items import player_equipment
score = w.dun_level * 1000 + round(player_equipment['copper pieces'] * 0.1) + player_equipment['silver pieces'] * 10 + player_equipment['gold pieces'] * 1000

print(f'''Score:
Dungeon Floors ({w.dun_level}): {w.dun_level * 1000}
Coins (c:{player_equipment['copper pieces']}, s:{player_equipment['silver pieces']}, g: {player_equipment['gold pieces']}): {player_equipment['copper pieces'] + player_equipment['silver pieces'] * 100 + player_equipment['gold pieces'] * 1000}
Level({player.level}): {player.level * 100}
difficulty({w.difficulty}): {w.difficulty * 1000}

Total: {score}''')


print()