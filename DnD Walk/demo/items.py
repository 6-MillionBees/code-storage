# Arden Boettcher
# 12/2/24
# Item Stats

from default_functions import *
from dice import *
from player_stats import *

weapon_name = {
    'empty':             'Empty',

    'battle axe':        'Battle Axe',
    'club':              'Club',
    'dagger':            'Dagger',
    'flail':             'Flail',
    'glaive':            'Glaive',
    'great club':        'Great Club',
    'greataxe':          'Greataxe',
    'greatsword':        'Greatsword',
    'halberd':           'Halberd',
    'handaxe':           'Handaxe',
    'javelin':           'Javelin',
    'lance':             'Lance',
    'longsword':         'Longsword',
    'light hammer':      'Light Hammer',
    'mace':              'Mace',
    'maul':              'Maul',
    'morningstar':       'Morningstar',
    'pike':              'Pike',
    'quarterstaff':      'Quarterstaff',
    'sickle':            'Sickle',
    'spear':             'Spear',
    'rapier':            'Rapier',
    'scimitar':          'Scimitar',
    'shortsword':        'Shortsword',
    'trident':           'Trident',
    'war pick':          'War Pick',
    'warhammer':         'Warhammer',
    'whip':              'Whip',

    # unique weapons

    'lilys staff':       'Lily\'s Staff',
    'dangolf staff':     'Dangolf\'s Staff',
    'sif dagger':        'Siffrin\'s Dagger',
    'player sif dagger': 'Siffrin\'s Dagger',

    # No Touchy

    'gun':               'Item Name Error'
}

weapon_print_damage = {
    'empty':             '1',

    'club':              'd4',
    'dagger':            'd4', 
    'great club':        'd4',
    'light hammer':      'd4',
    'sickle':            'd4',
    'whip':              'd4',

    'greatsword':        '2d6',
    'maul':              '2d6',
    'handaxe':           'd6',
    'javelin':           'd6',
    'mace':              'd6',
    'scimitar':          'd6',
    'shortsword':        'd6',
    'spear':             'd6',

    'battle axe':        'd8',
    'flail':             'd8',
    'lance':             'd8',
    'longsword':         'd8',
    'morningstar':       'd8',
    'quarterstaff':      'd8',
    'rapier':            'd8',
    'trident':           'd8',
    'war pick':          'd8',
    'warhammer':         'd8',

    'glaive':            'd10',
    'halberd':           'd10',
    'pike':              'd10',

    'greataxe':          'd12',

    # unique weapons

    'lilys staff':       '5d4',
    'player sif dagger': '5d4',
    'dangolf staff':     '2d6',
    'sif dagger':        '999',

    # No Touchy

    'gun':               '999999'
}


weapon_damage = {
    'empty':             lambda: 1,

    'club':              lambda: d4(),
    'dagger':            lambda: d4(),
    'great club':        lambda: d4(),
    'light hammer':      lambda: d4(),
    'sickle':            lambda: d4(),
    'whip':              lambda: d4(),

    'handaxe':           lambda: d6(),
    'javelin':           lambda: d6(),
    'mace':              lambda: d6(),
    'scimitar':          lambda: d6(),
    'shortsword':        lambda: d6(),
    'spear':             lambda: d6(),
    'greatsword':        lambda: d6(2),
    'maul':              lambda: d6(2),

    'flail':             lambda: d8(),
    'battle axe':        lambda: d8(),
    'lance':             lambda: d8(),
    'longsword':         lambda: d8(),
    'morningstar':       lambda: d8(),
    'quarterstaff':      lambda: d8(),
    'trident':           lambda: d8(),
    'rapier':            lambda: d8(),
    'war pick':          lambda: d8(),
    'warhammer':         lambda: d8(),

    'glaive':            lambda: d10(),
    'halberd':           lambda: d10(),
    'pike':              lambda: d10(),

    'greataxe':          lambda: d12(),


    # unique weapons

    'lilys staff':       lambda: d4(5),
    'player sif dagger': lambda: d4(5),
    'dangolf staff':     lambda: d6(4), 
    'golden spirit':     lambda: d10(2),
    'sif dagger':        lambda: 999, 

    # No Touchy

    'gun':               lambda: 999999,
    'slime':             lambda: d4()
}

