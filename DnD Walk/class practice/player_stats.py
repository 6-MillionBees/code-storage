# Arden Boettcher
# 12/2/24
# Player Stats


from default_functions import *
from dice import *




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


rested = False


class player:

    def __init__(self, level):
        player.isalive             = True
        player.level               = level
        player.rested              = False
        player.stats               = {'str': 0, 'dex': 0, 'end': 0, 'int': 0, 'wis': 0, 'cha': 0}
        player.sdamage_increase    = 0
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
        from items import weapon_name
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
        from items import weapon_name, weapon_print_damage
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
        from items import weapon_name, weapon_print_damage
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
        from items import weapon_name, weapon_print_damage
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
                        if current_player_health == self.health:
                            print('You already have full health.')
                            current_player_health = self.health
                            break

                        health_potion = d4(2)
                        current_player_health += health_potion
                        if current_player_health >= self.health:
                            current_player_health = self.health
                        print(f'You gained {health_potion} health.')
                        bar(current_player_health, self.health, 15)
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

        from spells import spell_descriptions # IMPORT

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







# So I don't actually have enough time to add multiple classes sooooooo
# Work in progress