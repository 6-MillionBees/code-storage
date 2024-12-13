# Arden Boettcher
# 12/2/24
# Player Stats


from default_functions import *
from dice import *

is_str_chosen = False
is_dex_chosen = False
is_end_chosen = False
is_int_chosen = False
is_wis_chosen = False
is_cha_chosen = False
all_stats = False

player_stats = {
    'str': 0,
    'dex': 0,
    'end': 0,
    'int': 0,
    'wis': 0,
    'cha': 0
}

stats_choice_num = 0

while stats_choice_num < 6:

    stat_list = [d6(), d6(), d6(), d6()]
    stat_roll_main= sum(stat_list) - min(stat_list)

    while True:
        try:
            print(f'You rolled a {Fore.GREEN}{stat_roll_main}{Fore.RESET}!')

            choice = int(input(f'''{Fore.GREEN}Which stat?{Fore.RESET}
    1. Strength {player_stats["str"]}
    2. Dexterity {player_stats["dex"]}
    3. Endurance {player_stats["end"]}
    4. Inteligence {player_stats["int"]}
    5. Wisdom {player_stats["wis"]}
    6. Charisma {player_stats["cha"]}
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
            player_stats['str'] = stat_roll_main
            is_str_chosen = True
            print(f'Your Strength is now {player_stats["str"]}.')
            cont()
            break

        elif choice == 2 and is_dex_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            continue
        elif choice == 2 and is_dex_chosen == False:
            player_stats["dex"] = stat_roll_main
            is_dex_chosen = True
            print(f'Your Dexterity is now {player_stats["dex"]}.')
            cont()
            break

        elif choice == 3 and is_end_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            continue
        elif choice == 3 and is_end_chosen == False:
            player_stats["end"] = stat_roll_main
            is_end_chosen = True
            print(f'Your Endurance is now {player_stats["end"]}')
            cont()
            break

        elif choice == 4 and is_int_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            continue
        elif choice == 4 and is_int_chosen == False:
            player_stats["int"] = stat_roll_main
            is_int_chosen = True
            print(f'Your Inteligence is now {player_stats["int"]}')
            cont()
            break

        elif choice == 5 and is_wis_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            continue
        elif choice == 5 and is_wis_chosen == False:
            player_stats["wis"] = stat_roll_main
            is_wis_chosen = True
            print(f'Your Wisdom is now {player_stats["wis"]}')
            cont()
            break

        elif choice == 6 and is_cha_chosen == True:
            print(f'{Fore.RED}Stat already chosen please choose another.\n{Fore.RESET}')
            cont()
            continue
        elif choice == 6 and is_cha_chosen == False:
            player_stats['cha'] = stat_roll_main
            is_cha_chosen = True
            print(f'Your charisma is now {player_stats["cha"]}')
            cont()
            break

        else:
            print('Please pick a number between 1 and 6.')
            continue
    stats_choice_num += 1

player_mods = {
    'str mod': int((player_stats['str'] - 10) / 2),
    'dex mod': int((player_stats['dex'] - 10) / 2),
    'end mod': int((player_stats['end'] - 10) / 2),
    'int mod': int((player_stats['int'] - 10) / 2),
    'wis mod': int((player_stats['wis'] - 10) / 2),
    'cha mod': int((player_stats['cha'] - 10) / 2),
}


# So I don't actually have enough time to add multiple classes sooooooo
# Work in progress

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

character_class = 'fighter'

player_ac = 10 + player_mods['dex mod']
initiative_bonus = player_mods['dex mod']


level = 3
player_exp = 0
exp_needed = 100

player_health = starting_hit_dice[character_class] + player_mods['end mod']
for x in range(level):
    player_health += hit_dice[character_class]()
current_player_health = player_health

def skill_save(save_mod, dc):
    save = d20() + save_mod
    print(f'You rolled a {save}')
    if save >= dc:
        print('Success!')
        return True
    elif save < dc:
        print('Failure.')
        return False


from spells import spell_damage_increase

def level_up():

    global level
    global player_exp
    global exp_needed
    global player_stats
    global player_health
    global current_player_health
    global spell_damage_increase
    
    level += 1
    player_exp -= exp_needed
    exp_needed *= 1.5
    exp_needed = int(exp_needed)

    print(Fore.GREEN + 'You Leveled Up!')
    print(f'You are now level {level}' + Fore.RESET)
    print(f'{exp_needed} exp until next level up.')

    player_health += hit_dice[character_class]()
    current_player_health = player_health


    print(f'You now have {player_health} health')

    if level % 3 == 0:
        spell_damage_increase += 1

    if level % 5 == 0:
        while True:
            print('Please pick one stat to increase:')
            num = 0
            for stat in player_stats.keys():
                num += 1
                print(f'    {num}.) {stat} ({player_stats[stat]})')
            stat_pick = int_input()
            if stat_pick not in range(1, num + 1):
                invalid()
                continue

            if stat_pick == 1:
                player_stats['str'] += 1
                break
            elif stat_pick == 2:
                player_stats['dex'] += 1
                break
            elif stat_pick == 3:
                player_stats['end'] += 1
                break
            elif stat_pick == 4:
                player_stats['int'] += 1
                break
            elif stat_pick == 5:
                player_stats['wis'] += 1
                break
            elif stat_pick == 6:
                player_stats['cha'] += 1
                break

    if level % 6 == 0:
        max_player_spell_slots[1] += 1
    if level % 7 == 0:
        max_player_spell_slots[2] += 1





def rest_items_menu():
    from items import weapon_name, weapon_print_damage, player_equipment, drop_weapon, equip_weapon

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
            print(f'''
weapons:
Equipped: {weapon_name[player_equipment['equipped weapon']]} damage: {weapon_print_damage[player_equipment['equipped weapon']]}
Stored 1: {weapon_name[player_equipment['stored weapon 1']]} damage: {weapon_print_damage[player_equipment['stored weapon 1']]}
Stored 2: {weapon_name[player_equipment['stored weapon 2']]} damage: {weapon_print_damage[player_equipment['stored weapon 2']]}
Stored 3: {weapon_name[player_equipment['stored weapon 3']]} damage: {weapon_print_damage[player_equipment['stored weapon 3']]}
Stored 4: {weapon_name[player_equipment['stored weapon 4']]} damage: {weapon_print_damage[player_equipment['stored weapon 4']]}
Stored 5: {weapon_name[player_equipment['stored weapon 5']]} damage: {weapon_print_damage[player_equipment['stored weapon 5']]}

items:
Copper Pieces: {player_equipment['copper pieces']}
Silver Pieces: {player_equipment['silver pieces']}
Gold Pieces: {player_equipment['gold pieces']}
Health Potions: {player_equipment['health potion']}
''')
            cont()
            continue
        elif items_choice == 2:
            drop_weapon()
            continue
        elif items_choice == 3:
            print('Use Health Potion? (2d4)')
            if player_equipment['health potion'] == 0:
                print('You don\'t have any potions')
                continue
            while True:
                confirm = int_input('''    1.) Yes
    2.) No
