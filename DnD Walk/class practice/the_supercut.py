# Arden Boettcher
# 11/26/24
# DnD walk demo (for class)




from time import sleep
from colorama import Fore
from random import randint



def d100(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 100)
    return roll

def d20(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 20)
    return roll

def d12(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 12)
    return roll

def d10(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 10)
    return roll

def d8(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 8)
    return roll

def d6(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 6)
    return roll

def d4(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 4)
    return roll



# I don't want to type this out every time (or copy-paste)
# better on the fingers to have a tiny function do it
def cont():
    input('Press enter to continue')
    print()


def invalid(): # same use as cont()
    print(Fore.RED + 'Invalid Input: Please try again' + Fore.RESET)
    cont()

def confirm(): # used to confirm user input
    while True: # like if they make an important decision
        try:
            print('''Are you sure?
    1.) Yes
    2.) No''')
            sure = int(input())
        except ValueError:
            invalid()
        else:
            if sure == 1:
                sure = True
            elif sure == 2:
                sure = False
            else:
                invalid()
                continue
            return sure




def rolling(rolling_for = ''): # this is used for drama *jazz hands*
    x =0
    while x <= 3:
        xperiod = x * '.'
        if rolling_for == '':
            print(f'\rRolling{xperiod}',end='')
        else:
            print(f'\rRolling {rolling_for}{xperiod}',end='')
        x += 1
        sleep(1)
    print()

def roll_to_hit(roll, dc, mod): # use this in combat to check if it hit
    rolling('to hit')
    print(f'{roll}')
    if roll + mod >= 20:
        print(Fore.RED + '\n!!!CRITICAL HIT!!!' + Fore.RESET)
        return 'crit'
    elif roll == 1:
        print('\nCritical Fail.')
        return False
    elif roll + mod < dc:
        print('\nFail.')
        return False
    elif roll + mod >= dc:
        print('\nSuccess!')
        return True

def bar(current, total, bar_length = 20, text = 'hp'): # This is a bar for health and other things (I'll see what I use it for)
    fraction = current / total
    extra = ''
    if fraction > 1:
        extra = '░'
        fraction = 1
    arrow = int(fraction * bar_length) * '█' + extra
    padding = int(bar_length - len(arrow)) * '-'
    return f'{arrow}{padding} {round(current)}/{total} {text}'

def int_input(words = ''):
    while True:
        try:
            choice = int(input(words))
        except ValueError:
            invalid()
            continue
        else:
            break
    return choice


karma = 1

luck_bonus = 0

dun_level = 1
difficulty = 1 + (dun_level - 1) / 5

luck = lambda: (karma - 1) * 8 + 10 + luck_bonus
luck_mod = lambda: int((luck() - 10) / 2)

WIDTH = 5
HEIGHT = 5
dun_level = 1


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
    2: 99, # REMOVE AFTER TESTING
}

max_player_spell_slots = { # WIP
    0: -1,
    1: 3,
    2: 99, # REMOVE AFTER TESTING
}




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









# WIP


starting_hit_dice = {
    'barbarian': 12,
    'bard':      8,
    'cleric':    8,
    'fighter':   10,
    'monk':      8,
    'paladin':   10,
    'rogue':     8,
    'sorcerer':  6,
    'warlock':   8,
    'wizard':    6,
}

hit_dice = {
    'barbarian': (lambda: d12()),
    'bard':      (lambda: d8()),
    'cleric':    (lambda: d8()),
    'fighter':   (lambda: d10()),
    'monk':      (lambda: d8()),
    'paladin':   (lambda: d10()),
    'rogue':     (lambda: d8()),
    'sorcerer':  (lambda: d6()),
    'warlock':   (lambda: d8()),
    'wizard':    (lambda: d6()),
}



def skill_save(save_mod, dc):
    save = d20() + save_mod
    print(f'You rolled a {save}')
    if save >= dc:
        print('Success!')
        return True
    elif save < dc:
        print('Failure.')
        return False





goblin = {
    'name': 'Goblin', 'title': '', 'caster': False,
    'health': (lambda: int((d6(1) + 6) * difficulty)), 'weapon': 'dagger', 'ac': 5,
    'exp': int(50), 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1,
    'score': 20
}

kobold = {
    'name': 'Kobold', 'title': '', 'caster': False,
    'health': (lambda: int((d4(4) - 2) * difficulty)), 'weapon': 'dagger', 'ac': 7,
    'exp': int(25), 'agression': 4,
    'str mod': -2, 'dex mod': 2, 'end mod': -1, 'int mod': -1, 'wis mod': -2, 'cha mod': -1,
    'score': 20
}

slime = {
    'name': 'Slime', 'title': '', 'caster': False,
    'health': (lambda: int(d4(2) * difficulty)), 'weapon': 'slime', 'ac': 6,
    'exp': int(26), 'agression': 20,
    'str mod': -4, 'dex mod': -3, 'end mod': 5, 'int mod': -5, 'wis mod': -5, 'cha mod': 1,
    'score': 10
}

la_creatura = {
    'name': 'La Creatura', 'title': '',
    'health': (lambda: int(d4(8) * difficulty)), 'weapon': 'sickle', 'ac': 0,
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
    'health': (lambda: 30 * difficulty), 'weapon': 'golden spirit', 'ac': 12, 'exp': 2000, 'agression': -3,
    'str mod': 5, 'dex mod': 2, 'end mod': 4, 'int mod': 1, 'wis mod': 2, 'cha mod': 10,
    'casting mod': 0
}

# loot tables

def item_pickup(items):
    num = 0
    for drop in items[0]:
        user.equipment[drop] += items[1][num]
        print(f'You picked up {items[1][num]} {drop}')
        num += 1


def common_table(no_of_items, enemy):
    drops = []
    numbers = []
    num = 0
    if enemy == dangolf:
        user.pickupweapon('dangolf staff')

    while num < no_of_items:
        rand = randint(1, 100) + luck_mod()
        if rand < 30:
            drops.append('copper pieces')
            numbers.append(randint(30, 90))
        elif rand > 30 and rand < 50:
            drops.append('arrows')
            numbers.append(randint(1, 10))
        elif rand > 50 and rand < 60:
            drops.append('silver pieces')
            numbers.append(randint(1, 3))
        elif rand > 60 and rand < 75:
            drops.append('health potion')
            numbers.append(1)
        elif rand > 75 and rand < 97:
            drops.append('rope')
            numbers.append(randint(25, 75))
        elif rand > 97:
            drops.append('gold pieces')
            numbers.append(1)
        num += 1
    return drops, numbers, # unique_items






