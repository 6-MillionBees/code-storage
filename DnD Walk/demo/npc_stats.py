# Arden Boettcher
# 12/2/24
# NPC Stats

from random import randint

from dice import *
from world import luck, luck_mod, difficulty
from items import *



lily_spells = []

# Enemies

# Basic
goblin = {
    'name': 'Goblin', 'title': '', 'caster': False,
    'health': int(d6(1) + 6 * difficulty), 'weapon': 'dagger', 'ac': 5, 'exp': 50, 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1,
    'casting mod': 0
}

kobold = {
    'name': 'Kobold', 'title': '', 'caster': False,
    'health': int((d4(4) - 2) * difficulty), 'weapon': 'dagger', 'ac': 7, 'exp': 25, 'agression': 4,
    'str mod': -2, 'dex mod': 2, 'con mod': -1, 'int mod': -1, 'wis mod': -2, 'cha mod': -1,
    'casting mod': 0
}


# Named

lily = {
    'name': 'Lily', 'title': '', 'caster': True,
    'health': d6(3) + 10, 'weapon': 'staff', 'ac': 8, 'exp': 250, 'agression': 0,
    'str mod': 0, 'dex mod': 1, 'end mod': 1, 'int mod': 3, 'wis mod': 2, 'cha mod': 1,
    'casting mod': 3,
    'spells': lily_spells
}

kile = {
    'name': 'Kile', 'title': ', With An I', 'caster': False,
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
    'health': 60, 'weapon': 'golden spirit', 'ac': 12, 'exp': 2000, 'agression': -3,
    'str mod': 5, 'dex mod': 2, 'end mod': 4, 'int mod': 1, 'wis mod': 2, 'cha mod': 10,
    'casting mod': 0
}



# loot tables

def item_pickup(items):
    global player_equipment
    for item, numbers in items:
        player_equipment[item] += numbers


def common_table(no_of_items):
    drops = []
    numbers = []
    num = 0
    while num < no_of_items:
        rand = randint(1, 100) + luck_mod()
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
            drops.append('rocks')
            numbers.append(1)
        elif rand > 75 and rand < 97:
            drops.append('rope')
            numbers.append(randint(25, 75))
        elif rand > 97:
            drops.append('gold pieces')
            numbers.append(1)
        num += 1
    return zip(drops, numbers), # unique_items



uncommon_table = [
    'arrows5', 'arrows5', 
]
