from dice import *
from player_stats import player_mods
from starting_functions import invalid

weapon_name = {
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

    'dangolf staff':     'Dangolf\'s Staff', 
    'sif dagger':        'Siffrin\'s Dagger', 
    'player sif dagger': 'Siffrin\'s Dagger',

    # No Touchy

    'gun':               'Item Name Error'
}

weapon_print_damage = {
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

    'player sif dagger': '5d4',
    'dangolf staff':     '2d6',
    'sif dagger':        '999',

    # No Touchy

    'gun':               '999999'
}


weapon_damage = {
    'club':              (lambda: d4()),
    'dagger':            (lambda: d4()),
    'great club':        (lambda: d4()),
    'light hammer':      (lambda: d4()),
    'sickle':            (lambda: d4()),
    'whip':              (lambda: d4()),

    'handaxe':           (lambda: d6()),
    'javelin':           (lambda: d6()),
    'mace':              (lambda: d6()),
    'scimitar':          (lambda: d6()),
    'shortsword':        (lambda: d6()),
    'spear':             (lambda: d6()),
    'greatsword':        (lambda: d6(2)),
    'maul':              (lambda: d6(2)),

    'flail':             (lambda: d8()),
    'battle axe':        (lambda: d8()),
    'lance':             (lambda: d8()),
    'longsword':         (lambda: d8()),
    'morningstar':       (lambda: d8()),
    'quarterstaff':      (lambda: d8()),
    'trident':           (lambda: d8()),
    'rapier':            (lambda: d8()),
    'war pick':          (lambda: d8()),
    'warhammer':         (lambda: d8()),

    'glaive':            (lambda: d10()),
    'halberd':           (lambda: d10()),
    'pike':              (lambda: d10()),

    'greataxe':          (lambda: d12()),


    # unique weapons

    'player sif dagger': (lambda: d4(5)),
    'dangolf staff':     (lambda: d6(4)), 
    'golden spirit':     (lambda: d10(2)),
    'sif dagger':        (lambda: 999), 

    # No Touchy

    'gun':               (lambda: 999999)
}

weapon_mod = {
    'battle axe':        player_mods['str mod'],
    'club':              player_mods['str mod'],
    'flail':             player_mods['str mod'],
    'glaive':            player_mods['str mod'],
    'great club':        player_mods['str mod'],
    'greataxe':          player_mods['str mod'],
    'greatsword':        player_mods['str mod'],
    'halberd':           player_mods['str mod'],
    'handaxe':           player_mods['str mod'],
    'javelin':           player_mods['str mod'],
    'lance':             player_mods['str mod'],
    'light hammer':      player_mods['str mod'],
    'longsword':         player_mods['str mod'],
    'mace':              player_mods['str mod'],
    'maul':              player_mods['str mod'],
    'morningstar':       player_mods['str mod'],
    'pike':              player_mods['str mod'],
    'quarterstaff':      player_mods['str mod'],
    'sickle':            player_mods['str mod'],
    'spear':             player_mods['str mod'],
    'trident':           player_mods['str mod'],
    'war pick':          player_mods['str mod'],
    'warhammer':         player_mods['str mod'],

    'dagger':            player_mods['dex mod'],
    'scimitar':          player_mods['dex mod'],
    'shortsword':        player_mods['dex mod'],
    'rapier':            player_mods['dex mod'],
    'whip':              player_mods['dex mod'],

    # unique weapons

    'dangolf staff':     player_mods['wis mod'],
    'player sif dagger': player_mods['dex mod'],

    # No Touchy

    'gun':               99999999
}

npc_weapon_mod = {
    'battle axe':    'str mod',
    'club':          'str mod',
    'flail':         'str mod',
    'glaive':        'str mod',
    'great club':    'str mod',
    'greataxe':      'str mod',
    'greatsword':    'str mod',
    'halberd':       'str mod',
    'handaxe':       'str mod',
    'javelin':       'str mod',
    'lance':         'str mod',
    'light hammer':  'str mod',
    'longsword':     'str mod',
    'mace':          'str mod',
    'maul':          'str mod',
    'morningstar':   'str mod',
    'pike':          'str mod',
    'quarterstaff':  'str mod',
    'sickle':        'str mod',
    'spear':         'str mod',
    'trident':       'str mod',
    'war pick':      'str mod',
    'warhammer':     'str mod',

    'dagger':        'dex mod',
    'rapier':        'dex mod',
    'scimitar':      'dex mod',
    'shortsword':    'dex mod',
    'whip':          'dex mod',

    # unique weapons
    'sif dagger':    'dex mod',
    'dangolf staff': 'wis mod',
    'golden spirit': 'cha mod'
}

player_equipment = {
    'equipped weapon': '', 'stored weapon 1': '', 'stored weapon 2': '', 'stored weapon 3': '', 'stored weapon 4': '', 'stored weapon 5': '',
    'equipped armor': '', 'stored armor': '',
    'copper pieces': 0, 'silver pieces': 0,  'gold pieces': 0, 'arrows': 0, 'rope': 0, 'rocks': 0
}

from player_stats import player_class

if player_class == 'barbarian':
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
    caster = False
        
