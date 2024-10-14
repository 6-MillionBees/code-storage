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

level = 1
difficulty = 1
str_mod = 0
dex_mod = 0
initiative_bonus = 0
player_ac = 10 + dex_mod
player_health = 30
current_player_health = player_health


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

player_equipment = {
    'weapon': 'greataxe'
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

def player_turn(no_of_enemy, enemy1, enemy2, enemy3, enemy4):
    print('Your turn.\n')
    player_turn = int(input('''
    1. Attack
    2. Block\n'''))

    if player_turn == 1:
        while True:
            if no_of_enemy == 1:
                choice = 1
            
            elif no_of_enemy == 2:
                print(f'''Choose who to attack:
    1. {enemy1['name']}
    2. {enemy2['name']}''')
                choice = int(input(''))

            elif no_of_enemy == 3:
                print(f'''Choose who to attack:
    1. {enemy1['name']}
    2. {enemy2['name']}
    3. {enemy3['name']}''')
                choice = int(input(''))

            elif no_of_enemy == 4:
                print(f'''Choose who to attack:
    1. {enemy1['name']}
    2. {enemy2['name']}
    3. {enemy3['name']}
    4. {enemy4['name']}''')
                choice = int(input(''))
            
            if choice == 1:
                print('You attack ' + enemy1['name'] + '\n')
                cont()
                return False, attack(roll_to_hit(d20(), enemy1['ac'], weapon_mod[player_equipment['weapon']]), player_equipment['weapon']), enemy1['name']
                break

            elif choice == 2:
                print('You attack ' + enemy2['name'] + '\n')
                cont()
                return False, attack(roll_to_hit(d20(), enemy2['ac'], weapon_mod[player_equipment['weapon']]), player_equipment['weapon']), enemy2['name']
                break

            elif choice == 3:
                print('You attack ' + enemy3['name'] + '\n')
                cont()
                return False, attack(roll_to_hit(d20(), enemy3['ac'], weapon_mod[player_equipment['weapon']]), player_equipment['weapon']), enemy3['name']
                break

            elif choice == 4:
                print('You attack ' + enemy4['name'] + '\n')
                cont()
                return False, attack(roll_to_hit(d20(), enemy4['ac'], weapon_mod[player_equipment['weapon']]), player_equipment['weapon']), enemy4['name']
                break

            else:
                print('Please enter a valid number.')

    elif player_turn == 2:
        print('You are blocking.')
        return True, 0, enemy1['name']



def fight(no_of_enemy, enemy1, enemy2 = '', enemy3 = '', enemy4 = ''):
    global player_health
    global current_player_health
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



    while no_of_enemy > 0 and player_health > 0:
        blocking = 1
        for turn in list_initiative:
            if turn == 0:

                print(f'''Player Stats
    Level.............{level}
    Current Health....{current_player_health}
    Weapon............''' + player_equipment['weapon'])

                player = player_turn(no_of_enemy, enemy1, enemy2, enemy3, enemy4)
                print(player)

                if player[0] == True:
                    blocking = 2
                elif player[0] == False:
                    blocking = 1
                    if player[2] == enemy1['name']:
                        print(enemy1_health)
                        enemy1_health -= player[1]
                        print(enemy1_health)
                    elif player[2] == enemy2['name']:
                        print(enemy2_health)
                        enemy2_health -= player[1]
                        print(enemy2_health)
                    elif player[2] == enemy3['name']:
                        print(enemy3_health)
                        enemy3_health -= player[1]
                        print(enemy3_health)
                    elif player[2] == enemy4['name']:
                        print(enemy4_health)
                        enemy4_health -= player[1]
                        print(enemy4_health)

                if enemy1_health <= 0 and enemy1_is_alive == True:
                    print(f'You killed ' + enemy1['name'])
                    enemy1_is_alive = False
                    no_of_enemy -= 1
                elif enemy2_health <= 0 and enemy2_is_alive == True:
                    print(f'You killed ' + enemy2['name'])
                    enemy2_is_alive = False
                    no_of_enemy -= 1
                elif enemy3_health <= 0 and enemy3_is_alive == True:
                    print(f'You killed ' + enemy3['name'])
                    enemy3_is_alive = False
                    no_of_enemy -= 1
                elif enemy4_health <= 0 and enemy4_is_alive == True:
                    print(f'You killed ' + enemy4['name'])
                    enemy4_is_alive = False
                    no_of_enemy -= 1
                cont()

            elif turn != 0:
                if str(turn).endswith('1') and enemy1_health > 0:
                    print('It\'s ' + enemy1['name'].title() + '\'s turn\n')
                    roll = d10() + enemy1['agression']
                    if roll > 10:
                        damage = attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy1['weapon']]), enemy1['weapon'])
                        print(f'You took {damage} damage.')
                    elif roll <=10:
                        enemy1_blocking = True
                        damage = 0
                        print(enemy1['name'] + ' is blocking.')
                    current_player_health -= damage
                    cont()

                elif str(turn).endswith('2') and enemy2_health > 0:
                    print('It\'s ' + enemy2['name'].title() + '\'s turn\n')
                    roll = d10() + enemy2['agression']
                    if roll > 10:
                        damage = attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy2['weapon']]), enemy2['weapon'])
                        print(f'You took {damage} damage.')
                    elif roll <=10:
                        enemy2_blocking = True
                        damage = 0
                        print(enemy2['name'] + ' is blocking.')
                    current_player_health -= damage/blocking
                    cont()

                elif str(turn).endswith('3') and enemy3_health > 0:
                    print('It\'s ' + enemy3['name'].title() + '\'s turn\n')
                    roll = d10() + enemy3['agression']
                    if roll > 10:
                        damage = attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy3['weapon']]), enemy3['weapon'])
                        print(f'\nYou took {damage} damage.')
                    elif roll <=10:
                        enemy3_blocking = True
                        damage = 0
                        print(enemy3['name'] + ' is blocking.')
                    current_player_health -= damage
                    cont()

                elif str(turn).endswith('4') and enemy3_health > 0:
                    print('It\'s ' + enemy4['name'].title() + '\'s turn\n')
                    roll = d10() + enemy4['agression']
                    if roll > 10:
                        damage = attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy4['weapon']]), enemy4['weapon'])
                        print(f'\nYou took {damage} damage.')
                    elif roll <=10:
                        enemy4_blocking = True
                        damage = 0
                        print(enemy4['name'] + ' is blocking.')
                    current_player_health -= damage
                    cont()
    if current_player_health <= 0:
        print('You died.')
        return 0
    elif no_of_enemy == 0:
        print('You won!')
        return 1

fight(2, greg, goblin)