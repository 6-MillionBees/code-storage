# Arden Boettcher
# Start: 10/9/24
# A Hike Through The Woods

import random
from colorama import Fore
from colorama import Back
import time


# Dice

def d100(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 100)
    return roll

def d69(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 69)
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


chance = {
    1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 
    11: False, 12: False, 13: False, 14: False, 15: False, 16: False, 17: False, 18: False, 19: False, 20: False, 
    21: False, 22: False, 23: False, 24: False, 25: False, 26: False, 27: False, 28: False, 29: False, 30: False, 
    31: False, 32: False, 33: False, 34: False, 35: False, 36: False, 37: False, 38: False, 39: False, 40: False, 
    41: False, 42: False, 43: False, 44: False, 45: False, 46: False, 47: False, 48: False, 49: False, 50: False, 
    51: False, 52: False, 53: False, 54: False, 55: False, 56: False, 57: False, 58: False, 59: False, 60: False, 
    61: False, 62: False, 63: False, 64: False, 65: False, 66: False, 67: False, 68: False, 69: False, 70: False, 
    71: False, 72: False, 73: False, 74: False, 75: False, 76: False, 77: False, 78: False, 79: False, 80: False, 
    81: False, 82: False, 83: False, 84: False, 85: False, 86: False, 87: False, 88: False, 89: False, 90: False, 
    91: False, 92: False, 93: False, 94: False, 95: False
}

encounter = {
    1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 
    11: False, 12: False, 13: False, 14: False, 15: False, 16: False, 17: False, 18: False, 19: False, 20: False, 
    21: False, 22: False, 23: False, 24: False, 25: False, 26: False, 27: False, 28: False, 29: False, 30: False, 
    31: False, 32: False, 33: False, 34: False, 35: False, 36: False, 37: False, 38: False, 39: False, 40: False, 
    41: False, 42: False, 43: False, 44: False, 45: False, 46: False, 47: False, 48: False, 49: False, 50: False, 
    51: False, 52: False, 53: False, 54: False, 55: False, 56: False, 57: False, 58: False, 59: False, 60: False, 
    61: False, 62: False, 63: False, 64: False, 65: False, 66: False, 67: False, 68: False, 69: False, 70: False, 
    71: False, 72: False, 73: False, 74: False, 75: False, 76: False, 77: False, 78: False, 79: False, 80: False, 
    81: False, 82: False, 83: False, 84: False, 85: False, 86: False, 87: False, 88: False, 89: False, 90: False, 
    91: False, 92: False, 93: False, 94: False, 95: False
}

# Other Functions

def game_over():
    if current_player_health <= 0:
        quit

def cont():
    input('\n' + Fore.BLACK + Back.WHITE + 'Press enter to continue.' + Fore.RESET + Back.RESET + '\n')

def rolling(rolling_for = ''):
    x =0
    while x <= 3:
        xperiod = x * '.'
        print(f'\rRolling {rolling_for}{xperiod}',end='')
        x += 1
        time.sleep(1)

def roll_to_hit(roll, dc, mod):
    rolling('to hit')
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

def bar(current, total, bar_length = 20):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '█' + '▒'
    idk = int(fraction * bar_length) * '█'
    padding = int(bar_length - len(arrow)) * '-'
    if fraction >= .99:
        return f'''{idk}{padding} {round(current)}hp'''
    else:
        return f'''{arrow}{padding} {round(current)}hp'''


strength = 0
dexterity = 0
endurance = 0
inteligence = 0
wisdom = 0
charisma = 0
is_str_chosen = False
is_dex_chosen = False
is_end_chosen = False
is_int_chosen = False
is_wis_chosen = False
is_cha_chosen = False
all_stats = False

name = input(Fore.GREEN +'\nWhat is your name?\n' + Fore.RESET)