elif player_class == 'bard':
    while True:
        main = int(input('''Choose your main weapon
    1. '''))
        

        break

    
    caster = True
    player_mods['casting mod'] = player_mods['cha mod']
    
elif player_class == 'cleric':
    caster = True
    player_mods['casting mod'] = player_mods['cha mod']

elif player_class == 'fighter'  :
    caster = False

elif player_class == 'monk':
    caster = False

elif player_class == 'paladin':
    caster = True
    player_mods['casting mod'] = player_mods['cha mod']

elif player_class == 'rogue':
    caster = False

elif player_class == 'sorcerer':
    caster = True
    player_mods['casting mod'] = player_mods['int mod']

elif player_class == 'warlock':
    caster = True
    player_mods['casting mod'] = player_mods['cha mod']

elif player_class == 'wizard':
    caster = True
    player_mods['casting mod'] = player_mods['wis mod']

print(player_equipment['equipped weapon'], player_equipment['stored weapon 1'], player_equipment['stored weapon 2'], player_equipment['equipped armor'])

player_unique_items = []

def unarmored():
    player_ac = 10 + player_mods['dex mod']
    return player_ac

def pickupweapon(weapon):
    print(f'you picked up a {weapon_name[weapon]}')
    while True:
        choice = input(f'''Which slot should it be put in?
    1. {weapon_name[player_equipment['stored weapon 1']]} ({weapon_print_damage[player_equipment['stored weapon 1']]})
    2. {weapon_name[player_equipment['stored weapon 2']]} ({weapon_print_damage[player_equipment['stored weapon 2']]})
    3. {weapon_name[player_equipment['stored weapon 3']]} ({weapon_print_damage[player_equipment['stored weapon 3']]})
    4. {weapon_name[player_equipment['stored weapon 4']]} ({weapon_print_damage[player_equipment['stored weapon 4']]})
    5. {weapon_name[player_equipment['stored weapon 5']]} ({weapon_print_damage[player_equipment['stored weapon 5']]})
    6. Throw away (cannot be undone)\n''')
        try:
            ynchoice = int(input('Are you sure?\n    1.) Yes\n    2.) No'))
        except ValueError:
            invalid()
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

            else:
                invalid()



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



def drop_item():
    global player_unique_items
    player_unique_items.sort()
    print('Which item?')
    if len(player_unique_items) > 0:
        print(f'    1.) {player_unique_items[0]}')
        no_of_items = 1
    if len(player_unique_items) > 1:
        print(f'    2.){player_unique_items[1]}')
        no_of_items = 2
    if len(player_unique_items) > 2:
        print(f'    3.){player_unique_items[2]}')
        no_of_items = 3
    if len(player_unique_items) > 3:
        print(f'    4.){player_unique_items[3]}')
        no_of_items = 4
    if len(player_unique_items) > 4:
        print(f'    5.){player_unique_items[4]}')
        no_of_items = 5
    if len(player_unique_items) > 5:
        print(f'    6.){player_unique_items[5]}')
        no_of_items = 6
    if len(player_unique_items) > 6:
        print(f'    7.){player_unique_items[6]}')
        no_of_items = 7
    if len(player_unique_items) > 7:
        print(f'    8.){player_unique_items[7]}')
        no_of_items = 8
    if len(player_unique_items) > 8:
        print(f'    9.){player_unique_items[8]}')
        no_of_items = 9
    if len(player_unique_items) > 9:
        print(f'    10.){player_unique_items[9]}')
        no_of_items = 10
    if len(player_unique_items) > 10:
        print(f'    11.){player_unique_items[10]}')
        no_of_items = 11
    if len(player_unique_items) > 11:
        print(f'    12.){player_unique_items[11]}')
        no_of_items = 12
    if len(player_unique_items) == 0:
        print('You don\'t have any unique items')
        return None


    while True:
        try:
            dropped_item = int(input())
        except ValueError:
            invalid()
        else:
            if dropped_item == 1:
                player_unique_items.remove(player_unique_items[0])
                break
            elif dropped_item == 2 and no_of_items > 1:
                player_unique_items.remove(player_unique_items[1])
                break
            elif dropped_item == 3 and no_of_items > 2:
                player_unique_items.remove(player_unique_items[2])
                break
            elif dropped_item == 4 and no_of_items > 3:
                player_unique_items.remove(player_unique_items[3])
                break
            elif dropped_item == 5 and no_of_items > 4:
                player_unique_items.remove(player_unique_items[4])
                break
            elif dropped_item == 6 and no_of_items > 5:
                player_unique_items.remove(player_unique_items[5])
                break
            elif dropped_item == 7 and no_of_items > 6:
                player_unique_items.remove(player_unique_items[6])
                break
            elif dropped_item == 8 and no_of_items > 7:
                player_unique_items.remove(player_unique_items[7])
                break
            elif dropped_item == 9 and no_of_items > 8:
                player_unique_items.remove(player_unique_items[8])
                break
            elif dropped_item == 10 and no_of_items > 9:
                player_unique_items.remove(player_unique_items[9])
                break
            elif dropped_item == 11 and no_of_items > 10:
                player_unique_items.remove(player_unique_items[10])
                break
            elif dropped_item == 12 and no_of_items > 11:
                player_unique_items.remove(player_unique_items[11])
                break
            else:
                invalid()