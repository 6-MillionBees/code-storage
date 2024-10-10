# Arden boettcher
# 10/10/24
# dnd walk testing

import time
import random

def d100(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 100)
    return roll
def d20(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 20)
    return roll
def d12(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 12)
    return roll
def d10(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 10)
    return roll
def d8(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 8)
    return roll
def d6(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 6)
    return roll
def d4(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 4)

def cont():
    input('\nPress enter to continue.\n')
def roll_to_hit(roll, dc, mod):
    x =0
    while x <= 3:
        xperiod = x * '.'
        print(f'\rRolling{xperiod}',end='')
        x += 1
        time.sleep(1)
    if roll == 20:
        print('\nNATURAL 20!')
        return 'crit'
    elif roll == 1:
        print('\nCritical Fail.')
        return False
    elif roll + mod < dc:
        print('\nfailed.')
        return False
    elif roll + mod >= dc:
        print('\nSuccess!')
        return True

difficulty = 1
str_mod = 0
dex_mod = 0

weapon_damage = {
    'club': d4(), 'dagger': d4(), 'great club': d10(), 'javelin': d6(), 'light hammer': d4(),
    'mace': d6(), 'quarterstaff': d8(), 'sickle': d4(), 'spear': d6(), 'battle axe': d8(),
    'flail': d8(), 'glaive': d10(), 'greataxe': d12(), 'greatsword': d6(2), 'halberd': d10(),
    'handaxe': d6(), 'lance': d8(), 'longsword': d8(), 'maul': d6(2), 'morningstar': d8(),
    'pike': d10(), 'rapier': d8(), 'scimitar': d6(), 'shortsword': d6(), 'trident': d8(),
    'war pick': d8(), 'warhammer': d8(), 'whip': d4()
}

weapon_mod = {
    'club': str_mod, 'dagger': dex_mod, 'great club': str_mod, 'javelin': str_mod, 'light hammer': str_mod,
    'mace': str_mod, 'quarterstaff': str_mod, 'sickle': str_mod, 'spear': str_mod, 'battle axe': str_mod,
    'flail': str_mod, 'glaive': str_mod, 'greataxe': str_mod, 'greatsword': str_mod, 'halberd': str_mod,
    'handaxe': str_mod, 'lance': str_mod, 'longsword': str_mod, 'maul': str_mod, 'morningstar': str_mod,
    'pike': str_mod, 'rapier': dex_mod, 'scimitar': dex_mod, 'shortsword': dex_mod, 'trident': str_mod,
    'war pick': str_mod, 'warhammer': str_mod, 'whip': dex_mod
}

goblin = {
    'health': d6(2) * difficulty, 'weapon1': 'dagger', 'weapon2': 'shortsword', 'weapon3': 'sickle', 'xp': 50,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1
}

def rolling(rolling_for = ''):
    x =0
    while x <= 3:
        xperiod = x * '.'
        if rolling_for == '':
            print(f'\rRolling{xperiod}',end='')
        else:
            print(f'\rRolling for {rolling_for}{xperiod}',end='')
        x += 1
        time.sleep(1)

def attack(tohit, weapon):
    rolling('damage')
    if tohit == 'crit':
        print('\nCritical Hit!')
        return weapon_damage[weapon] + weapon_mod[weapon] * 2
    elif tohit == True:
        print('\nYour attack hit.')
        return weapon_damage[weapon] + weapon_mod[weapon]
    elif tohit == False:
        print('\nYou missed.')
        return 0
    else:
        print('\nYou missed.')
        return 0

def fight(no_of_enemy1, enemy_type1, no_of_enemy2 = 0, enemy_type2 = '', no_of_enemy3 = 0, enemy_type3 = ''):
    rolling('initiative')
    initiative = {'player_in': d20() + dex_mod, }
    print(f'you rolled a {initiative['player_in']}')

    for x in range(1, no_of_enemy1 + 1):
        initiative['{0}'.format(x)] = d20() + enemy_type1['dex mod']
    if no_of_enemy2 > 0:
        for x in range(1, no_of_enemy2 + 1):
            initiative['{0}'.format(x)] = d20() + enemy_type2['dex mod']
    if no_of_enemy3 > 0:
        for x in range(1, no_of_enemy3 + 1):
            initiative['{0}'.format(x)] = d20() + enemy_type3['dex mod']
    
    initiative = list(initiative).sort

    while no_of_enemy1 > 0:
        