weapon_mod = {
    'empty':             'str mod',

    'battle axe':        'str mod',
    'club':              'str mod',
    'flail':             'str mod',
    'glaive':            'str mod',
    'great club':        'str mod',
    'greataxe':          'str mod',
    'greatsword':        'str mod',
    'halberd':           'str mod',
    'handaxe':           'str mod',
    'javelin':           'str mod',
    'lance':             'str mod',
    'light hammer':      'str mod',
    'longsword':         'str mod',
    'mace':              'str mod',
    'maul':              'str mod',
    'morningstar':       'str mod',
    'pike':              'str mod',
    'quarterstaff':      'str mod',
    'sickle':            'str mod',
    'spear':             'str mod',
    'trident':           'str mod',
    'war pick':          'str mod',
    'warhammer':         'str mod',

    'dagger':            'dex mod',
    'scimitar':          'dex mod',
    'shortsword':        'dex mod',
    'rapier':            'dex mod',
    'whip':              'dex mod',

    # unique weapons

    'lilys staff':       'int mod',
    'dangolf staff':     'wis mod',
    'player sif dagger': 'dex mod',

    # No Touchy

    'gun':               99999999,
    'slime':             'end mod'
}

player_equipment = {
    'equipped weapon': 'empty', 'stored weapon 1': 'empty', 'stored weapon 2': 'empty', 'stored weapon 3': 'empty',
    'stored weapon 4': 'empty', 'stored weapon 5': 'empty',
    'equipped armor': '', 'stored armor': '',
    'copper pieces': 0, 'silver pieces': 0,  'gold pieces': 0, 'arrows': 0, 'rope': 0, 'health potion': 0,
    'common keys': 0
}

player_unique_items = []

def unarmored():
    player_ac = 10 + player_mods['dex mod']
    return player_ac

def pickupweapon(weapon):
    print(f'you picked up a {weapon_name[weapon]}')
    while True:
        choice = int_input(f'''Which slot should it be put in?
    1. {weapon_name[player_equipment['stored weapon 1']]} ({weapon_print_damage[player_equipment['stored weapon 1']]})
    2. {weapon_name[player_equipment['stored weapon 2']]} ({weapon_print_damage[player_equipment['stored weapon 2']]})
    3. {weapon_name[player_equipment['stored weapon 3']]} ({weapon_print_damage[player_equipment['stored weapon 3']]})
    4. {weapon_name[player_equipment['stored weapon 4']]} ({weapon_print_damage[player_equipment['stored weapon 4']]})
    5. {weapon_name[player_equipment['stored weapon 5']]} ({weapon_print_damage[player_equipment['stored weapon 5']]})
    6. Throw away (cannot be undone)\n''')
        ynchoice = confirm()
        if ynchoice == True:
            if choice == 1:
                player_equipment['stored weapon 1'] = weapon
                print('You pick up the weapon')
                break
            elif choice == 2:
                player_equipment['stored weapon 2'] = weapon
                print('You pick up the weapon')
                break
            elif choice == 3:
                player_equipment['stored weapon 3'] = weapon
                print('You pick up the weapon')
                break
            elif choice == 4:
                player_equipment['stored weapon 4'] = weapon
                print('You pick up the weapon')
                break
            elif choice == 5:
                player_equipment['stored weapon 5'] = weapon
                print('You pick up the weapon')
                break
            elif choice == 6:
                print('You don\'t pick up the weapon')
                break

            else:
                invalid()



