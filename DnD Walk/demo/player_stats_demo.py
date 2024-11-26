from colorama import Fore

from dice_demo import *
from starting_functions_demo import cont, invalid, confirm
from pygame import *



def define_class():
    while True:
        try:
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
        except ValueError:
            invalid()
        else:

            if class_choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                invalid()
                continue

            sure = confirm()

            if sure == 1:
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
                continue
    print(f'You now are a {character_class.title()}')
    return character_class


def define_stats():
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


    while all_stats == False:

        if is_str_chosen and is_dex_chosen and is_end_chosen and is_int_chosen and is_wis_chosen and is_cha_chosen:
            all_stats = True
            continue

        stat_list = [d6(), d6(), d6(), d6()]
        stat_roll_main= sum(stat_list) - min(stat_list)
        print(f'You rolled a {stat_roll_main}!')

        while True:
            try:
                choice = int(input(f'''{Fore.GREEN}Which stat?{Fore.RESET}
        1. Strength {strength}
        2. Dexterity {dexterity}
        3. Endurance {endurance}
        4. Inteligence {inteligence}
        5. Wisdom {wisdom}
        6. Charisma {charisma}\n1-6\n'''))
            except ValueError:
                invalid()
            else:
                break

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
                player_stats['cha'] = stat_roll_main
                is_cha_chosen = True
                print(f'Your charisma is now {charisma}')
                cont()
                break

            else:
                print('Please pick a number between 1 and 6.')
                continue


player_stats = {
    'str': 0,
    'dex': 0,
    'end': 0,
    'int': 0,
    'wis': 0,
    'cha': 0
}

player_mods = {
    'str mod': int((player_stats['str'] - 10) / 2),
    'dex mod': int((player_stats['str'] - 10) / 2),
    'end mod': int((player_stats['str'] - 10) / 2),
    'int mod': int((player_stats['str'] - 10) / 2),
    'wis mod': int((player_stats['str'] - 10) / 2),
    'cha mod': int((player_stats['str'] - 10) / 2),
    'casting mod': 0
}

class_casting_mods = {
    'barbarian': 0,
    'bard':      player_mods['cha mod'],
    'cleric':    player_mods['wis mod'],
    'fighter':   2, # WIP
    'monk':      0,
    'paladin':   player_mods['cha mod'],
    'rogue':     0,
    'sorcerer':  player_mods['end mod'],
    'warlock':   player_mods['cha mod'],
    'wizard':    player_mods['int mod']
}


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
player_mods['casting mod'] = class_casting_mods[character_class]

level = 3
player_health = starting_hit_dice[character_class] + player_mods['end mod']
current_player_health = player_health
print('Total Health: ', player_health)
print('Current Health: ', current_player_health)