class player:

    def __init__(self, level):
        player.isalive             = True
        player.level               = level
        player.rested              = False
        player.stats               = {'str': 0, 'dex': 0, 'end': 0, 'int': 0, 'wis': 0, 'cha': 0}
        player.damage_increase    = 0
        player.needed_exp          = 100
        player.current_exp         = 0
        player.character_class     = 'fighter'
        player.ac                  = 0
        player.mods                = {}
        player.max_spell_slots     = {0: -1, 1: 3, 2: 99} # REMOVE AFTER TESTING
        player.current_spell_slots = player.max_spell_slots

        player.equipment           = {
    'equipped weapon': 'empty', 'stored weapon 1': 'empty', 'stored weapon 2': 'empty',
    'stored weapon 3': 'empty', 'stored weapon 4': 'empty', 'stored weapon 5': 'empty',
    'equipped armor': '', 'stored armor': '',
    'copper pieces': 0, 'silver pieces': 0,  'gold pieces': 0,
    'arrows': 0, 'rope': 0, 'health potion': 0,
    'common keys': 0}

        player.spells = { # WIP
    0: ['acid splash',   'fire bolt',    'poison spray'],
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





    def define_stats(self):

        is_str_chosen = False
        is_dex_chosen = False
        is_end_chosen = False
        is_int_chosen = False
        is_wis_chosen = False
        is_cha_chosen = False

        stats_choice_num = 0

        while stats_choice_num < 6:

            stat_list = [d6(), d6(), d6(), d6()]
            stat_roll_main= sum(stat_list) - min(stat_list)

            while True:
                try:
                    print(f'You rolled a {Fore.GREEN}{stat_roll_main}{Fore.RESET}!')

                    choice = int(input(f'''{Fore.GREEN}Which stat?{Fore.RESET}
            1. Strength     {self.stats["str"]}
            2. Dexterity    {self.stats["dex"]}
            3. Endurance    {self.stats["end"]}
            4. Inteligence  {self.stats["int"]}
            5. Wisdom       {self.stats["wis"]}
            6. Charisma     {self.stats["cha"]}
        Enter a number 1-6: '''))

                except ValueError:
                    invalid()
                    continue

                else:
                    print()
                    sure = confirm()
                    if sure == False:
                        continue

                if choice == 1 and is_str_chosen == True:
                    print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
                    cont()
                    continue
                elif choice == 1 and is_str_chosen == False:
                    self.stats['str'] = stat_roll_main
                    is_str_chosen = True
                    print(f'Your Strength is now {self.stats["str"]}.')
                    cont()
                    break

                elif choice == 2 and is_dex_chosen == True:
                    print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
                    cont()
                    continue
                elif choice == 2 and is_dex_chosen == False:
                    self.stats["dex"] = stat_roll_main
                    is_dex_chosen = True
                    print(f'Your Dexterity is now {self.stats["dex"]}.')
                    cont()
                    break

                elif choice == 3 and is_end_chosen == True:
                    print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
                    cont()
                    continue
                elif choice == 3 and is_end_chosen == False:
                    self.stats["end"] = stat_roll_main
                    is_end_chosen = True
                    print(f'Your Endurance is now {self.stats["end"]}')
                    cont()
                    break

                elif choice == 4 and is_int_chosen == True:
                    print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
                    cont()
                    continue
                elif choice == 4 and is_int_chosen == False:
                    self.stats["int"] = stat_roll_main
                    is_int_chosen = True
                    print(f'Your Inteligence is now {self.stats["int"]}')
                    cont()
                    break

                elif choice == 5 and is_wis_chosen == True:
                    print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
                    cont()
                    continue
                elif choice == 5 and is_wis_chosen == False:
                    self.stats["wis"] = stat_roll_main
                    is_wis_chosen = True
                    print(f'Your Wisdom is now {self.stats["wis"]}')
                    cont()
                    break

                elif choice == 6 and is_cha_chosen == True:
                    print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
                    cont()
                    continue
                elif choice == 6 and is_cha_chosen == False:
                    self.stats['cha'] = stat_roll_main
                    is_cha_chosen = True
                    print(f'Your charisma is now {self.stats["cha"]}')
                    cont()
                    break

                else:
                    print('Please pick a number between 1 and 6.')
                    continue
            stats_choice_num += 1
        self.mods = {
            'str mod': int((self.stats['str'] - 10) / 2),
            'dex mod': int((self.stats['dex'] - 10) / 2),
            'end mod': int((self.stats['end'] - 10) / 2),
            'int mod': int((self.stats['int'] - 10) / 2),
            'wis mod': int((self.stats['wis'] - 10) / 2),
            'cha mod': int((self.stats['cha'] - 10) / 2),}
        self.ac = 10 + self.mods['dex mod']

        self.health = starting_hit_dice[self.character_class] + self.mods['end mod']
        for x in range(self.level):
            self.health += hit_dice[self.character_class]()
        self.current_health = self.health


    def levelup(self):
        self.level += 1
        self.current_exp -= self.needed_exp
        self.needed_exp *= 1.5
        self.needed_exp = int(self.needed_exp)

        print(Fore.GREEN + 'You Leveled Up!')
        print(f'You are now level {self.level}' + Fore.RESET)
        print(f'{self.needed_exp} exp until next level up.')

        self.health += hit_dice[self.character_class]()
        self.current_health = self.health


        print(f'You now have {self.health} health')

        if self.level % 3 == 0:
            self.damage_increase += 1

        if self.level % 5 == 0:
            while True:
                print('Please pick one stat to increase:')
                num = 0
                for stat in self.stats.keys():
                    num += 1
                    print(f'    {num}.) {stat} ({self.stats[stat]})')
                stat_pick = int_input('>')

                if stat_pick == 1:
                    self.stats['str'] += 1
                    break
                elif stat_pick == 2:
                    self.stats['dex'] += 1
                    break
                elif stat_pick == 3:
                    self.stats['end'] += 1
                    break
                elif stat_pick == 4:
                    self.stats['int'] += 1
                    break
                elif stat_pick == 5:
                    self.stats['wis'] += 1
                    break
                elif stat_pick == 6:
                    self.stats['cha'] += 1
                    break
                else:
                    invalid()
                    continue

        if self.level % 3 == 0:
            player.max_spell_slots[1] += 1
            print('You gained one level 1 spell slot.')
        if self.level % 4 == 0:
            player.max_spell_slots[2] += 1
            print('You gained one level 2 spell slot.')


    def unarmored(self):
        self.ac = 10 + self.mods['dex mod']




# Items

    # Item Management
    def count_coints(self):
        while self.equipment['copper pieces'] >= 100:
            self.equipment['copper pieces'] -= 100
            self.equipment['silver pieces'] += 1

        while self.equipment['silver pieces'] >= 100:
            self.equipment['silver pieces'] -= 100
            self.equipment['gold pieces'] += 1



    def drop_weapon(self):
        print('Which item?')
        print(f'''
        1.) {weapon_name[self.equipment['stored weapon 1']]}
        2.) {weapon_name[self.equipment['stored weapon 2']]}
        3.) {weapon_name[self.equipment['stored weapon 3']]}
        4.) {weapon_name[self.equipment['stored weapon 4']]}
        5.) {weapon_name[self.equipment['stored weapon 5']]}''')

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
                    self.equipment['stored weapon 1']
                elif dropped_item == 2:
                    self.equipment['stored weapon 2']
                elif dropped_item == 3:
                    self.equipment['stored weapon 3']
                elif dropped_item == 4:
                    self.equipment['stored weapon 4']
                elif dropped_item == 5:
                    self.equipment['stored weapon 5']
                else:
                    continue
                return


    def pickupweapon(self, weapon):
        print(f'you picked up a {weapon_name[weapon]}')
        while True:
            choice = int_input(f'''Which slot should it be put in?
        1. {weapon_name[self.equipment['stored weapon 1']]} ({weapon_print_damage[self.equipment['stored weapon 1']]})
        2. {weapon_name[self.equipment['stored weapon 2']]} ({weapon_print_damage[self.equipment['stored weapon 2']]})
        3. {weapon_name[self.equipment['stored weapon 3']]} ({weapon_print_damage[self.equipment['stored weapon 3']]})
        4. {weapon_name[self.equipment['stored weapon 4']]} ({weapon_print_damage[self.equipment['stored weapon 4']]})
        5. {weapon_name[self.equipment['stored weapon 5']]} ({weapon_print_damage[self.equipment['stored weapon 5']]})
        6. Throw away (cannot be undone)\n''')
            ynchoice = confirm()
            if ynchoice == True:
                if choice == 1:
                    self.equipment['stored weapon 1'] = weapon
                    print('You pick up the weapon')
                    break
                elif choice == 2:
                    self.equipment['stored weapon 2'] = weapon
                    print('You pick up the weapon')
                    break
                elif choice == 3:
                    self.equipment['stored weapon 3'] = weapon
                    print('You pick up the weapon')
                    break
                elif choice == 4:
                    self.equipment['stored weapon 4'] = weapon
                    print('You pick up the weapon')
                    break
                elif choice == 5:
                    self.equipment['stored weapon 5'] = weapon
                    print('You pick up the weapon')
                    break
                elif choice == 6:
                    print('You don\'t pick up the weapon')
                    break

                else:
                    invalid()


    def equip_weapon(self):

        while True:
            choice = int_input(f'''Which weapon do you want to equip?

    current: {weapon_name[self.equipment['equipped weapon']]} ({weapon_print_damage[self.equipment['equipped weapon']]})

        1. {weapon_name[self.equipment['stored weapon 1']]} ({weapon_print_damage[self.equipment['stored weapon 1']]})
        2. {weapon_name[self.equipment['stored weapon 2']]} ({weapon_print_damage[self.equipment['stored weapon 2']]})
        3. {weapon_name[self.equipment['stored weapon 3']]} ({weapon_print_damage[self.equipment['stored weapon 3']]})
        4. {weapon_name[self.equipment['stored weapon 4']]} ({weapon_print_damage[self.equipment['stored weapon 4']]})
        5. {weapon_name[self.equipment['stored weapon 5']]} ({weapon_print_damage[self.equipment['stored weapon 5']]})
        6. Throw away (cannot be undone)\n''')
            ynchoice = confirm()
            if ynchoice == True:
                if choice == 1:
                    var = self.equipment['equipped weapon']
                    self.equipment['equipped weapon'] = self.equipment['stored weapon 1']
                    self.equipment['stored weapon 1'] = var
                    print(f'You equip {self.equipment["equipped weapon"]}')
                    break
                elif choice == 2:
                    var = self.equipment['equipped weapon']
                    self.equipment['equipped weapon'] = self.equipment['stored weapon 2']
                    self.equipment['stored weapon 2'] = var
                    print(f'You equip {self.equipment["equipped weapon"]}')
                    break
                elif choice == 3:
                    var = self.equipment['equipped weapon']
                    self.equipment['equipped weapon'] = self.equipment['stored weapon 3']
                    self.equipment['stored weapon 3'] = var
                    print(f'You equip {self.equipment["equipped weapon"]}')
                    break
                elif choice == 4:
                    var = self.equipment['equipped weapon']
                    self.equipment['equipped weapon'] = self.equipment['stored weapon 4']
                    self.equipment['stored weapon 4'] = var
                    print(f'You equip {self.equipment["equipped weapon"]}')
                    break
                elif choice == 5:
                    var = self.equipment['equipped weapon']
                    self.equipment['equipped weapon'] = self.equipment['stored weapon 5']
                    self.equipment['stored weapon 5'] = var
                    print(f'You equip {self.equipment["equipped weapon"]}')
                    break
                elif choice == 6:
                    print('You don\'t equip the weapon')
                    break

                else:
                    invalid()
            else:
                print()


    # Items Menu

    def rest_items_menu(self):
        print()
        print('What do you want to do?')
        while True:
            print('''    1.) Veiw all items
        2.) Drop Item
        3.) Use Potion
        4.) Equip Weapon
        5.) Exit''')
            items_choice = int_input()
            if items_choice == 5:
                return
            elif items_choice == 1:
                self.count_coints()
                print(f'''
weapons:
Equipped: {weapon_name[self.equipment['equipped weapon']]}    damage: {weapon_print_damage[self.equipment['equipped weapon']]}
Stored 1: {weapon_name[self.equipment['stored weapon 1']]}    damage: {weapon_print_damage[self.equipment['stored weapon 1']]}
Stored 2: {weapon_name[self.equipment['stored weapon 2']]}    damage: {weapon_print_damage[self.equipment['stored weapon 2']]}
Stored 3: {weapon_name[self.equipment['stored weapon 3']]}    damage: {weapon_print_damage[self.equipment['stored weapon 3']]}
Stored 4: {weapon_name[self.equipment['stored weapon 4']]}    damage: {weapon_print_damage[self.equipment['stored weapon 4']]}
Stored 5: {weapon_name[self.equipment['stored weapon 5']]}    damage: {weapon_print_damage[self.equipment['stored weapon 5']]}

items:
Copper Pieces:  {self.equipment['copper pieces']}
Silver Pieces:  {self.equipment['silver pieces']}
Gold Pieces:    {self.equipment['gold pieces']}
Health Potions: {self.equipment['health potion']}
''')
                cont()
                continue
            elif items_choice == 2:
                self.drop_weapon()
                continue
            elif items_choice == 3:
                print('Use Health Potion? (2d4)')
                if self.equipment['health potion'] == 0:
                    print('You don\'t have any potions')
                    continue
                while True:
                    confirm = int_input('''    1.) Yes
        2.) No
    ''')
                    if confirm == 1:
                        if self.current_health == self.health:
                            print('You already have full health.')
                            user.current_health = self.health
                            break

                        health_potion = d4(2)
                        self.current_health += health_potion
                        if self.current_health >= self.health:
                            self.current_health = self.health
                        print(f'You gained {health_potion} health.')
                        bar(self.current_health, self.health, 15)
                        self.equipment['health potion'] -= 1
                        break
                    elif confirm == 2:
                        break
                    else:
                        invalid()
                        continue

            elif items_choice == 4:
                self.equip_weapon()
            else:
                invalid()
                continue



    def rest_spells_menu(self):

        print('Current/Max Spell Slots:')
        for spell_level in self.max_spell_slots.keys():
            print(f'level {spell_level}: {self.current_spell_slots[spell_level]}/{self.max_spell_slots[spell_level]}')
        while True:
            num = 0
            print('See spell descriptions (-1 to exit)')
            for spell_level in self.max_spell_slots.keys():
                num += 1
                print(f'    {spell_level}.) {", ".join(self.spells[spell_level])}')

            spell_level = int_input()

            if spell_level == -1:
                return
            elif spell_level not in range(num + 1):
                continue

            num1 = 0
            for spell in self.spells[spell_level]:
                num1 += 1
                print(f'''    {num1}.) {spell_descriptions[spell]}\n''')
            cont()



    def stats_menu(self):
        print('Stats:')
        print(f'''
Strength:       {self.stats["str"]}     modifier: {self.mods["str mod"]}
Dexterity:      {self.stats["dex"]}     modifier: {self.mods["dex mod"]}
Endurance:      {self.stats["end"]}     modifier: {self.mods["end mod"]}
Inteligence:    {self.stats["int"]}     modifier: {self.mods["int mod"]}
Wisdom:         {self.stats["wis"]}     modifier: {self.mods["wis mod"]}
Charisma:       {self.stats["cha"]}     modifier: {self.mods["cha mod"]}

Health {self.current_health}/{self.health}
    {bar(self.current_health, self.health, 15)}''')
        cont()


# Main Rest method

    def rest(self, menu):

        if menu: # This checks if you are rested or if you're just using the menu
                 # If you are using the menu it ignores the rest of the statement
            pass
        elif self.rested == True:
            print('Since you already rested on this floor you don\'t get any health back')
        else:
            print('You have been restored to full health')
            print('and your spell slots have been restored')
            self.current_health = self.health
            self.current_spell_slots = self.max_spell_slots
            self.rested = True

        print()

        while True:
            print('Options')
            print(f'''    1.) Items
        2.) Stats
        3.) Spells
        4.) back''')
            rest_choice = int_input()
            if rest_choice == 4:
                return
            elif rest_choice == 1:
                self.rest_items_menu()
                continue
            elif rest_choice == 2:
                self.stats_menu()
            elif rest_choice == 3:
                self.rest_spells_menu()






user = player(3)





spell_descriptions = {
    'acid splash': f'''{Fore.GREEN}Acid Splash, cantrip, single, {1 + user.damage_increase}d6{Fore.RESET}
details: You swing a bubble of acid towards an enemy
dealing {1 + user.damage_increase}d6 damage''',

    'fire bolt': f'''{Fore.GREEN}Fire Bolt, cantrip, single, {1 + user.damage_increase}d10{Fore.RESET}
details: You throw a small ball of fire towards one
unlucky enemy damaging it for {1 + user.damage_increase}d10 fire damage on a
failed dexterity save and half that on a success.''',

    'poison spray': f'''{Fore.GREEN}Poison Spray, cantrip, single, {1 + user.damage_increase}d6{Fore.RESET}
details: You send a puff of noxious gas towards two random
enemies, they take {1 + user.damage_increase}d6 damage on a failed constitution
save and half that on a success.''',

    'healing word': f'''{Fore.GREEN}Healing Word, level 1, healing, {2 + int(user.damage_increase / 2)}d4{Fore.RESET}
details: You speak a word commading the arcane to
heal the desired wound restoring {2 + int(user.damage_increase / 2)}d4 health.''',

    'burning hands': f'''{Fore.GREEN}Burning Hands, level 1, AOE, {3 + user.damage_increase}d6 {Fore.RESET}
details: You spread your fingers sending out a wave
of flame hitting 3 adjacent enemies for {3 + user.damage_increase}d6.''',

    'magic missile': f'''{Fore.GREEN}Magic Missile, level 1, multi-hit, {1 + int(user.damage_increase / 2)}d4 + 1 {Fore.RESET}
details: You fire three homing bolts of glowing blue
magic dealing {1 + int(user.damage_increase / 2)}d4 + {user.damage_increase} to three enemies of your choice.''',

    'fireball': f'''{Fore.GREEN}Fireball, level 2, AOE, {8 + int(user.damage_increase / 2)}d6 {Fore.RESET}
details : You throw a hurtling ball of fire that
explodes on contact dealing {8 + int(user.damage_increase / 2)}d6 to all enemies.'''
}



def spells_menu():

    while True:
        print('Spells:')

        num = 0
        for spell_level in user.spells.keys():
            if user.spells[spell_level] == []:
                continue
            print(f'    {num}.) {print_spell_level[num]}: {", ".join(user.spells[spell_level])} (spell slots: {current_player_spell_slots[spell_level]})')
            num += 1

        spell_level = int_input('Choose a spell level (-1 to go back): ')
        print()

        if current_player_spell_slots[spell_level] <= 0:
            print('You don\'t have enough spell slots to cast that')
            continue

        if spell_level == -1:
            return False
        elif spell_level in range(num):

            if spell_level != 0:
                print(f'You have {current_player_spell_slots[spell_level]} {print_spell_level[spell_level]} spell slots')
            print('Which spell?: ')

            while True:

                num = 0
                for spell in user.spells[spell_level]:
                    num += 1
                    print(f'    {num}.) {spell}')
                spell_choice = input('type description for spell descriptions: ')
                if spell_choice == 'description':
                    num1 = 0
                    for spell in user.spells[spell_level]:
                        num1 += 1
                        print(f'''    {num1}.) {spell_descriptions[spell]}''')
                    cont()
                    continue

                try:
                    spell_choice = int(spell_choice)
                except ValueError:
                    invalid()
                    continue

                if spell_choice in range(1, len(user.spells[spell_level]) + 1):
                    break
                else:
                    invalid()
                    continue

            if spell_choice == -1:
                continue
            elif spell_choice in range(1, num + 1):
                current_player_spell_slots[spell_level] -= 1
                return user.spells[spell_level][spell_choice - 1]
            else:
                invalid()
                continue

        else:
            invalid()
            continue


def cast(spell, enemies): # WIP
    if spell == 'acid splash':
        return cast_acid_splash(enemies)

    elif spell == 'poison spray':
        return cast_poison_spray(enemies)

    elif spell == 'fire bolt':
        return cast_fire_bolt(enemies)

    elif spell == 'healing word':
        current_player_spell_slots[1] - 1
        return cast_healing_word(enemies)

    elif spell == 'magic missile':
        current_player_spell_slots[1] - 1
        return cast_magic_missile(enemies)

    elif spell == 'burning hands':
        current_player_spell_slots[1] - 1
        return cast_burning_hands(enemies)

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
    dictionary = {choice: d6(1 + user.damage_increase)}
    return dictionary

def cast_magic_missile(enemies):
    print('You cast Magic Missile')
    choice = []
    num = 1

    while num <= 3:
        var = 0
        for enemy in enemies:
            var += 1
            print(f'{var}.) {enemy["name"]}')

        temp_choice = int_input(f'Which enemy do you attack? {num}/3: ')
        if temp_choice in range(1, var + 1):
            choice.append(temp_choice)
            num += 1
            continue
        else:
            invalid()
            continue

    dictionary = {}
    for target in choice:
        dictionary[target] = 0
    for target in choice:
        damage = lambda: d4(1 + int(user.damage_increase / 2) + 1)
        dictionary[target] += damage()
    return dictionary

def cast_burning_hands(enemies):
    print('You cast Burning Hands')
    var = 0
    while True:
        for enemy in enemies:
            var += 1
            print(f'{var}.) {enemy["name"]}')

        choice1 = int_input(f'Which enemy do you attack?: ')
        if choice1 in range(1, len(enemies) + 1):
            choice0 = choice1 - 1
            choice2 = choice1 + 1
            break
        else:
            invalid()
            continue

    dictionary = {choice1: d6(3 + user.damage_increase)}
    if choice0 >= 1:
        dictionary[choice0] = d6(3 + user.damage_increase)
    if choice2 <= len(enemies):
        dictionary[choice2] = d6(3 + user.damage_increase)
    return dictionary

def cast_poison_spray(enemies):
    print('You cast Poison Spray')
    choice1 = randint(1, len(enemies))

    rolling('Enemy Dex Save')
    enemy_save = skill_save(enemies[choice1 - 1]['dex mod'], 10 + (user.damage_increase - 1))
    if enemy_save == True:
        dictionary = {choice1: d10(1 + user.damage_increase) / 2}
    elif enemy_save == False:
        dictionary = {choice1: d10(1 + user.damage_increase)}

    if len(enemies) == 1:
        return dictionary

    choice2 = randint(1, len(enemies))
    while choice1 == choice2:
        choice2 = randint(1, len(enemies))

    enemy_save = skill_save(enemies[choice2 - 1]['dex mod'], 10 + (user.damage_increase - 1))
    if enemy_save == True:
        dictionary += {choice2: d10(1 + user.damage_increase) / 2}
    elif enemy_save == False:
        dictionary += {choice2: d10(1 + user.damage_increase)}

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
    enemy_save = skill_save(enemies[choice - 1]['dex mod'], 10 + (user.damage_increase - 1))
    if enemy_save == True:
        dictionary = {choice: d10(1 + user.damage_increase) / 2}
    elif enemy_save == False:
        dictionary = {choice: d10(1 + user.damage_increase)}
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
    dictionary = {choice: d4(2 + int(user.damage_increase / 2)) * -1}
    return dictionary


def cast_fireball(enemies):
    print('You cast Fireball.')
    cont()
    dictionary = {1: d6(8), 2: d6(8), 3: d6(8), 4: d6(8)}
    return dictionary




def roll_against(agressor_mod, agressor, defender, defender_mod):
    agressor_roll = d20() + agressor[agressor_mod]
    defender_roll = d20() + defender[defender_mod]
    if agressor_roll > defender_roll:
        return True
    elif agressor_roll < defender_roll:
        return False




def damage_over_time(target, duration, damage, damage_type = ''):
    print('dnd\'s mechanics are going to be my 13 reason.')
    # I'm not finishing some things because I don't need to ¯\_(ツ)_/¯



def npc_attack(tohit, weapon, enemy):
    if tohit == 'crit':
        print('\nCritical Hit!')
        damage = weapon_damage[weapon]() + enemy[weapon_mod[weapon]] * 2
        cont()
        return damage
    elif tohit == True:
        print('\nAttack hit.')
        cont()
        return weapon_damage[weapon]() + enemy[weapon_mod[weapon]]
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
        return weapon_damage[weapon]() + user.mods[weapon_mod[weapon]] * 2
    elif tohit == True:
        print('\nYour attack hit.')
        cont()
        return weapon_damage[weapon]() + user.mods[weapon_mod[weapon]]
    elif tohit == False:
        print('\nYou missed.')
        cont()
        return 0
    else:
        print('\nYou missed.')
        cont()
        return 0





def npc_turn(enemy, current_health, blocking):
    print('It\'s ' + enemy['name'] + '\'s turn')
    cont()

    roll = d10() + enemy['agression']

    if roll > 6:
        print(enemy['name'] + ' is attacking.\n')

        damage = npc_attack(roll_to_hit(d20(), user.ac, enemy[weapon_mod[enemy['weapon']]]), enemy['weapon'], enemy)
        damage = round(damage * blocking)

        if damage > 50:
            print(f'You took {Fore.RED}{damage}{Fore.RESET} damage.')
        else:
            print(f'You took {damage} damage.')
            print()
        return 1, damage

    elif roll <= 6:
        print(enemy['name'] + ' is blocking.')
        cont()
        return 0.5, 0




def player_turn(no_of_enemy, enemy1, enemy2, enemy3, enemy4):
    while True:
        while True:
            print('Your turn.\n')
            print(f'''Player Stats
    Level.............{user.level}
    Weapon............{weapon_name[user.equipment["equipped weapon"]]} ({weapon_print_damage[user.equipment['equipped weapon']]})
    Health {bar(user.current_health, user.health, 20)}''')
            try:
                player_turn = int(input(f'''
    1. Attack
    2. Cast
    3. Block\n'''))
            except ValueError:
                invalid()
            else:
                if player_turn in range(1, 4):
                    break
                else:
                    invalid()

        if player_turn == 1:
            while True:
                enemies = [enemy1, enemy2, enemy3, enemy4]
                for num in range(1, no_of_enemy + 1):
                    if enemies[num - 1] != '':
                        print(f'{num}.) {enemies[num - 1]["name"]}')
                choice = int_input('Which enemy?: ')
                print()



                if choice == 1:
                    damage =  attack(roll_to_hit(d20(), enemy1['ac'], user.mods[weapon_mod[user.equipment['equipped weapon']]]), user.equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy1["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy1["name"]} for {damage}')
                    return 'attack', damage, enemy1['name']

                elif choice == 2:
                    damage =  attack(roll_to_hit(d20(), enemy2['ac'], user.mods[weapon_mod[user.equipment['equipped weapon']]]), user.equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy2["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy2["name"]} for {damage}')
                    return 'attack', damage, enemy2['name']

                elif choice == 3:
                    damage =  attack(roll_to_hit(d20(), enemy3['ac'], user.mods[weapon_mod[user.equipment['equipped weapon']]]), user.equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy3["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy3["name"]} for {damage}')
                    return 'attack', damage, enemy3['name']

                elif choice == 4:
                    damage =  attack(roll_to_hit(d20(), enemy4['ac'], user.mods[weapon_mod[user.equipment['equipped weapon']]]), user.equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy4["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy4["name"]} for {damage}')
                    return 'attack', damage, enemy4['name']

                else:
                    print(f'{Fore.RED}Please enter a valid number.{Fore.RESET}')

        elif player_turn == 2:
            spell = spells_menu()
            if spell == -1:
                continue
            else:

                enemies = []
                for enemy in [enemy1, enemy2, enemy3, enemy4]:
                    if enemy == "":
                        continue
                    elif enemy != "":
                        enemies.append(enemy)
                casting = cast(spell, enemies)
                return 'cast', casting



        elif player_turn == 3:
            print('You are blocking.')
            return 'block', 0, ''



# If it ain't broke don't fix it
player_dict = {'initiative': 0, 'name': 'You'}

def fight(enemy1_og, enemy2_og = '', enemy3_og = '', enemy4_og = ''):
    no_of_turns = 0
    exp = 0

    rolling('for Initiative')
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
    enemy2 = ''
    enemy3 = ''
    enemy4 = ''


    enemy1 = dict(enemy1_og)
    no_of_enemy = 1
    enemy1_is_alive = True
    enemy1_health = enemy1['health']()
    initiative.insert(randint(0, len(initiative)), enemy1)

    if enemy2_og != '':
        enemy2 = dict(enemy2_og)
        num = 0
        while enemy2 in initiative:
            num += 1
            enemy2['name'] = enemy2_og['name'] + ' ' + str(num)
        enemy2_is_alive = True
        enemy2_health = enemy2['health']()
        no_of_enemy += 1
        initiative.insert(randint(0, len(initiative)), enemy2)

    if enemy3_og != '':
        enemy3 = dict(enemy3_og)
        num = 0
        while enemy2 in initiative:
            num += 1
            enemy3['name'] = enemy3_og['name'] + ' ' + str(num)
        enemy3_is_alive = True
        enemy3_health = enemy3['health']()
        no_of_enemy += 1
        initiative.insert(randint(0, len(initiative)), enemy3)

    if enemy4_og != '':
        enemy4 = dict(enemy4_og)
        num = 0
        while enemy4 in initiative:
            num += 1
            enemy4['name'] = enemy4_og['name'] + ' ' + str(num)
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
    cont()

    while no_of_enemy > 0 and user.current_health > 0:
        if user.current_health <= 0:
            break
        blocking = 1

        for turn in initiative:
            no_of_turns += 1
            if user.current_health <= 0:
                break

            if turn == player_dict:

                player = player_turn(no_of_enemy, enemy1, enemy2, enemy3, enemy4)

                if player[0] == 'block':
                    blocking = 0.25
                elif player[0] == 'attack':
                    blocking = 1
                    if player[2] == enemy1['name']:
                        enemy1_health -= player[1] * enemy1_blocking
                    elif player[2] == enemy2['name']:
                        enemy2_health -= player[1] * enemy2_blocking
                    elif player[2] == enemy3['name']:
                        enemy3_health -= player[1] * enemy3_blocking
                    elif player[2] == enemy4['name']:
                        enemy4_health -= player[1] * enemy4_blocking

                elif player[0] == 'cast':
                    blocking = 1

                    # I have it in a for loop so it can hit a single target multiple times
                    # (magic missile)
                    for target in player[1].keys():
                        if target == 0:
                            damage = player[1][1]()
                            user.current_health -= damage
                            if damage < 0:
                                print(f'You restored {Fore.GREEN}{damage}{Fore.RESET} health.')
                            else:
                                print(f'You took {damage} damage.')

                            if user.current_health > user.health:
                                user.current_health = user.health

                        if target == 1 and enemy1_is_alive:
                            spell_damage = player[1][target]
                            spell_damage = spell_damage * enemy1_blocking
                            enemy1_health -= spell_damage
                            print(f'{enemy1["name"]} took {spell_damage} damage.')

                        if target == 2 and enemy2_is_alive:
                            spell_damage = player[1][target]
                            spell_damage = spell_damage * enemy2_blocking
                            enemy2_health -= spell_damage
                            print(f'{enemy2["name"]} took {spell_damage} damage.')

                        if target == 3 and enemy3_is_alive:
                            spell_damage = player[1][target]
                            spell_damage = spell_damage * enemy3_blocking
                            enemy3_health -= spell_damage
                            print(f'{enemy3["name"]} took {spell_damage} damage.')

                        if target == 4 and enemy4_is_alive:
                            spell_damage = player[1][target]
                            spell_damage = spell_damage * enemy4_blocking
                            enemy4_health -= spell_damage
                            print(f'{enemy4["name"]} took {spell_damage} damage.')


                if enemy1_health <= 0 and enemy1_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy1["name"]}{Fore.RESET}')
                    enemy1_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy1['exp']
                    print('+', enemy1['exp'], 'exp')
                    item_pickup(common_table(2, enemy1))
                    cont()

                if enemy2_health <= 0 and enemy2_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy2["name"]}{Fore.RESET}')
                    enemy2_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy2['exp']
                    print('+', enemy2['exp'], 'exp')
                    item_pickup(common_table(2, enemy2))
                    cont()

                if enemy3_health <= 0 and enemy3_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy3["name"]}{Fore.RESET}')
                    enemy3_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy3['exp']
                    print('+', enemy3['exp'], 'exp')
                    item_pickup(common_table(2, enemy3))
                    cont()

                if enemy4_health <= 0 and enemy4_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy4["name"]}{Fore.RESET}')
                    enemy4_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy4['exp']
                    print('+', enemy4['exp'], 'exp')
                    item_pickup(common_table(2, enemy4))
                    cont()


            elif turn == enemy1 and enemy1_is_alive:
                enemy1_turn = npc_turn(enemy1, enemy1_health, blocking)
                enemy1_blocking = enemy1_turn[0]
                damage = enemy1_turn[1] * blocking
                user.current_health -= damage
                if damage != 0:
                    print(f'You took {damage} damage.')

            elif turn == enemy2 and enemy2_is_alive:
                enemy2_turn = npc_turn(enemy2, enemy2_health, blocking)
                enemy2_blocking = enemy2_turn[0]
                damage = enemy2_turn[1] * blocking
                user.current_health -= damage
                if damage != 0:
                    print(f'You took {damage} damage.')

            elif turn == enemy3 and enemy3_is_alive:
                enemy3_turn = npc_turn(enemy3, enemy3_health, blocking)
                enemy3_blocking = enemy3_turn[0]
                damage = enemy3_turn[1] * blocking
                user.current_health -= damage
                if damage != 0:
                    print(f'You took {damage} damage.')

            elif turn == enemy4 and enemy4_is_alive:
                enemy4_turn = npc_turn(enemy4, enemy4_health, blocking)
                enemy4_blocking = enemy4_turn[0]
                damage = enemy4_turn[1] * blocking
                user.current_health -= damage
                if damage != 0:
                    print(f'You took {damage} damage.')

    if user.current_health <= 0:
        global player_is_alive
        print(Fore.RED + 'You Died.' + Fore.RESET)
        player_is_alive = False
        return False

    elif no_of_enemy == 0:
        print(Fore.GREEN + 'You Won!' + Fore.RESET)
        print(f'You gained {exp} exp')
        user.exp += exp
        print(bar(user.exp, user.needed_exp, 15, 'exp'))
        return True




def make_dungeon():
    dungeon = []
    for row in range(WIDTH):
        dungeon.append([])

        for column in range(HEIGHT):
            type = randint(1, 25)

            if type <= 4:
                encounter_type_num = randint(1, 100)
                encounter_type = 'goblin'
                if encounter_type_num <= 20:
                    encounter_type = 'goblin'
                elif encounter_type_num > 20 and encounter_type_num <= 40:
                    encounter_type = 'kobold'
                elif encounter_type_num > 40 and encounter_type_num <= 50:
                    encounter_type = 'slime'
                elif encounter_type_num > 50 and encounter_type_num <= 70:
                    encounter_type = 'mixed'
                elif encounter_type_num > 70 and encounter_type_num <= 80:
                    encounter_type = 'la creatura'
                elif encounter_type_num > 80 and encounter_type_num <= 85:
                    encounter_type = 'kyle'
                elif encounter_type_num > 85 and encounter_type_num <= 90:
                    encounter_type = 'gronk'
                elif encounter_type_num > 90 and encounter_type_num <= 96 and difficulty >= 3:
                    encounter_type = 'dangolf'
                elif encounter_type_num > 96 and encounter_type_num <= 99:
                    encounter_type = 'siffrin traveler'
                elif encounter_type_num == 100 and difficulty >= 5:
                    encounter_type = 'siffrin lost'
                else:
                    encounter_type = 'slime'

                dungeon[row].append(['encounter', encounter_type, False, True])

            elif 4 < type <= 6:
                dungeon[row].append(['chest', None, False, True])

            elif 6 < type <= 8:
                trap_type_rand = randint(1, 10)
                if trap_type_rand <= 5:
                    trap_type = 'dart'
                elif 5 < trap_type_rand <= 10:
                    trap_type = 'spike'
                dungeon[row].append(['trap', trap_type, False, True])

            else:
                dungeon[row].append(['empty', None, False, True])

    def find_entrance(dungeon):
        while True:
            for row in dungeon:
                for column in row:
                    if column[0] == 'empty':
                        entrance_rand = randint(1, 25)
                        if entrance_rand == 1:
                            column[0] = 'entrance'
                            column[2] = True
                            column[3] = False
                            return dungeon

    def find_exit(dungeon):
        while True:
            for row in dungeon:
                for column in row:
                    if column[0] == 'empty':
                        entrance_rand = randint(1, 25)
                        if entrance_rand == 1:
                            column[0] = 'exit'
                            return dungeon

    dungeon = find_entrance(dungeon)
    dungeon = find_exit(dungeon)

    return dungeon


def print_dungeon(dungeon):
    print(f'Floor {dun_level}')
    print(f'Difficulty: {difficulty}')
    printing_dungeon = ''
    for row in dungeon:
        for column in row:
            if column[2] == True:
                printing_dungeon += f'{Fore.GREEN}+{Fore.RESET}'
            elif column[3]:
                printing_dungeon += '█'
            elif column[0] == 'empty':
                printing_dungeon += '·'
            elif column[0] == 'exit':
                printing_dungeon += 'E'
            elif column[0] == 'encounter':
                printing_dungeon += 'F'
            elif column[0] == 'chest':
                printing_dungeon += 'C'
            elif column[0] == 'trap':
                printing_dungeon += 'T'
            elif column[0] == 'entrance':
                printing_dungeon += 'e'
        printing_dungeon += '\n'
    print(printing_dungeon)





def dungeon_encounters(column):
    if column[1] == 'goblin':
        no_of_enemies = randint(2, 4)
        if no_of_enemies == 2:
            encounter = fight(goblin, goblin)
        elif no_of_enemies == 3:
            encounter = fight(goblin, goblin, goblin)
        elif no_of_enemies == 4:
            encounter = fight(goblin, goblin, goblin, goblin)

    elif column[1] == 'kobold':
        no_of_enemies = randint(3, 4)
        if no_of_enemies == 3:
            encounter = fight(kobold, kobold, kobold)
        elif no_of_enemies == 4:
            encounter = fight(kobold, kobold, kobold, kobold)

    elif column[1] == 'slime':
        no_of_enemies = randint(1, 4)
        if no_of_enemies == 1:
            encounter = fight(slime)
        elif no_of_enemies == 2:
            encounter = fight(slime, slime)
        elif no_of_enemies == 3:
            encounter = fight(slime, slime, slime)
        elif no_of_enemies == 4:
            encounter = fight(slime, slime, slime, slime)

    elif column[1] == 'mixed':
        encounter = fight(goblin, kobold, slime)

    elif column[1] == 'la cretura':
        encounter = fight(la_creatura, slime)

    elif column[1] == 'kyle':
        print('You walk into a room, and you see a person standing there like a weirdo.')
        print('He asks you "Is K?le spelled with an I or a Y?".')

        while True:
            answer = int_input('''    1.) "With an I!"
        2.) "With a Y!"
    > ''')
            if answer == 1:
                print('He gets visibly angry with your answer and he charges at you with his sword drawn.')
                encounter = fight(kyle)
                break
            elif answer == 2:
                print('He gets visibly angry with your answer and he charges at you with his sword drawn.')
                encounter = fight(kile)
                break
            else:
                invalid()

    elif column[1] == 'gronk':
        encounter = fight(gronk, lily)

    elif column[1] == 'dangolf':
        encounter = fight(dangolf)

    elif column[1] == 'siffrin traveler':
        encounter = fight(siffrin_traveler)

    elif column[1] == 'siffrin lost':
        encounter = fight(siffrin_lost)

    else:
        encounter = fight(goblin, goblin)

    return encounter



def dungeon_trap(column):
    damage = 0

    if column[3] == False:
        print('You\'ve been here before')
        return 0

    rolling('')
    wis_save = skill_save(user.mods['wis mod'], 10 + int(difficulty / 2))

    if column == 'dart':
        int_save = False
        if wis_save == True:

            print()
            print('You spot small holes in the walls.')
            print('You know from experience that this is a dart trap.')
            print('Unfortunately the door to the previous room has closed.')
            print('The only way forward is to defuse it.\n')
            cont()

            rolling('Intelegence Save')
            int_save = skill_save(user.mods['int mod'], 10 + int(difficulty / 3))

            if int_save == True:
                print('You manage to defuse the trap, letting you move forward.')
                return damage

        if wis_save == False or int_save == False:
            print('The dart trap inside of the room goes off!')
            rolling('Dexterity Save')
            dex_save = skill_save(user.mods['dex mod'], 10 + int(difficulty / 2))
            if dex_save == True:
                damage = d4()
                print('You managed to dodge the majority of the darts!')
                print(f'You only took {damage} damage.')
                cont()
            elif dex_save == False:
                damage = d4(3)
                print('You don\'t manage to react in time.')
                print(f'You took {damage} damage.')
                cont()
        return damage

    elif column == 'spike':
        if wis_save == True:

            print()
            print('You spot a poorly hidden pit.')
            print('it\'s filled with deadly spikes')
            print('(who keeps on making these things???)')
            print('The door behind you closed.')
            print('Looks like you\'re going to have to jump it.')
            cont()

            rolling('Strength Save')
            str_save = skill_save(user.mods['str mod'], 10 + int(difficulty / 2))

            if str_save == True:
                print('You just barely manage to jump over the gap.')
                cont()
                return damage
        else:
            print('You fall into a spike trap!')
            rolling('Dexterity Save')
            dex_save = skill_save(user.mods['dex mod'], 10 + int(difficulty / 2))
            if dex_save == True:
                print('You manage to flail your arms enough to keep balance')
                print(f'You took no damage.')
            elif dex_save == False:
                damage = d4(3)
                print('You fell right into the traps thorny embrace.')
                print(f'You took {damage} damage.')
        return damage




def dungeon_chest():
    rarity = randint(luck_mod() * 10, 100)
    if rarity <= 25:
        print('You find a chest')
        print('The chest is empty.')
        print(':(')

    elif rarity <= 75:
        item_rand = randint(1, 25)
        print('You found a common chest!')
        print('You open it')
        cont()
        rolling('for goodies')
        if item_rand <= 5:
            item = ['weapon', 'dagger']
        elif item_rand <= 10:
            item = ['basic', 'health potion', 5]
        elif item_rand <= 15:
            item = ['basic', 'silver pieces', 40]
        elif item_rand <= 20:
            item = ['weapon', 'trident']
        elif item_rand <= 24:
            item = ['weapon', 'warhammer']
        elif item_rand == 25:
            item = ['weapon', 'greataxe']

    elif rarity <= 99:
        item_rand = randint(1, 10)
        print('You found a rare chest.')
        cont()
        rolling('for goodies')
        if item_rand <= 5:
            item = ['basic', 'health potion', 10]
        elif item_rand <= 7:
            item = ['basic', 'silver pieces', 75]
        if item_rand == 8:
            item = ['basic', 'gold pieces', randint(1, 2)]
        if item_rand == 9:
            item = ['weapon', 'greataxe']
        if item_rand == 10:
            item = ['weapon', 'maul']

    elif rarity == 100:
        item_rand = randint(1, 6)
        print('JACKPOT!!!!')
        print('You found a Legendary chest.')
        cont()
        rolling('for goodies')
        if item_rand <= 2:
            item = ['weapon', 'golden spirit']
        elif item_rand <= 4:
            item = ['weapon', 'player sif\'s dagger']
        elif item_rand == 5:
            item = ['weapon', 'dangolf staff']
        elif item_rand == 6:
            item = ['weapon', 'gun']

    try:
        if item[0] == 'basic':
            print(f'You obtained {item[2]} {item[1]}')
            user.equipment[item[1]] += item[2]
        elif item[0] == 'weapon':
            user.pickupweapon(item[1])
    except UnboundLocalError:
        return




def dungeon_exit():
    global dun_level

    print('You found a starecase leading down!')
    while True:
        print('do you want to go down?')
        print('''
        1.) Yes
        2.) No''')
        go_down = int_input('')
        if go_down == 1:
            dun_level += 1
            return True
        elif go_down == 2:
            return False
        else:
            invalid()

def dungeon_effects(dungeon):


    for row in dungeon:
        for column in row:
            if column[2] == True:
                if column[0] == 'encounter':
                    if column[3]:
                        player_is_alive = dungeon_encounters(column)
                        if player_is_alive == False:
                            return
                        print(user.current_exp, user.needed_exp)
                        print(user.current_exp >= user.needed_exp)
                        if user.current_exp >= user.needed_exp:
                            user.level_up()
                        column[3] = False
                    else:
                        print('You\'ve been here before.')

                elif column[0] == 'chest':
                    if column[3]:
                        dungeon_chest()
                        column[3] = False
                        return
                    else:
                        print('You\'ve been here before.')

                elif column[0] == 'trap':
                    if column[3]:
                        user.current_health -= dungeon_trap(column[1])
                        if user.current_health <= 0:
                            player_is_alive = False
                            return
                        column[3] = False
                    print(user.current_health, user.health)

                elif column[0] == 'exit':
                    column[3] = False
                    exit_choice = dungeon_exit()
                    if exit_choice == True:
                        return True

                elif column[0] == 'empty':
                    print('The room is empty.')
                    column[3] = False

                elif column[0] == 'entrance':
                    print('You are at the entrance')




def player_move_left(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        if row.index(column) - 1 == -1:
                            raise IndexError
                        row[row.index(column) - 1][2] = True
                        column[2] = False
                    except IndexError:
                        invalid()
                        return dungeon
                    print('You move to the left.')
                    return dungeon

def player_move_right(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        row[row.index(column) + 1][2] = True
                        column[2] = False
                    except IndexError:
                        invalid()
                        return dungeon
                    print('You move to the right.')
                    return dungeon

def player_move_up(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        if dungeon.index(dungeon[dungeon.index(row)]) - 1 == -1:
                            raise IndexError
                        dungeon[dungeon.index(row) - 1][row.index(column)][2] = True
                        column[2] = False
                    except IndexError:
                        invalid()
                        return dungeon
                    print('You move up.')
                    return dungeon

def player_move_down(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        dungeon[dungeon.index(row) + 1][row.index(column)][2] = True
                        column[2] = False
                    except IndexError:
                        invalid()
                        return dungeon
                    print('You move down.')
                    return dungeon

def movement_menu(dungeon):

    while True:
        print('Please pick a direction:')
        print('''    1.) Up
    2.) Down
    3.) Left
    4.) Right
    5.) Menu
    6.) Rest''')
        direction = int_input()
        if direction == 6:
            user.rest(False)
            return dungeon

        elif direction == 5:
            user.rest(True)
            return dungeon

        elif direction == 1:
            return player_move_up(dungeon)

        elif direction == 2:
            return player_move_down(dungeon)

        elif direction == 3:
            return player_move_left(dungeon)

        elif direction == 4:
            return player_move_right(dungeon)

        else:
            invalid()




# Getting this out of the way from the start:
# This is a demo for a project I've been working on for 2, almost 3, months
# Most of this code is copied from the main thing and was probably written a month ago
# Though a bunch of the important stuff is quite recent

# For example these are some recent things:
# Everything to do with spells
# Map navigation & generation
# The entire gameplay loop
# The Class "player"
# A lot

# You might notice that there are multiple files
# This was a decision I made and I regret it at all times
# It might've been a little worth it solely for the learning experience
# Programming :D


name = input(Fore.GREEN +'\nWhat is your name?\n' + Fore.RESET)
name_title = name.title()

print()
print(Fore.GREEN + 'Welcome ' + name_title + '! To my RPG demo!')
print('I\'d say it\'s pretty good (I am very biased)' + Fore.RESET)
print()

cont()

print('To start we\'re going to assign your stats (this is permenent)')

user.define_stats()

print('Total Health: ', user.health)
print('Current Health: ', user.current_health)
cont()






dungeon = make_dungeon()
print(f'you are here > {Fore.GREEN}+{Fore.RESET}')




user.equipment['equipped weapon'] = 'handaxe'

fight(slime, slime, slime, slime)

while user.isalive:

    print_dungeon(dungeon)
    dungeon = movement_menu(dungeon)
    print()
    effects = dungeon_effects(dungeon)
    cont()

    if user.current_exp >= user.needed_exp:
        user.level_up()

    if effects == True:
        dungeon = make_dungeon()
        rested = False

user.count_coints()

score = dun_level * 1000 + round(user.equipment['copper pieces'] * 0.1) + user.equipment['silver pieces'] * 10 + user.equipment['gold pieces'] * 1000

print(f'''Score:
Dungeon Floors ({dun_level}): {dun_level * 1000}
Coins (c:{user.equipment['copper pieces']}, s:{user.equipment['silver pieces']}, g: {user.equipment['gold pieces']}): {user.equipment['copper pieces'] + user.equipment['silver pieces'] * 100 + user.equipment['gold pieces'] * 1000}
Level({user.level}): {user.level * 100}
difficulty({difficulty}): {difficulty * 1000}

Total: {score}''')


print()