''')
                if confirm == 1:
                    if current_player_health == player_health:
                        print('You already have full health.')
                        current_player_health = player_health
                        break

                    health_potion = d4(2)
                    current_player_health += health_potion
                    if current_player_health >= player_health:
                        current_player_health = player_health
                    print(f'You gained {health_potion} health.')
                    bar(current_player_health, player_health, 15)
                    player_equipment['health potion'] -= 1
                    break
                elif confirm == 2:
                    break
                else:
                    invalid()
                    continue
            
        elif items_choice == 4:
            equip_weapon()
        else:
            invalid()
            continue


def stats_menu():
    print('Stats:')
    print(f'''
Strength:       {player_stats["str"]} modifier: {player_mods["str mod"]}
Dexterity:      {player_stats["dex"]} modifier: {player_mods["dex mod"]}
Endurance:      {player_stats["end"]} modifier: {player_mods["end mod"]}
Inteligence:    {player_stats["int"]} modifier: {player_mods["int mod"]}
Wisdom:         {player_stats["wis"]} modifier: {player_mods["wis mod"]}
Charisma:       {player_stats["cha"]} modifier: {player_mods["cha mod"]}

Health {current_player_health}/{player_health}
{bar(current_player_health, player_health, 15)}''')
    cont()


from spells import *

def rest_spells_menu():
    print('Current/Max Spell Slots:')
    for spell_level in max_player_spell_slots.keys():
        print(f'level {spell_level}: {current_player_spell_slots[spell_level]}/{max_player_spell_slots[spell_level]}')
    while True:
        num = 0
        print('See spell descriptions (-1 to exit)')
        for spell_level in max_player_spell_slots.keys():
            num += 1
            print(f'    {spell_level}.) {", ".join(player_spells[spell_level])}')

        spell_level = int_input()

        if spell_level == -1:
            return
        elif spell_level not in range(num + 1):
            continue
 
        num1 = 0
        for spell in player_spells[spell_level]:
            num1 += 1
            print(f'''    {num1}.) {spell_descriptions[spell]}\n''')
        cont()


rested = False

def rest(rested):
    global current_player_health
    # from world import current_player_health, player_health
    global current_player_spell_slots

    if rested == True:
        print('Since you already rested on this floor you don\'t get any health back')
    else:
        print('You have been restored to full health')
        print('and your spell slots have been restored')
        current_player_health = player_health
        current_player_spell_slots = max_player_spell_slots

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
            rest_items_menu()
            continue
        elif rest_choice == 2:
            stats_menu()
        elif rest_choice == 3:
            rest_spells_menu()

def rest_without_the_rest():
    global player_health
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
            rest_items_menu()
            continue
        elif rest_choice == 2:
            stats_menu()
        elif rest_choice == 3:
            rest_spells_menu()
        elif rest_choice == 231645:
            player_health = -1