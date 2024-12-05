# Arden Boettcher
# 12/2/24
# NPC Stats

from random import randint

from dice import *
from world import difficulty as difficulty_silly
from world import luck_mod as luck_mod_var
from items import *



# Enemies

# Basic
goblin = {
    'name': 'Goblin', 'title': '', 'caster': False,
    'health': (lambda: int(d6(1) + 6 * difficulty_silly)), 'weapon': 'dagger', 'ac': 5,
    'exp': int(50 * difficulty_silly), 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1,
    'score': 20
}

kobold = {
    'name': 'Kobold', 'title': '', 'caster': False,
    'health': (lambda: int((d4(4) - 2) * difficulty_silly)), 'weapon': 'dagger', 'ac': 7,
    'exp': int(25 * difficulty_silly), 'agression': 4,
    'str mod': -2, 'dex mod': 2, 'con mod': -1, 'int mod': -1, 'wis mod': -2, 'cha mod': -1,
    'score': 20
}

slime = {
    'name': 'Slime', 'title': '', 'caster': False,
    'health': (lambda: int(d4(2) * difficulty_silly)), 'weapon': 'dagger', 'ac': 6,
    'exp': int(26 * difficulty_silly), 'agression': 20,
    'str mod': -4, 'dex mod': -3, 'con mod': 5, 'int mod': -5, 'wis mod': -5, 'cha mod': 1,
    'score': 10
}

la_creatura = {
    'name': 'La Creatura', 'title': '',
    'health': (lambda: int(d4(8) * difficulty_silly)), 'weapon': 'sickle', 'ac': 0,
    'exp': int(50 * difficulty_silly), 'agrssion': 20,
    'str mod': 3, 'dex mod': -2, 'con mod': 4, 'int mod': -3, 'wis mod': -2, 'cha mod': -1,
    'score': 30
}


# Named

lily = {
    'name': 'Lily', 'title': '', 
    'health': d6(3) + 10, 'weapon': 'staff', 'ac': 8, 'exp': 250, 'agression': 0,
    'str mod': 0, 'dex mod': 1, 'end mod': 1, 'int mod': 3, 'wis mod': 2, 'cha mod': 1,
    'casting mod': 3,
    'spells': 'firebolt'
}

kile = {
    'name': 'Kile', 'title': ', With An I', 
    'health': d4(4) + 20, 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1,
    'casting mod': 0
}

kyle = {
    'name': 'Kyle', 'title': ', With A Y',
    'health': d4(4) + 20, 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1,
    'casting mod': 0
}

gronk = {
    'name': 'Gronk', 'title': ', The Killer', 'caster': False,
    'health': d6(4) + 20, 'weapon': 'maul', 'ac': 13, 'exp': 200, 'agression': 3,
    'str mod': 4, 'dex mod': -1, 'end mod': 3, 'int mod': -2, 'wis mod': -1, 'cha mod': 0,
    'casting mod': 0
}

siffrin_traveler = {
    'name': 'Siffrin', 'title': ', The Traveler', 'caster': False,
    'health': 50, 'weapon': 'dagger', 'ac': 13, 'exp': 500, 'agression': 6,
    'str mod': 0, 'dex mod': 5, 'end mod': 2, 'int mod': 1, 'wis mod': -1, 'cha mod': 2,
    'casting mod': 0
}

siffrin_lost = {
    'name': 'Siffrin', 'title': ', The Lost', 'caster': False,
    'health': 999, 'weapon': 'sif dagger', 'ac': 15, 'exp': 9999, 'agression': 10,
    'str mod': 0, 'dex mod': 6, 'end mod': 3, 'int mod': 0, 'wis mod': -2, 'cha mod': 1,
    'casting mod': 0
}

dangolf = {
    'name': 'Dangolf', 'title': ', The Gold',
    'health': 150, 'weapon': 'dangolf staff', 'ac': 10, 'exp': 1000, 'agression': 2,
    'str mod': -2, 'dex mod': -2, 'end mod': 2, 'int mod': 5, 'wis mod': 10, 'cha mod': 2,
    'casting mod': 0
}

godwin = {
    'name': 'Godwin', 'title': ', The Golden',
    'health': 30, 'weapon': 'golden spirit', 'ac': 12, 'exp': 2000, 'agression': -3,
    'str mod': 5, 'dex mod': 2, 'end mod': 4, 'int mod': 1, 'wis mod': 2, 'cha mod': 10,
    'casting mod': 0
}



# loot tables

def item_pickup(items):
    global player_equipment
    for item, numbers in items:
        player_equipment[item] += numbers
        print(f'You picked up {numbers} {item}')


def common_table(no_of_items, enemy):
    drops = []
    numbers = []
    num = 0
    if enemy == dangolf:
        pickupweapon('dangolf staff')

    while num < no_of_items:
        rand = randint(1, 100) + luck_mod_var()
        if rand < 30:
            drops.append('copper pieces')
            numbers.append(randint(30, 90))
        elif rand > 30 and rand < 50:
            drops.append('arrows')
            numbers.append(randint(1, 10))
        elif rand > 50 and rand < 60:
            drops.append('silver pieces')
            numbers.append(randint(1, 5))
        elif rand > 60 and rand < 75:
            drops.append('health potion')
            numbers.append(1)
        elif rand > 75 and rand < 97:
            drops.append('rope')
            numbers.append(randint(25, 75))
        elif rand > 97:
            drops.append('gold pieces')
            numbers.append(1)
        num += 1
    return zip(drops, numbers), # unique_items