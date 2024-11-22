from colorama import Fore

from starting_functions import invalid

while True:
    try:
        distance = int(input(Fore.GREEN + '\nhow long do you want to hike?\n' + Fore.RESET))
    except ValueError:
        invalid()
    else:
        break

distance_traveled = 0
karma = 2.891

luck_bonus = 0
luck_multiplier = 1
luck_mod = 0


# def luck_calc():
#     luck = round(karma/2 + luck + luck_bonus)
#     luck_mod = int((luck - 10) / 2)
#     return round(luck, 2), luck_mod

luck = lambda: karma * 1.5 + 10 + luck_bonus
luck_mod = lambda: int((luck() - 10) / 2)