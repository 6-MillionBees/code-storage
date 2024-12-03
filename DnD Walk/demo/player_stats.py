# Arden Boettcher
# 12/2/24
# Player Stats


from default_functions import *
from dice import *

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
    1. Strength {strength}
    2. Dexterity {dexterity}
    3. Endurance {endurance}
    4. Inteligence {inteligence}
    5. Wisdom {wisdom}
    6. Charisma {charisma}\n1-6\n'''))
        except ValueError:
            invalid()
        else:
            sure = confirm()
            if sure == True:
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
    stats_choice_num += 1

player_mods = {
    'str mod': int((player_stats['str'] - 10) / 2),
    'dex mod': int((player_stats['str'] - 10) / 2),
    'end mod': int((player_stats['str'] - 10) / 2),
    'int mod': int((player_stats['str'] - 10) / 2),
    'wis mod': int((player_stats['str'] - 10) / 2),
    'cha mod': int((player_stats['str'] - 10) / 2),
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
player_health = starting_hit_dice[character_class] + player_mods['end mod']
current_player_health = player_health
print('Total Health: ', player_health)
print('Current Health: ', current_player_health)