while True:
    class_choice = int(input('''Please choose your character class:
    1. Sorcerer
    2. Wizard
    3. Rogue
    4. Bard
    5. Cleric
    6. Monk
    7. Warlock
    8. Fighter
    9. Paladin
    10. Barbarian\n'''))
    if class_choice == 1:
        character_class = 'sorcerer'
        break

    elif class_choice == 2:
        character_class = 'wizard'
        break

    elif class_choice == 3:
        character_class = 'rogue'
        break

    elif class_choice == 4:
        character_class = 'bard'
        break

    elif class_choice == 5:
        character_class = 'cleric'
        break

    elif class_choice == 6:
        character_class = 'monk'
        break

    elif class_choice == 7:
        character_class = 'warlock'
        break

    elif class_choice == 8:
        character_class = 'fighter'
        break

    elif class_choice == 9:
        character_class = 'paladin'
        break

    elif class_choice == 10:
        character_class = 'barbarian'
        break
    else:
        print(Fore.RED + 'Please enter a number from 1-11.\n' + Fore.RESET)
print(f'You now are a {character_class.title()}')


# Equipment Functions

player_equipment = {
    'equipped weapon': '', 'stored weapon 1': '', 'stored weapon 2': '', 'stored weapon 3': '', 'stored weapon 4': '', 'stored weapon 5': '',
    'equipped armor': '', 'stored armor': '',
    'copper pieces': 0, 'silver pieces': 0,  'gold pieces': 0, 'arrows': '', 'item 5': '', 'item 6': ''
}

player_unique_items = []

def unarmored():
    player_ac = 10 + player_mods['dex mod']
    return player_ac

def pickupweapon(weapon):
    print(f'you picked up a {weapon_name[weapon]}')
    while True:
        choice = input(f'''Which slot should it be put in?
    1. {player_equipment['stored weapon 1']}
    2. {player_equipment['stored weapon 2']}
    3. {player_equipment['stored weapon 3']}
    4. {player_equipment['stored weapon 4']}
    5. {player_equipment['stored weapon 5']}
    6. Throw away (cannot be undone)\n''')
        ynchoice = input('Are you sure? Yes or No\n')
        if ynchoice.lower() == 'yes':
            if choice == 1:
                player_equipment['stored weapon 1'] = weapon['name']
                print('You pick up the weapon')
                break
            elif choice == 2:
                player_equipment['stored weapon 2'] = weapon['name']
                print('You pick up the weapon')
                break
            elif choice == 3:
                player_equipment['stored weapon 3'] = weapon['name']
                print('You pick up the weapon')
                break
            elif choice == 4:
                player_equipment['stored weapon 4'] = weapon['name']
                print('You pick up the weapon')
                break
            elif choice == 5:
                player_equipment['stored weapon 5'] = weapon['name']
                print('You pick up the weapon')
                break
            elif choice == 6:
                print('You don\'t pick up the weapon')
                break
            else:
                print(Fore.RED + 'Invalid input Please try again.' + Fore.RESET)


if character_class == 'barbarian':
    player_equipment['equipped armor'] = 'unarmored'
    while True:
        main = int(input('''Choose your main weapon
    1. A Greataxe (1d12 + str mod)
    2. Morningstar (2d6 + str mod)\n'''))
        if main == 1:
            player_equipment['equipped weapon'] = 'greataxe'
            break
        elif main == 2:
            player_equipment['equipped weapon'] = 'morningstar'
            break
        else:
            print('Please enter a valid number')
    while True:
        stored = int(input('''Choose your other weapon(s)
    1. 2 handaxes (1d6 + str mod)
    2. 2 maces (1d6 + str mod)\n'''))
        if stored == 1:
            player_equipment['stored weapon 1'] = 'handaxe'
            player_equipment['stored weapon 2'] = 'handaxe'
            break
        elif stored == 2:
            player_equipment['stored weapon 1'] = 'mace'
            player_equipment['stored weapon 2'] = 'mace'
            break
        else:
            print('please enter a valid number')
    def unarmored():
        player_ac = 10 + player_mods['dex mod'] + player_mods['end mod']
        return player_ac
        
elif character_class == 'bard':
    while True:
        main = int(input('''Choose your main weapon
    1. '''))

# elif character_class == 'cleric':

# elif character_class == 'fighter'  :

# elif character_class == 'monk':

