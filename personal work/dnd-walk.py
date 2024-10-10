# Arden Boettcher
# Start: 10/9/24
# A short hike in DND

import random
import colorama as col

def cont():
    return input('Press enter to continue.\n')
def d100():
    roll = random.randint(1, 100)
    return roll
def d20():
    roll = random.randint(1, 20)
    return roll
def d12():
    roll = random.randint(1, 12)
    return roll
def d10():
    roll = random.randint(1, 10)
    return roll
def d8():
    roll = random.randint(1, 8)
    return roll
def d6():
    roll = random.randint(1, 6)
    return roll
def d4():
    roll = random.randint(1, 4)
    return roll



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

name = input(col.Fore.LIGHTWHITE_EX +'\nwhat is your name?\n' + col.Fore.RESET)

while all_stats == False:
    if is_str and is_dex and is_end and is_int and is_wis and is_cha:
        all_stats = True
        continue
    roll1 = d6()
    roll2 = d6()
    roll3 = d6()
    roll4 = d6()
    stat_list = [roll1, roll2, roll3, roll4,]
    stat_roll = roll1 + roll2 + roll3 + roll4 - min(stat_list)
    print(f'You rolled a {stat_roll}!')
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
            strength = stat_roll
            is_str = True
            print(f'Your Strength is now {strength}.')
            cont()
            break

        elif choice == 2 and is_dex == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 2 and is_dex == False:
            dexterity = stat_roll
            is_dex = True
            print(f'Your Dexterity is now {dexterity}.')
            cont()
            break

        elif choice == 3 and is_end == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 3 and is_end == False:
            endurance = stat_roll
            is_end = True
            print(f'Your Endurance is now {endurance}')
            cont()
            break

        elif choice == 4 and is_int == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 4 and is_int == False:
            inteligence = stat_roll
            is_int = True
            print(f'Your Inteligence is now {inteligence}')
            cont()
            break

        elif choice == 5 and is_wis == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 5 and is_wis == False:
            wisdom = stat_roll
            is_wis = True
            print(f'Your Wisdom is now {wisdom}')
            cont()
            break

        elif choice == 6 and is_cha == True:
            print('Stat already chosen please choose another.\n')
            cont()
            break
        elif choice == 6 and is_cha == False:
            charisma = stat_roll
            is_cha = True
            print(f'Your  is now {stat_roll}')
            cont()
            break



distance = input(col.Fore.LIGHTWHITE_EX + '\nhow long do you want to hike?\n' + col.Fore.RESET)
distance_traveled = 0
days = 0
karma = 0

while distance > distance_traveled:
    if d20() >= 10:
        is_encounter = True
    else:
        is_encounter = False
    if d20() >= 10:
        is_chance = True
    else:
        is_chance = False

    if is_chance == True and is_encounter == True:

    elif is_encounter == True:
        roll_encounter = d100()
    elif is_chance == True:
        roll_chance = d100()
        if roll_chance == 1:
            print('''As you travel a bit off the beaten path you run into a party of adventurers, they look experienced.
one of them notices you and begins to talk;
"Oh hey! A person! You're not a bandit are you?''', end='')
            say = input('''What do you say?
    1. Yes I am, now give me all your money *fight*
    2. No I'm just a traveler
    3. You'll never know *you wink at them ;D*
    4. *Walk away slowly*''')
            if say == 1:
                if karma <= -10:
                    print('They didn\'t take a liking to your admition and begin to quickly prepare for battle.', end= '')
                elif karma >= 10:
                    print('They didn\'t like your attempt at humour and begin to quickly prepare for battle.', end= '')
                else:
                    print('They didn\'t appear to like that and begin to quickly prepare for battle.', end= '')
                print(' Before you can grasp the depth of your mistake the robed one with the funny hat hits you with a spell that blinds you with a flash of light')
                save = d20() + endurance_mod
