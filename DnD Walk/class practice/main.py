# Arden Boettcher
# 11/26/24
# DnD walk demo (for class)

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
# The Class "player"
# A lot

# You might notice that there are multiple files
# This was a decision I made and I regret it at all times
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

from player_stats import player

user = player(3)
user.define_stats()

user.mods['cha']
print('Total Health: ', user.health)
print('Current Health: ', user.current_health)
cont()



from world import make_dungeon



dungeon = make_dungeon()
print(f'you are here > {Fore.GREEN}+{Fore.RESET}')



import world as w

user.equipment['equipped weapon'] = 'handaxe'

w.fight(w.slime, w.slime, w.slime, w.slime)

while user.isalive:

    w.print_dungeon(dungeon)
    dungeon = w.movement_menu(dungeon)
    print()
    effects = w.dungeon_effects(dungeon)
    cont()

    if user.current_exp >= user.needed_exp:
        user.level_up()

    if effects == True:
        dungeon = make_dungeon()
        rested = False

user.count_coints()

score = w.dun_level * 1000 + round(user.equipment['copper pieces'] * 0.1) + user.equipment['silver pieces'] * 10 + user.equipment['gold pieces'] * 1000

print(f'''Score:
Dungeon Floors ({w.dun_level}): {w.dun_level * 1000}
Coins (c:{user.equipment['copper pieces']}, s:{user.equipment['silver pieces']}, g: {user.equipment['gold pieces']}): {user.equipment['copper pieces'] + user.equipment['silver pieces'] * 100 + user.equipment['gold pieces'] * 1000}
Level({player.level}): {player.level * 100}
difficulty({w.difficulty}): {w.difficulty * 1000}

Total: {score}''')


print()