# elif character_class == 'paladin':

# elif character_class == 'rogue':

# elif character_class == 'sorcerer':

# elif character_class == 'warlock':

# elif character_class == 'wizard':

print(player_equipment['equipped weapon'], player_equipment['stored weapon 1'], player_equipment['stored weapon 2'], player_equipment['equipped armor'])


print('Please assign your stats')
cont()

while all_stats == False:
    if is_str_chosen and is_dex_chosen and is_end_chosen and is_int_chosen and is_wis_chosen and is_cha_chosen:
        all_stats = True
        continue
    stat_roll1 = d6()
    stat_roll2 = d6()
    stat_roll3 = d6()
    stat_roll4 = d6()
    stat_list = [stat_roll1, stat_roll2, stat_roll3, stat_roll4,]
    stat_roll_main= stat_roll1 + stat_roll2 + stat_roll3 + stat_roll4 - min(stat_list)
    print(f'You rolled a {stat_roll_main}!')
    choice = int(input(f'''{Fore.GREEN}Which stat?{Fore.RESET}
    1. Strength {strength}
    2. Dexterity {dexterity}
    3. Endurance {endurance}
    4. Inteligence {inteligence}
    5. Wisdom {wisdom}
    6. Charisma {charisma}\n1-6\n'''))
    while True:
        if choice == 1 and is_str_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            break
        elif choice == 1 and is_str_chosen == False:
            strength = stat_roll_main
            is_str_chosen = True
            print(f'Your Strength is now {strength}.')
            cont()
            break

        elif choice == 2 and is_dex_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            break
        elif choice == 2 and is_dex_chosen == False:
            dexterity = stat_roll_main
            is_dex_chosen = True
            print(f'Your Dexterity is now {dexterity}.')
            cont()
            break

        elif choice == 3 and is_end_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            break
        elif choice == 3 and is_end_chosen == False:
            endurance = stat_roll_main
            is_end_chosen = True
            print(f'Your Endurance is now {endurance}')
            cont()
            break

        elif choice == 4 and is_int_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            break
        elif choice == 4 and is_int_chosen == False:
            inteligence = stat_roll_main
            is_int_chosen = True
            print(f'Your Inteligence is now {inteligence}')
            cont()
            break

        elif choice == 5 and is_wis_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            break
        elif choice == 5 and is_wis_chosen == False:
            wisdom = stat_roll_main
            is_wis_chosen = True
            print(f'Your Wisdom is now {wisdom}')
            cont()
            break
        elif choice == 6 and is_cha_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            break
        elif choice == 6 and is_cha_chosen == False:
            charisma = stat_roll_main
            is_cha_chosen = True
            print(f'Your charisma is now {charisma}')
            cont()
            break
        else:
            print('Please pick a number between 1 and 6.')
            continue

player_mods = {
    'str mod': int((strength - 10) / 2),
    'dex mod': int((dexterity - 10) / 2),
    'end mod': int((endurance - 10) / 2),
    'int mod': int((inteligence - 10) / 2),
    'wis mod': int((wisdom - 10) / 2),
    'cha mod': int((charisma - 10) / 2)
}

print(player_mods)
player_ac = 10 + player_mods['dex mod']
initiative_bonus = player_mods['dex mod']
days = 0
level = 1
difficulty = 1 + days / 25

print(initiative_bonus)

# Various Dictionaries

starting_hit_dice = {
    'sorcerer': 6, 'wizard': 6, 'rogue': 8, 'bard': 8,
    'cleric': 8, 'monk': 8, 'warlock': 8, 'fighter': 10,
    'paladin': 10, 'barbarian': 12
}

hit_dice = {
    'sorcerer': d6(), 'wizard':  d6(), 'rogue': d8(), 'bard': d8(),
    'cleric': d8(), 'monk': d8(), 'warlock': d8(), 'fighter': d10(),
    'paladin': d10(), 'barbarian': d12()
}

player_health = starting_hit_dice[character_class] + player_mods['end mod']
current_player_health = player_health
print(player_health)
print(current_player_health)
cont()

