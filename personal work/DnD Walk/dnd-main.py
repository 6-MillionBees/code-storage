# Arden Boettcher
# Start: 10/9/24
# A Hike Through The Woods

import random
import colorama as col
import time

# Dice
def d100(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += random.randint(1, 100)
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
    91: False, 92: False, 93: False, 94: False, 95: False, 96: False, 97: False, 98: False, 99: False, 100: False
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
    91: False, 92: False, 93: False, 94: False, 95: False, 96: False, 97: False, 98: False, 99: False, 100: False
}

# Other functions
def cont():
    input('\nPress enter to continue.\n')
def roll(roll, difficulty, mod):
    if roll == 20:
        print('NATURAL 20!')
        return True
    elif roll == 1:
        print('Critical Fail.')
        return False
    elif (roll + mod - difficulty) < 0:
        print('Roll failed')
        return False
    else:
        return True




strength = 0
dexterity = 0
endurance = 0
inteligence = 0
wisdom = 0
charisma = 0
is_str = False
is_dex = False
is_end = False
is_int = False
is_wis = False
is_cha = False
true = True
all_stats = False

name = input(col.Fore.GREEN +'\nWhat is your name?\n' + col.Fore.RESET)

print('Please assign your stats')
cont()

while all_stats == False:
    if is_str and is_dex and is_end and is_int and is_wis and is_cha:
        all_stats = True
        continue
    stat_roll1 = d6()
    stat_roll2 = d6()
    stat_roll3 = d6()
    stat_roll4 = d6()
    stat_list = [stat_roll1, stat_roll2, stat_roll3, stat_roll4,]
    stat_roll_main= stat_roll1 + stat_roll2 + stat_roll3 + stat_roll4 - min(stat_list)
    print(f'You rolled a {stat_roll_main}!')
    choice = int(input(f'''Which stat?
    1. Strength {strength}
    2. Dexterity {dexterity}
    3. Endurance {endurance}
    4. Inteligence {inteligence}
    5. Wisdom {wisdom}
    6. Charisma {charisma}\n1-6\n'''))
    while true:
        if choice == 1 and is_str == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 1 and is_str == False:
            strength = stat_roll_main
            is_str = True
            print(f'Your Strength is now {strength}.')
            cont()
            break

        elif choice == 2 and is_dex == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 2 and is_dex == False:
            dexterity = stat_roll_main
            is_dex = True
            print(f'Your Dexterity is now {dexterity}.')
            cont()
            break

        elif choice == 3 and is_end == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 3 and is_end == False:
            endurance = stat_roll_main
            is_end = True
            print(f'Your Endurance is now {endurance}')
            cont()
            break

        elif choice == 4 and is_int == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 4 and is_int == False:
            inteligence = stat_roll_main
            is_int = True
            print(f'Your Inteligence is now {inteligence}')
            cont()
            break

        elif choice == 5 and is_wis == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 5 and is_wis == False:
            wisdom = stat_roll_main
            is_wis = True
            print(f'Your Wisdom is now {wisdom}')
            cont()
            break

        elif choice == 6 and is_cha == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 6 and is_cha == False:
            charisma = stat_roll_main
            is_cha = True
            print(f'Your charisma is now {charisma}')
            cont()
            break
        else:
            print('Please pick a number between 1 and 6.')

str_mod = int((strength - 10) / 2)
dex_mod = int((dexterity - 10) / 2)
end_mod = int((dexterity - 10) / 2)
int_mod = int((dexterity - 10) / 2)
wis_mod = int((dexterity - 10) / 2)
cha_mod = int((dexterity - 10) / 2)
proficientcy = 2

weapon_damage = {
    'club': d4(), 'dagger': d4(), 'great club': d10(), 'javelin': d6(), 'light hammer': d4(),
    'mace': d6(), 'quarterstaff': d8(), 'sickle': d4(), 'spear': d6(), 'battle axe': d8(),
    'flail': d8(), 'glaive': d10(), 'greataxe': d12(), 'greatsword': d6(2), 'halberd': d10(),
    'handaxe': d6(), 'lance': d8(), 'longsword': d8(), 'maul': d6(2), 'morningstar': d8(),
    'pike': d10(), 'rapier': d8(), 'scimitar': d6(), 'shortsword': d6(), 'trident': d8(),
    'war pick': d8(), 'warhammer': d8(), 'whip': d4()
}

weapon_mod = {
    'club mod': str_mod, 'dagger': dex_mod, 'great club': str_mod, 'javelin': str_mod, 'light hammer': str_mod,
    'mace': str_mod, 'quarterstaff': str_mod, 'sickle': str_mod, 'spear': str_mod, 'battle axe': str_mod,
    'flail': str_mod, 'glaive': str_mod, 'greataxe': str_mod, 'greatsword': str_mod, 'halberd': str_mod,
    'handaxe': str_mod, 'lance': str_mod, 'longsword': str_mod, 'maul': str_mod, 'morningstar': str_mod,
    'pike': str_mod, 'rapier': dex_mod, 'scimitar': dex_mod, 'shortsword': dex_mod, 'trident': str_mod,
    'war pick': str_mod, 'warhammer': str_mod, 'whip': dex_mod
}

def attack(modifier, weapon, ac):
    roll = d20() + modifier 
    if ac > roll:
        print('Your attack did not hit')
        return 0
    if ac <= roll:
        print('')
        return weapon_damage[weapon] + weapon_mod[weapon]

distance = input(col.Fore.GREEN + '\nhow long do you want to hike?\n' + col.Fore.RESET)
distance_traveled = 0
days = 0
karma = 0
luck_bonus = 0
luck = round(karma/2 + 10 + luck_bonus)
luck_mod = int((luck - 10) / 2)

while distance > distance_traveled:
    if d20() <= 10:
        is_encounter = True
    else:
        is_encounter = False
    if d20() >= 10:
        is_chance = True
    else:
        is_chance = False

    if is_chance == True and is_encounter == True:
        roll_enocounter = d100()
        roll_chance = d100()
    elif is_encounter == True:
        roll_encounter = d100()
    elif is_chance == True:
        roll_chance = d100()
        if roll_chance == 1 and chance[1] == False:
            print('''As you travel a bit off the beaten path you run into a party of adventurers, they look experienced.
one of them notices you and begins to talk;
"Oh hey! A person! You're not a bandit are you?''', end='')
            say = input('''What do you say?
    1. Yes I am, now give me all your money *fight*
    2. No I'm just a traveler
    3. You'll never know *you wink at them ;D*
    4. *Walk away slowly*''')
            if say == 1:
                if karma <= -5:
                    print('They didn\'t like your admition of guilt and begin to quickly prepare for battle.', end= '')
                elif karma >= 5:
                    print('They didn\'t like your attempt at humour and begin to quickly prepare for battle.', end= '')
                else:
                    print('They didn\'t appear to like that and begin to quickly prepare for battle.', end= '')
                print('But before you can grasp the depth of your mistake the robed one with the funny hat hits you with a spell that blinds you with a flash of light')
                save = d20() + dex_mod
                if save < 8:
                    print('After being blinded you feel a sharp pain as something hits you on the back of the head. You lose consciousness.')
                    time.sleep(1)
                    print('You slowly start to wake up and realise you are tied up, with your belongings hung from the branches of a very tall tree.')