from dice import *
goblin = {
    'name': 'Goblin', 'title': '', 'caster': False,
    'health': (lambda: int(d6(1))), 'weapon': 'dagger', 'ac': 5,
    'exp': int(50), 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1,
    'score': 20
}

enemy1 = goblin
enemy2 = goblin
enemy3 = goblin
enemy4 = goblin
player_dict = {'initiative': 0, 'name': 'You'}
player_mods = {'dex mod': 1}
initiative_bonus = 0


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

no_of_enemy = 1
enemy1_is_alive = True
enemy1_health = enemy1['health']()
initiative.insert(randint(0, len(initiative)), enemy1)

if enemy2 != '':
    enemy2_is_alive = True
    enemy2_health = enemy2['health']()
    no_of_enemy += 1
    initiative.insert(randint(0, len(initiative)), enemy2)


if enemy3 != '':
    enemy3_is_alive = True
    enemy3_health = enemy3['health']()
    no_of_enemy += 1
    initiative.insert(randint(0, len(initiative)), enemy3)

if enemy4 != '':
    enemy4_is_alive = True
    enemy4_health = enemy4['health']()
    no_of_enemy += 1
    initiative.insert(randint(0, len(initiative)), enemy4)



initiative.insert(randint(0, len(initiative) - player_mods['dex mod'] / ), player_dict)

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