weapon_name = {
    'club': 'Club', 'dagger': 'Dagger', 'great club': 'Great Club', 'javelin': 'Javelin', 'light hammer': 'Light Hammer',
    'mace': 'Mace', 'quarterstaff': 'Quarterstaff', 'sickle': 'Sickle', 'spear': 'Spear', 'battle axe': 'Battle Axe',
    'flail': 'Flail', 'glaive': 'Glaive', 'greataxe': 'Greataxe', 'greatsword': 'Greatsword', 'halberd': 'Halberd',
    'handaxe': 'Handaxe', 'lance': 'Lance', 'longsword': 'Longsword', 'maul': 'Maul', 'morningstar': 'Morningstar',
    'pike': 'Pike', 'rapier': 'Rapier', 'scimitar': 'Scimitar', 'shortsword': 'Shortsword', 'trident': 'Trident',
    'war pick': 'War Pick', 'warhammer': 'Warhammer', 'whip': 'Whip',
    # unique weapons
    'dangolf staff': 'Dangolf\'s Staff', 'sif dagger': 'Siffrin\'s Dagger', 'player sif dagger': 'Siffrin\'s Dagger'
}


weapon_damage = {
    'club': (lambda: d4()), 'dagger': (lambda: d4()), 'great club': (lambda: d4()), 'javelin': (lambda: d6()), 'light hammer': (lambda: d4()),
    'mace': (lambda: d6()), 'quarterstaff': (lambda: d8()), 'sickle': (lambda: d4()), 'spear': (lambda: d6()), 'battle axe': (lambda: d8()),
    'flail': (lambda: d8()), 'glaive': (lambda: d10()), 'greataxe': (lambda: d12()), 'greatsword': (lambda: d6(2)), 'halberd': (lambda: d10()),
    'handaxe': (lambda: d6()), 'lance': (lambda: d8()), 'longsword': (lambda: d8()), 'maul': (lambda: d6(2)), 'morningstar': (lambda: d8()),
    'pike': (lambda: d10()), 'rapier': (lambda: d8()), 'scimitar': (lambda: d6()), 'shortsword': (lambda: d6()), 'trident': (lambda: d8()),
    'war pick': (lambda: d8()), 'warhammer': (lambda: d8()), 'whip': (lambda: d4()),
    # unique weapons
    'dangolf staff': (lambda: d6(4)), 'sif dagger': 999, 'player sif dagger': (lambda: d4(5))
}

weapon_mod = {
    'club': player_mods['str mod'], 'dagger': player_mods['dex mod'], 'great club': player_mods['str mod'], 'javelin': player_mods['str mod'],
    'light hammer': player_mods['str mod'], 'mace': player_mods['str mod'], 'quarterstaff': player_mods['str mod'], 'sickle': player_mods['str mod'],
    'spear': player_mods['str mod'], 'battle axe': player_mods['str mod'], 'flail': player_mods['str mod'], 'glaive': player_mods['str mod'],
    'greataxe': player_mods['str mod'], 'greatsword': player_mods['str mod'], 'halberd': player_mods['str mod'], 'handaxe': player_mods['str mod'],
    'lance': player_mods['str mod'], 'longsword': player_mods['str mod'], 'maul': player_mods['str mod'], 'morningstar': player_mods['str mod'],
    'pike': player_mods['str mod'], 'rapier': player_mods['dex mod'], 'scimitar': player_mods['dex mod'], 'shortsword': player_mods['dex mod'],
    'trident': player_mods['str mod'], 'war pick': player_mods['str mod'], 'warhammer': player_mods['str mod'], 'whip': player_mods['dex mod'],
    # unique weapons
    'dangolf staff': player_mods['wis mod'], 'player sif dagger': player_mods['dex mod'], 
}

