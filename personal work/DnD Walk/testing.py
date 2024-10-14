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
    return roll


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
initiative_bonus = 0
player_ac = 10 + dex_mod


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
    'name': 'Goblin',
    'health': d6(2) * difficulty, 'weapon': 'dagger', 'ac': 10, 'xp': 50, 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1
}

greg = {
    'name': 'Greg',
    'health': d4(10) * difficulty, 'weapon': 'maul', 'ac': 15, 'xp': 200, 'agression': 3,
    'str mod': 4, 'dex mod': -1, 'end mod': 3, 'int mod': -2, 'wis mod': -1, 'cha mod': 1
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
    if tohit == 'crit':
        print('\nCritical Hit!')
        return weapon_damage[weapon] + weapon_mod[weapon] * 2
    elif tohit == True:
        print('\nAttack hit.')
        return weapon_damage[weapon] + weapon_mod[weapon]
    elif tohit == False:
        print('\nAttack missed.')
        return 0
    else:
        print('\nAttack missed.')
        return 0

playerhealth = 30

def fight(enemy1, enemy2 = '', enemy3 = '', enemy4 = ''):
    global playerhealth
    rolling('initiative')
    player_initiative = d20() + dex_mod + initiative_bonus
    initiative = {player_initiative: 0}
    print(f'\nYou rolled a {player_initiative}')

    initiative[d20() + enemy1['dex mod']] = enemy1['name']+'1'
    enemy1_health = enemy1['health']
    if enemy2 != '':
        initiative[d20() + enemy2['dex mod']] = enemy2['name']+'2'
        enemy2_health = enemy2['health']
    if enemy3 != '':
        initiative[d20() + enemy3['dex mod']] = enemy3['name']+'3'
        enemy3_health = enemy3['health']
    if enemy4 != '':
        initiative[d20() + enemy4['dex mod']] = enemy4['name']+'4'
        enemy4_health = enemy4['health']
    print(initiative)
    list_initiative = list(initiative.keys())
    list_initiative.sort(reverse= True)
    initiative = {item: initiative[item] for item in list_initiative}
    print(initiative)
    list_initiative = list(initiative.values())
    print(list_initiative)
    if enemy2 == '':
        no_of_enemy = 1
    elif enemy3 == '':
        no_of_enemy = 2
    elif enemy4 == '':
        no_of_enemy = 3
    else:
        no_of_enemy = 4

    while no_of_enemy > 0 and playerhealth > 0:
        for turn in list_initiative:
            if turn == 0:
                print('doing this later')
                cont()
            elif turn != 0:
                if str(turn).endswith('1'):
                    print('It\'s ' + enemy1['name'].title() + '\'s turn\n')
                    roll = d10() + enemy1['agression']
                    if roll > 10:
                        damage = attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy1['weapon']]), enemy1['weapon'])
                        print(f'You took {damage} damage.')
                    elif roll <=10:
                        enemy1_blocking = True
                        damage = 0
                        print(f'\n{enemy1['name']} is blocking.')
                    playerhealth -= damage
                    cont()

                elif str(turn).endswith('2'):
                    print('It\'s ' + enemy2['name'].title() + '\'s turn\n')
                    roll = d10() + enemy2['agression']
                    if roll > 10:
                        damage = attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy2['weapon']]), enemy2['weapon'])
                        print(f'You took {damage} damage.')
                    elif roll <=10:
                        enemy2_blocking = True
                        damage = 0
                        print(f'\n{enemy2['name']} is blocking.')
                    playerhealth -= damage
                    cont()

                elif str(turn).endswith('3'):
                    print('It\'s ' + enemy3['name'].title() + '\'s turn\n')
                    roll = d10() + enemy3['agression']
                    if roll > 10:
                        damage = attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy3['weapon']]), enemy3['weapon'])
                        print(f'\nYou took {damage} damage.')
                    elif roll <=10:
                        enemy3_blocking = True
                        damage = 0
                        print(f'\n{enemy3['name']} is blocking.')
                    playerhealth -= damage
                    cont()

                elif str(turn).endswith('4'):
                    print('It\'s ' + enemy4['name'].title() + '\'s turn\n')
                    roll = d10() + enemy4['agression']
                    if roll > 10:
                        damage = attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy4['weapon']]), enemy4['weapon'])
                        print(f'\nYou took {damage} damage.')
                    elif roll <=10:
                        enemy4_blocking = True
                        damage = 0
                        print(f'\n{enemy4['name']} is blocking.')
                    playerhealth -= damage
                    cont()
    
    if playerhealth <= 0:
        print('')




fight(greg, goblin)