def equip_weapon():
    while True:
        choice = int_input(f'''Which weapon do you want to equip?

current: {weapon_name[player_equipment['equipped weapon']]} ({weapon_print_damage[player_equipment['equipped weapon']]})

    1. {weapon_name[player_equipment['stored weapon 1']]} ({weapon_print_damage[player_equipment['stored weapon 1']]})
    2. {weapon_name[player_equipment['stored weapon 2']]} ({weapon_print_damage[player_equipment['stored weapon 2']]})
    3. {weapon_name[player_equipment['stored weapon 3']]} ({weapon_print_damage[player_equipment['stored weapon 3']]})
    4. {weapon_name[player_equipment['stored weapon 4']]} ({weapon_print_damage[player_equipment['stored weapon 4']]})
    5. {weapon_name[player_equipment['stored weapon 5']]} ({weapon_print_damage[player_equipment['stored weapon 5']]})
    6. Throw away (cannot be undone)\n''')
        ynchoice = confirm()
        if ynchoice == True:
            if choice == 1:
                player_equipment['equipped weapon'] = player_equipment['stored weapon 1']
                player_equipment['stored weapon 1'] = 'empty'
                print(f'You equip {player_equipment["equipped weapon"]}')
                break
            elif choice == 2:
                player_equipment['equipped weapon'] = player_equipment['stored weapon 2']
                player_equipment['stored weapon 2'] = 'empty'
                print(f'You equip {player_equipment["equipped weapon"]}')
                break
            elif choice == 3:
                player_equipment['equipped weapon'] = player_equipment['stored weapon 3']
                player_equipment['stored weapon 3'] = 'empty'
                print(f'You equip {player_equipment["equipped weapon"]}')
                break
            elif choice == 4:
                player_equipment['equipped weapon'] = player_equipment['stored weapon 4']
                player_equipment['stored weapon 4'] = 'empty'
                print(f'You equip {player_equipment["equipped weapon"]}')
                break
            elif choice == 5:
                player_equipment['equipped weapon'] = player_equipment['stored weapon 5']
                player_equipment['stored weapon 5'] = 'empty'
                print(f'You equip {player_equipment["equipped weapon"]}')
                break
            elif choice == 6:
                print('You don\'t equip the weapon')
                break

            else:
                invalid()
        else:
            print()



def pickupitem(item):
    global player_unique_items
    player_unique_items.sort()
    print(f'You picked up {item}')
    print(f'You currently have {len(player_unique_items)} unique items:')
    for x in player_unique_items:
        if x == len(player_unique_items) - 1:
            print(x, end = '.\n')
        else:
            print(x, end = ', ')
    while True:
        try:
            choice = int(input('''Do you want to pick up this item?
    1. Yes
    2. No'''))
        except ValueError:
            invalid()
        else:
            if choice == 1:
                player_unique_items.append(item)
                break
            elif choice == 2:
                break
            else:
                invalid()



def drop_weapon():
    global player_unique_items
    player_unique_items.sort()
    print('Which item?')
    print(f'''
    1.) {weapon_name[player_equipment['stored weapon 1']]}
    2.) {weapon_name[player_equipment['stored weapon 2']]}
    3.) {weapon_name[player_equipment['stored weapon 3']]}
    4.) {weapon_name[player_equipment['stored weapon 4']]}
    5.) {weapon_name[player_equipment['stored weapon 5']]}''')

    while True:
        try:
            dropped_item = int(input('(-1 to quit)'))
        except ValueError:
            invalid()
            continue
        else:
            if dropped_item == -1:
                return
            elif dropped_item == 1:
                player_equipment['stored weapon 1']
            elif dropped_item == 2:
                player_equipment['stored weapon 2']
            elif dropped_item == 3:
                player_equipment['stored weapon 3']
            elif dropped_item == 4:
                player_equipment['stored weapon 4']
            elif dropped_item == 5:
                player_equipment['stored weapon 5']
            else:
                continue
            return


def count_coints():
    global player_equipment
    from items import player_equipment
    while player_equipment['copper pieces'] >= 100:
        player_equipment['copper pieces'] - 100
        player_equipment['silver pieces'] += 1
    
    while player_equipment['silver pieces'] >= 100:
        player_equipment['silver pieces'] - 100
        player_equipment['gold pieces'] += 1