npc_weapon_mod = {
    'club': 'str mod', 'dagger': 'dex mod', 'great club': 'str mod', 'javelin': 'str mod', 'light hammer': 'str mod',
    'mace': 'str mod', 'quarterstaff': 'str mod', 'sickle': 'str mod', 'spear': 'str mod', 'battle axe': 'str mod',
    'flail': 'str mod', 'glaive': 'str mod', 'greataxe': 'str mod', 'greatsword': 'str mod', 'halberd': 'str mod',
    'handaxe': 'str mod', 'lance': 'str mod', 'longsword': 'str mod', 'maul': 'str mod', 'morningstar': 'str mod',
    'pike': 'str mod', 'rapier': 'dex mod', 'scimitar': 'dex mod', 'shortsword': 'dex mod', 'trident': 'str mod',
    'war pick': 'str mod', 'warhammer': 'str mod', 'whip': 'dex mod',
    # unique weapons
    'dangolf staff': 'wis mod', 'sif dagger': 'dex mod', 
}

# Enemies

# Basic
goblin = {
    'name': 'Goblin', 'title': '',
    'health': int(d6(2) * difficulty), 'weapon': 'dagger', 'ac': 5, 'exp': 50, 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1
}

kobold = {
    'name': 'Kobold', 'title': '',
    'health': int((d4(4) - 2) * difficulty), 'weapon': 'dagger', 'ac': 7, 'exp': 25, 'agression': 4,
    'str mod': -2, 'dex mod': 2, 'con mod': -1, 'int mod': -1, 'wis mod': -2, 'cha mod': -1
}



# Named
kile = {
    'name': 'Kile', 'title': ', With An I',
    'health': d4(4) + 20, 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1
}

gronk = {
    'name': 'Gronk', 'title': ', The Killer',
    'health': d6(4) + 20, 'weapon': 'maul', 'ac': 13, 'exp': 200, 'agression': 3,
    'str mod': 4, 'dex mod': -1, 'end mod': 3, 'int mod': -2, 'wis mod': -1, 'cha mod': 0
}

siffrin_traveler = {
    'name': 'Siffrin', 'title': ', The Traveler',
    'health': 50, 'weapon': 'dagger', 'ac': 13, 'exp': 500, 'agression': 6,
    'str mod': 0, 'dex mod': 5, 'end mod': 2, 'int mod': 1, 'wis mod': -1, 'cha mod': 2
}

siffrin_lost = {
    'name': 'Siffrin', 'title': ', The Lost',
    'health': 999, 'weapon': 'sif dagger', 'ac': 15, 'exp': 9999, 'agression': 10,
    'str mod': 0, 'dex mod': 6, 'end mod': 3, 'int mod': 0, 'wis mod': -2, 'cha mod': 1
}

dangolf = {
    'name': 'Dangolf', 'title': ', The Gold',
    'health': 150, 'weapon': 'dangolf staff', 'ac': 10, 'exp': 1000, 'agression': 2,
    'str mod': -2, 'dex mod': -2, 'end mod': 2, 'int mod': 5, 'wis mod': 10, 'cha mod': 2
}

# Rolling Functions

def roll_against_player(agressor_mod, agressor, defender, defender_mod):
    agressor_roll = d20() + agressor[agressor_mod]
    defender_roll = d20() + defender[defender_mod]
    if agressor_roll > defender_roll:
        return True
    elif agressor_roll < defender_roll:
        return False

# Fighting Functions

def npc_attack(tohit, weapon, enemy):
    if tohit == 'crit':
        print('\nCritical Hit!')
        damage = weapon_damage[weapon]() + enemy[npc_weapon_mod[weapon]] * 2
        cont()
        return damage
    elif tohit == True:
        print('\nAttack hit.')
        cont()
        return weapon_damage[weapon]() + enemy[npc_weapon_mod[weapon]]
    elif tohit == False:
        print('\nAttack missed.')
        cont()
        return 0
    else:
        print('\nAttack missed.')
        cont()
        return 0

def attack(tohit, weapon):
    if tohit == 'crit':
        print(Fore.RED + '\nCritical' + Fore.RESET +' Hit!')
        cont()
        return weapon_damage[weapon]() + weapon_mod[weapon] * 2
    elif tohit == True:
        print('\nYour attack hit.')
        cont()
        return weapon_damage[weapon]() + weapon_mod[weapon]
    elif tohit == False:
        print('\nYou missed.')
        cont()
        return 0
    else:
        print('\nYou missed.')
        cont()
        return 0

