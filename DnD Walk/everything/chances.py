from time import sleep
from random import randint

from dice import *
from starting_functions import *
from player_stats import *
from npc_stats import *
from world import *
from fighting_functions import *

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
    91: False, 92: False, 93: False, 94: False, 95: False
}



def chance1():
    chance[1] = True
    print('''As you travel a bit off the beaten path you run into a party of adventurers around a campfire, they look experienced.
One of them notices you and begins to talk;
"Oh hey! A person! You're not a bandit are you?"''')
    cont()
    while True:
        try:
            say = int(input('''What do you say?
    1. Yes I am. Now give me all your money *fight*
    2. No I'm just a traveler
    3. You'll never know *you wink at them ;D*
    4. *Walk away slowly*\n'''))
        except ValueError:
            invalid()
        else:
            break
    if say == 1:
        if karma <= -5:
            print('They didn\'t like your admition of guilt and begin to quickly prepare for battle.')
            cont()
        elif karma >= 5:
            print('They didn\'t like your attempt at humour and begin to quickly prepare for battle.')
            cont()
        else:
            print('They didn\'t appear to like that and begin to quickly prepare for battle.')
            cont()

        if level < 10:
            rolling('for a dex save')
            save = d20()
            print(f'You rolled a {save} for a total of  {save + player_mods["dex mod"]}')
            save += player_mods["dex mod"]
            cont()
            if save < 8:
                print('But before you can grasp the depth of your mistake one of them hits you with a spell that blinds you with a flash of light.')
                cont()
                print('After being blinded you feel a sharp pain as something hits you on the back of the head. You lose consciousness.')
                sleep(1)
                print('You slowly start to wake up and realise you are tied up, with your belongings hung from the branches of a very tall tree.')

                thing = round(current_player_health/8) + randint(-3, 3)
                if current_player_health < thing:
                    thing = current_player_health + 1
                if thing <= 0:
                    print(f'You feel sore but are otherwise fine.')
                else:
                    print(f'You are slightly hurt and lost {thing} heath.')
                cont()

            elif save > 18:
                print('You notice one of them begins to cast a spell, instinctively you cover your eyes')
                cont()
                print('You see a flash through your hands and are partially stunned')
                while True:
                    try:
                        choice = int(input('''What do you do?
        1. Stay and fight
        2. RUN AWAY\n'''))
                    except ValueError:
                        invalid()
                    else:
                        if choice == 1:
                            fight(2, kile, gronk)
                            break
                        elif choice == 2:
                            print('You manage to escape')
                            cont()
                            break
                        else:
                            invalid()
            elif save >= 8:
                print('')
        elif level >= 10:
            fight(2, kile, gronk)
    elif say == 2:
        print('work in progress')
    elif say == 3:
        print('work in progress')