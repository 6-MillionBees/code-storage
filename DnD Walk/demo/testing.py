from random import randint
from default_functions import rolling
from dice import *

player_dict = {'initiative': 0, 'name': 'You'}

goblin = {
    'name': 'Goblin', 'title': '', 'caster': False,
    'health': (lambda: int(d6(1) + 6)), 'weapon': 'dagger', 'ac': 5,
    'exp': int(50), 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1,
    'score': 20
}


no_of_turns = 0
exp = 0

initiative = []

enemy2_is_alive = False
enemy3_is_alive = False
enemy4_is_alive = False
enemy1_blocking = 1
enemy2_blocking = 1
enemy3_blocking = 1
enemy4_blocking = 1
enemy2_health = 0
enemy3_health = 0
enemy4_health = 0




enemy1 = goblin
enemy1['name'] = enemy1['name'] + ' 1'
print(enemy1)
no_of_enemy = 1
enemy1_is_alive = True
enemy1_health = enemy1['health']()
initiative.insert(randint(0, len(initiative)), enemy1)

print(goblin)

if goblin != '':
    enemy2 = goblin
    enemy2['name'] = enemy2['name'] + ' 2'
    print(enemy1)
    print(enemy2)
    enemy2_is_alive = True
    enemy2_health = enemy2['health']()
    no_of_enemy += 1
    initiative.insert(randint(0, len(initiative)), enemy2)

print(goblin)

if goblin != '':
    enemy3 = goblin
    enemy3['name'] = enemy3['name'] + ' 3'
    print(enemy1)
    print(enemy2)
    print(enemy3)
    enemy3_is_alive = True
    enemy3_health = enemy3['health']()
    no_of_enemy += 1
    initiative.insert(randint(0, len(initiative)), enemy3)

print(goblin)

if goblin != '':
    enemy4 = goblin
    enemy4['name'] = enemy4['name'] + ' 4'
    print(enemy1)
    print(enemy2)
    print(enemy3)
    print(enemy4)
    enemy4_is_alive = True
    enemy4_health = enemy4['health']()
    no_of_enemy += 1
    initiative.insert(randint(0, len(initiative)), enemy4)

initiative.insert(randint(0, len(initiative)), player_dict)

print()
print('Initiative Order:')
initiative_print_num = 0
for turn in initiative:
    if initiative_print_num == 0:
        print(turn['name'], end = '')
        initiative_print_num += 1
    else:
        print(f', {turn["name"]}', end = '')
print()