def npc_turn(enemy, blocking):
    global current_player_health

    print('It\'s ' + enemy['name'] + '\'s turn')
    roll = d10() + enemy['agression']

    if roll > 8:
        print(enemy['name'] + ' is attacking.\n')

        damage = npc_attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy['weapon']]), enemy['weapon'], enemy)
        damage = round(damage * blocking)

        if damage > 50:
            print(f'You took {Fore.RED}{damage}{Fore.RESET} damage.')
        else:
            print(f'You took {damage} damage.')

    elif roll <= 8:
        enemy1_blocking = 0.5
        damage = 0
        print(enemy['name'] + ' is blocking.')

    current_player_health -= damage
    cont()

def player_turn(no_of_enemy, enemy1, enemy2, enemy3, enemy4):
    while True:
        print('Your turn.\n')
        print(f'''Player Stats
    Level.............{level}
    Weapon............{weapon_name[player_equipment["equipped weapon"]]}
    Health {bar(current_player_health, player_health, 20)}''')
        try:
            player_turn = int(input('''
            1. Attack
            2. Block\n'''))
        except ValueError:
            print('Invalid Input: please enter a valid input')
            cont()
        else:
            break

    if player_turn == 1:
        while True:
            if no_of_enemy == 1:
                print(f'You attack {enemy1["name"]}')
                choice = 1

            elif no_of_enemy == 2:
                print(f'''\nChoose who to attack:
    1. {enemy1["name"]}{enemy1["title"]}
    2. {enemy2["name"]}{enemy2["title"]}''')
                choice = int(input(''))

            elif no_of_enemy == 3:
                print(f'''\nChoose who to attack:
    1. {enemy1["name"]}{enemy1["title"]}
    2. {enemy2["name"]}{enemy2["title"]}
    3. {enemy3["name"]}{enemy3["title"]}''')
                choice = int(input(''))

            elif no_of_enemy == 4:
                print(f'''\nChoose who to attack:
    1. {enemy1["name"]}{enemy1["title"]}
    2. {enemy2["name"]}{enemy2["title"]}
    3. {enemy3["name"]}{enemy3["title"]}
    4. {enemy4["name"]}{enemy4["title"]}''')
                choice = int(input(''))
            print()

            if choice == 1:
                damage =  attack(roll_to_hit(d20(), enemy1['ac'], weapon_mod[player_equipment['equipped weapon']]), player_equipment['equipped weapon'])
                if damage > 50:
                    print(f'You attack {enemy1["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                else:
                    print(f'You attack {enemy1["name"]} for {damage}')
                return False, damage, enemy1['name']

            elif choice == 2:
                damage =  attack(roll_to_hit(d20(), enemy2['ac'], weapon_mod[player_equipment['equipped weapon']]), player_equipment['equipped weapon'])
                if damage > 50:
                    print(f'You attack {enemy2["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                else:
                    print(f'You attack {enemy2["name"]} for {damage}')
                return False, damage, enemy2['name']

            elif choice == 3:
                damage =  attack(roll_to_hit(d20(), enemy3['ac'], weapon_mod[player_equipment['equipped weapon']]), player_equipment['equipped weapon'])
                if damage > 50:
                    print(f'You attack {enemy3["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                else:
                    print(f'You attack {enemy3["name"]} for {damage}')
                return False, damage, enemy3['name']

            elif choice == 4:
                damage =  attack(roll_to_hit(d20(), enemy4['ac'], weapon_mod[player_equipment['equipped weapon']]), player_equipment['equipped weapon'])
                if damage > 50:
                    print(f'You attack {enemy4["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                else:
                    print(f'You attack {enemy4["name"]} for {damage}')
                return False, damage, enemy4['name']

            else:
                print(f'{Fore.RED}Please enter a valid number.{Fore.RESET}')

    elif player_turn == 2:
        print('You are blocking.')
        return True, 0, ''

def fight(no_of_enemy, enemy1, enemy2 = '', enemy3 = '', enemy4 = ''):
    global player_health
    global current_player_health
    no_of_turns = 0
    exp = 0

    rolling('for Initiative')
    player_initiative = d20() + player_mods['dex mod'] + initiative_bonus
    initiative = {
        player_initiative: 0
    }
    print(f'\nYou rolled a {player_initiative} for initiative.')

    enemy1_is_alive = False
    enemy2_is_alive = False
    enemy3_is_alive = False
    enemy4_is_alive = False
    enemy1_blocking = 1
    enemy2_blocking = 1
    enemy3_blocking = 1
    enemy4_blocking = 1

    enemy1_is_alive = True
    initiative[d20() + enemy1['dex mod']] = enemy1['name']+'1'
    enemy1_health = enemy1['health']
    if enemy2 != '':
        enemy2_is_alive = True
        initiative[d20() + enemy2['dex mod']] = enemy2['name']+'2'
        enemy2_health = enemy2['health']
    if enemy3 != '':
        enemy3_is_alive = True
        initiative[d20() + enemy3['dex mod']] = enemy3['name']+'3'
        enemy3_health = enemy3['health']
    if enemy4 != '':
        enemy4_is_alive = True
        initiative[d20() + enemy4['dex mod']] = enemy4['name']+'4'
        enemy4_health = enemy4['health']

    list_initiative = list(initiative.keys())
    list_initiative.sort(reverse= True)
    initiative = {item: initiative[item] for item in list_initiative}
    list_initiative = list(initiative.values())

    print('Initiative Order:')
    for x in list_initiative:
        if x == 0:
            print('You, ', end = '')
        else:
            print(f'{x}, ', end = '')
    print()
    cont()

    while no_of_enemy > 0 and current_player_health > 0:
        if player_health <= 0:
            break
        blocking = 1

        for turn in list_initiative:
            no_of_turns += 1
            if current_player_health <= 0:
                continue

            if turn == 0:

                player = player_turn(no_of_enemy, enemy1, enemy2, enemy3, enemy4)

                if player[0] == True:
                    blocking = 0.25
                elif player[0] == False:
                    blocking = 1
                    if player[2] == enemy1['name']:
                        enemy1_health -= player[1] * enemy1_blocking
                    elif player[2] == enemy2['name']:
                        enemy2_health -= player[1] * enemy2_blocking
                    elif player[2] == enemy3['name']:
                        enemy3_health -= player[1] * enemy3_blocking
                    elif player[2] == enemy4['name']:
                        enemy4_health -= player[1] * enemy4_blocking

                if enemy1_health <= 0 and enemy1_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy1["name"]}{Fore.RESET}')
                    enemy1_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy1['exp']
                if enemy2_is_alive:
                    if enemy2_health <= 0:
                        print(f'{Fore.LIGHTRED_EX}You killed {enemy2["name"]}{Fore.RESET}')
                        enemy2_is_alive = False
                        no_of_enemy -= 1
                        exp += enemy2['exp']
                if enemy3_is_alive:
                    if enemy3_health <= 0:
                        print(f'{Fore.LIGHTRED_EX}You killed {enemy3["name"]}{Fore.RESET}')
                        enemy3_is_alive = False
                        no_of_enemy -= 1
                        exp += enemy3['exp']
                if enemy4_is_alive:
                    if enemy4_health <= 0:
                        print(f'{Fore.LIGHTRED_EX}You killed {enemy4["name"]}{Fore.RESET}')
                        enemy4_is_alive = False
                        no_of_enemy -= 1
                        exp += enemy4['exp']
                cont()

            elif turn != 0:
                if str(turn).endswith('1') and enemy1_is_alive:
                    npc_turn(enemy1, blocking)

                elif str(turn).endswith('2') and enemy2_is_alive:
                    npc_turn(enemy1, blocking)

                elif str(turn).endswith('3') and enemy3_is_alive:
                    npc_turn(enemy1, blocking)

                elif str(turn).endswith('4') and enemy4_is_alive:
                    npc_turn(enemy1, blocking)

    if current_player_health <= 0:
        print(Fore.RED + 'You Lost.' + Fore.RESET)
        return 0
    elif no_of_enemy == 0:
        print(Fore.GREEN + 'You won!' + Fore.RESET)
        print(f'You gained {exp} exp')
        return 1, exp

while True:
    try:
        distance = int(input(Fore.GREEN + '\nhow long do you want to hike?\n' + Fore.RESET))
    except ValueError:
        print('Invalid Input: please try again')
        continue
    else:
        break
distance_traveled = 0
karma = 0
luck_bonus = 0
luck_multiplier = 1

def luck_calc():
    luck = karma/2 + 10 + luck_bonus
    luck_mod = int((luck - 10) / 2)
    return round(luck, 2), luck_mod

fight(1, goblin)
game_over()

# Chances & encounters

def chance1():
    chance[1] = True
    print('''As you travel a bit off the beaten path you run into a party of adventurers around a campfire, they look experienced.
One of them notices you and begins to talk;
"Oh hey! A person! You're not a bandit are you?"''')
    cont()
    while True:
        try:
            say = int(input('''What do you say?
    1. Yes I am. Now give me all your money *fight*
    2. No I'm just a traveler
    3. You'll never know *you wink at them ;D*
    4. *Walk away slowly*\n'''))
        except ValueError:
            print('Invalid Input: please try again')
            continue
        else:
            break
    if say == 1:
        if karma <= -5:
            print('They didn\'t like your admition of guilt and begin to quickly prepare for battle.')
            cont()
        elif karma >= 5:
            print('They didn\'t like your attempt at humour and begin to quickly prepare for battle.')
            cont()
        else:
            print('They didn\'t appear to like that and begin to quickly prepare for battle.')
            cont()

        if level < 10:
            rolling('for a dex save')
            save = d20()
            print(f'You rolled a {save} for a total of  {save + player_mods["dex mod"]}')
            save += player_mods["dex mod"]
            cont()
            if save < 8:
                print('But before you can grasp the depth of your mistake one of them hits you with a spell that blinds you with a flash of light.')
                cont()
                print('After being blinded you feel a sharp pain as something hits you on the back of the head. You lose consciousness.')
                time.sleep(1)
                print('You slowly start to wake up and realise you are tied up, with your belongings hung from the branches of a very tall tree.\n')
                thing = round(current_player_health/8)
                print(f'You are slightly hurt and lost {thing} heath.')
                cont()

            elif save > 18:
                print('You notice one of them begins to cast a spell, instinctively you cover your eyes')
                cont()
                print('You see a flash through your hands and are partially stunned')
                while True:
                    try:
                        choice = int(input('''What do you do?
        1. Stay and fight
        2. RUN AWAY\n'''))
                    except ValueError:
                        print('Invalid Input: please try again')
                        continue
                    else:
                        if choice == 1:
                            fight(2, kile, gronk)
                            break
                        elif choice == 2:
                            print('You manage to escape')
                            cont()
                            break
                        else:
                            print('Invalid Input: please try again')
                            continue
            elif save >= 8:
                print('')
        elif level >= 10:
            fight(2, kile, gronk)
    elif say == 2:
        print('work in progress')
    elif say == 3:
        print('work in progress')


while distance > distance_traveled:
    # if d20() <= 10:
    #     is_encounter = True
    # else:
    #     is_encounter = False
    # if d20() >= 10:
    #     is_chance = True
    # else:
    #     is_chance = False
    is_chance = True # REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING
    is_encounter = False # REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING

    if is_chance == True and is_encounter == True:
        roll_enocounter = d100()
        roll_chance = d100()

    elif is_encounter == True:
        roll_encounter = d100()

    elif is_chance == True:
        roll_chance = d100()
        roll_chance = 1 # REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING REMOVE AFTER TESTING

        if roll_chance == 1 and chance[1] == False:
            chance1()

        elif roll_chance == 1 and chance[1] == True:
            roll_chance = 90 + d10()
        elif roll_chance == 2 and chance[2] == False:
            print('work in progress')