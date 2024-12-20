# Arden Boettcher
# 12/2/24
# NPC Stats

from random import randint
from dice import *
from items import *
from world import luck_mod, difficulty

# Enemies

# Basic
goblin = {
    'name': 'Goblin', 'title': '', 'caster': False,
    'health': (lambda: int((d6(1) + 6) * difficulty)), 'weapon': 'dagger', 'ac': 5,
    'exp': int(50), 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1,
    'score': 20
}

kobold = {
    'name': 'Kobold', 'title': '', 'caster': False,
    'health': (lambda: int((d4(4) - 2))), 'weapon': 'dagger', 'ac': 7,
    'exp': int(25), 'agression': 4,
    'str mod': -2, 'dex mod': 2, 'end mod': -1, 'int mod': -1, 'wis mod': -2, 'cha mod': -1,
    'score': 20
}

slime = {
    'name': 'Slime', 'title': '', 'caster': False,
    'health': (lambda: int(d4(2))), 'weapon': 'slime', 'ac': 6,
    'exp': int(26), 'agression': 20,
    'str mod': -4, 'dex mod': -3, 'end mod': 5, 'int mod': -5, 'wis mod': -5, 'cha mod': 1,
    'score': 10
}

la_creatura = {
    'name': 'La Creatura', 'title': '',
    'health': (lambda: int(d4(8))), 'weapon': 'sickle', 'ac': 0,
    'exp': int(50), 'agrssion': 20,
    'str mod': 3, 'dex mod': -2, 'end mod': 4, 'int mod': -3, 'wis mod': -2, 'cha mod': -1,
    'score': 30
}


# Named

lily = {
    'name': 'Lily', 'title': '',
    'health': (lambda: d6(3) + 10), 'weapon': 'lilys staff', 'ac': 8, 'exp': 250, 'agression': 0,
    'str mod': 0, 'dex mod': 1, 'end mod': 1, 'int mod': 3, 'wis mod': 2, 'cha mod': 1,
    'casting mod': 3,
    'spells': 'firebolt'
}

kile = {
    'name': 'Kile', 'title': ', With An I',
    'health': (lambda: d4(4) + 20), 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1,
    'casting mod': 0
}

kyle = {
    'name': 'Kyle', 'title': ', With A Y',
    'health': (lambda: d4(4) + 20), 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1,
    'casting mod': 0
}

gronk = {
    'name': 'Gronk', 'title': ', The Killer', 'caster': False,
    'health': (lambda: d6(4) + 20), 'weapon': 'maul', 'ac': 13, 'exp': 200, 'agression': 3,
    'str mod': 4, 'dex mod': -1, 'end mod': 3, 'int mod': -2, 'wis mod': -1, 'cha mod': 0,
    'casting mod': 0
}

siffrin_traveler = {
    'name': 'Siffrin', 'title': ', The Traveler', 'caster': False,
    'health': (lambda: 50), 'weapon': 'dagger', 'ac': 13, 'exp': 500, 'agression': 6,
    'str mod': 0, 'dex mod': 5, 'end mod': 2, 'int mod': 1, 'wis mod': -1, 'cha mod': 2,
    'casting mod': 0
}

siffrin_lost = {
    'name': 'Siffrin', 'title': ', The Lost', 'caster': False,
    'health': (lambda: 999), 'weapon': 'sif dagger', 'ac': 15, 'exp': 9999, 'agression': 10,
    'str mod': 0, 'dex mod': 6, 'end mod': 3, 'int mod': 0, 'wis mod': -2, 'cha mod': 1,
    'casting mod': 0
}

dangolf = {
    'name': 'Dangolf', 'title': ', The Gold',
    'health': (lambda: 150), 'weapon': 'dangolf staff', 'ac': 10, 'exp': 1000, 'agression': 2,
    'str mod': -2, 'dex mod': -2, 'end mod': 2, 'int mod': 5, 'wis mod': 10, 'cha mod': 2,
    'casting mod': 0
}

godwin = {
    'name': 'Godwin', 'title': ', The Golden',
    'health': (lambda: 30), 'weapon': 'golden spirit', 'ac': 12, 'exp': 2000, 'agression': -3,
    'str mod': 5, 'dex mod': 2, 'end mod': 4, 'int mod': 1, 'wis mod': 2, 'cha mod': 10,
    'casting mod': 0
}

