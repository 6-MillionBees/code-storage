# Arden Boettcher
# 11/20/24
# Spells

from default_functions import *# IMPORT
from dice import *
from colorama import Fore

spell_damage_increase = 0

player_spells = { # WIP
    0: ['acid splash', 'fire bolt',  'poison spray'],
    1: ['burning hands', 'healing word', 'magic missile'],
    2: ['fireball'],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}

print_spell_level = {
    0: 'cantrips',
    1: 'level 1',
    2: 'level 2',
    3: 'level 3',
    4: 'level 4',
    5: 'level 5',
    6: 'level 6',
    7: 'level 7',
    8: 'level 8',
    9: 'level 9',
}

current_player_spell_slots = { # WIP
    0: -1,
    1: 3,
    2: 1,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

max_player_spell_slots = { # WIP
    0: -1,
    1: 3,
    2: 1,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

spell_descriptions = {
    'acid splash': f'''{Fore.GREEN}    cantrip, single, {1 + spell_damage_increase}d6{Fore.RESET}
details: You swing a bubble of acid towards an enemy
dealing {1 + spell_damage_increase}d6 damage''',

    'fire bolt': f'''{Fore.GREEN}    cantrip, single, {1 + spell_damage_increase}d10{Fore.RESET}
details: You throw a small ball of fire towards one
unlucky enemy damaging it for {1 + spell_damage_increase}d10 fire damage on a
failed dexterity save and half that on a success.''',

    'poison spray': f'''{Fore.GREEN}    cantrip, single, {1 + spell_damage_increase}d6{Fore.RESET}
details: You sent a puff of noxious gas towards two random
enemies, they take {1 + spell_damage_increase}d6 damage on a failed constitution
save and half that on a success.''',

    'healing word': f'''{Fore.GREEN}    level 1, healing, {2 + int(spell_damage_increase / 2)}d4{Fore.RESET}
details: You speak a word commading the arcane to
heal the desired wound restoring {2 + int(spell_damage_increase / 2)}d4 health.''',

    'burning hands': f'''{Fore.GREEN}    level 1, AOE, {3 + spell_damage_increase}d6 {Fore.RESET}
details: You spread your fingers sending out a wave 
of flame hitting 3 adjacent enemies for {3 + spell_damage_increase}d6.''',

    'magic missile': f'''{Fore.GREEN}    level 1, multi-hit, {1 + int(spell_damage_increase / 2)}d4 + 1 {Fore.RESET}
details: You fire three homing bolts of glowing blue
magic dealing {1 + int(spell_damage_increase / 2)}d4 + 1 to three enemies of your choice.''',

    'fireball': f'''{Fore.GREEN}    level 2, AOE, {8 + int(spell_damage_increase / 2)}d6 {Fore.GREEN}
details : You throw a hurtling ball of fire that
explodes on contact dealing {8 + int(spell_damage_increase / 2)}d6 to all enemies.'''
}


# This is so complicated because of customizability
# It works regardless of any other variable
# you could have hundreds of spells and it'd still keep on chuggin
def spells_menu():

    while True:
        print('Spells:')

        num = 0
        for spell_level in player_spells.keys():
            if player_spells[spell_level] == []:
                continue
            print(f'    {num}.) {print_spell_level[num]}: {", ".join(player_spells[spell_level])} (spell slots: {current_player_spell_slots[spell_level]})')
            num += 1

        spell_level = int_input('Choose a spell level (-1 to go back): ')
        print()
        if current_player_spell_slots[spell_level] <= 0:
            print('You don\'t have enough spell slots to cast that')

        if spell_level == -1:
            return False
        elif spell_level in range(num):

            if spell_level != 0:
                print(f'You have {current_player_spell_slots[spell_level]} {print_spell_level[spell_level]} spell slots')
            print('Which spell?: ')

            while True:
                
                num = 0
                for spell in player_spells[spell_level]:
                    num += 1
                    print(f'    {num}.) {spell}')
                spell_choice = input('type description for spell descriptions: ')
                if spell_choice == 'description':
                    num1 = 0
                    for spell in player_spells[spell_level]:
                        num1 += 1
                        print(f'''    {num1}.) 
{spell_descriptions[spell]}''')
                    cont()
                    continue

                if spell_choice in range(1, len(player_spells) + 1):
                    break
                else:
                    invalid()
                    continue

            if spell_choice == -1:
                continue
            elif spell_choice in range(1, num + 1):
                print(f'You cast {player_spells[spell_level][spell_choice - 1].title()}')
                return player_spells[spell_level][spell_choice - 1]
            else:
                invalid()
                continue

        else:
            invalid()
            continue

from player_stats import skill_save

def cast(spell, enemies): # WIP
    if spell == 'acid splash':
        return cast_acid_splash(enemies)

    elif spell == 'healing word':
        current_player_spell_slots[1] - 1
        return cast_healing_word(enemies)

    elif spell == 'fire bolt':
        return cast_fire_bolt(enemies)

    elif spell == 'fireball':
        current_player_spell_slots[2] - 1
        return cast_fireball(enemies)


def cast_acid_splash(enemies):
    print('You cast Acid Splash')
    num = 0
    while True:
        for enemy in enemies:
            num +=1
            print(f'{num}.) {enemy["name"]}')
        
        choice = int_input('Which enemy do you attack?: ')
        if choice in range(1, len(enemies) + 1):
            break
        else:
            invalid()
            continue
    dictionary = {choice: lambda: d6(1 + spell_damage_increase)}
    return dictionary


def cast_fire_bolt(enemies):
    print('You cast Fire Bolt')
    num = 0
    while True:
        for enemy in enemies:
            num +=1
            print(f'{num}.) {enemy["name"]}')
        
        choice = int_input('Which enemy do you attack?: ')
        if choice in range(1, len(enemies) + 1):
            break
        else:
            invalid()
            continue
    rolling('Enemy Dex Save')
    enemy_save = skill_save(enemies[choice - 1]['dex mod'], 10 + (spell_damage_increase - 1))
    if enemy_save == True:
        dictionary = {choice: lambda: d10(1 + spell_damage_increase) / 2}
    elif enemy_save == False:
        dictionary = {choice: lambda: d10(1 + spell_damage_increase)}
    return dictionary


def poison_spray(enemies):
    print('You cast Fire Bolt')
    choice1 = randint(1, len(enemies))

    rolling('Enemy Dex Save')
    enemy_save = skill_save(enemies[choice1 - 1]['dex mod'], 10 + (spell_damage_increase - 1))
    if enemy_save == True:
        dictionary = {choice1: lambda: d10(1 + spell_damage_increase) / 2}
    elif enemy_save == False:
        dictionary = {choice1: lambda: d10(1 + spell_damage_increase)}

    if len(enemies) == 1:
        return dictionary

    choice2 = randint(1, len(enemies))
    while choice1 == choice2:
        choice2 = randint(1, len(enemies))

    enemy_save = skill_save(enemies[choice2 - 1]['dex mod'], 10 + (spell_damage_increase - 1))
    if enemy_save == True:
        dictionary += {choice2: lambda: d10(1 + spell_damage_increase) / 2}
    elif enemy_save == False:
        dictionary += {choice2: lambda: d10(1 + spell_damage_increase)}

    return dictionary


def cast_healing_word(enemies):
    print('You cast Acid Splash')
    num = 0
    while True:
        print('0.) Yourself')
        for enemy in enemies:
            num +=1
            print(f'{num}.) {enemy["name"]}')
        
        choice = int_input('Which enemy do you attack?: ')
        if choice in range(len(enemies) + 1):
            break
        else:
            invalid()
            continue
    dictionary = {choice: (lambda: d4(2 + int(spell_damage_increase / 2)) * -1)}
    return dictionary


def cast_fireball():
    print('You cast Fireball.')
    cont()
    dictionary = {1: (lambda: d6(8)), 2: (lambda: d6(8)), 3: (lambda: d6(8)), 4: (lambda: d6(8)),}
    return dictionary


# REMOVE AFTER TESTING

# from npc_stats import *

# enemies = [goblin, kobold, goblin, goblin] 
# spell = cast(spells_menu(), enemies)

# print(spell)