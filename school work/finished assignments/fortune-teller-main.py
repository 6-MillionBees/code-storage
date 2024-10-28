# Arden Boettcher
# 10/24/24
# Fortune Teller

import random
import sys
import time
import colorama

fortunes = [
    'You are a winner!', 'A secret admirer will soon send you a sign of affection!', 'The one you love is much closer than you think.', 'It\'s coming from inside the house!', 'Good things will happen to you by the end of the day today!', 'Fame and fortune will be yours if you take the time to learn python!', 'That I hate this job. I quit', 'The spirits hate you personally.'
]

fortunes_len = len(fortunes) - 1
magic_colors = ['blue', 'red', 'green', 'yellow']

user_name = input('Please enter your name first name:\n')

print('Welcome to the Amazing Digital Fortune Teller ' + user_name.title() + '!')

question = input('Do you want a fortune? [y/n]\n')

if question.lower() in ['y', 'yes']:
    time.sleep(1)
    print('To get your fortune, please enter a magic color:')
    color = input('[Blue/Red/Green/Yellow]\n')

    while True:
        if color.lower() in magic_colors:
            print('Now... place your hand on the orb')
            time.sleep(2)
            print(f'''{colorama.Fore.BLUE}
                        ..:::..
                  .-++++=======++++-
                =++=================++-
              =+========--------======++-
            -+=====----------------=====+*.
           =+===----------------------====+-
          =+===-------------------:::---===+-
         -+===-------------------::::::--==+*.
        .++===--------------------::::::-===++
        :++===---------------------::::::==+*{colorama.Fore.LIGHTYELLOW_EX}#.
        =#{colorama.Fore.BLUE}*+===--------------------::::--==*{colorama.Fore.LIGHTYELLOW_EX}%%:
        -@%{colorama.Fore.BLUE}*+===-----------:::::--------==+{colorama.Fore.LIGHTYELLOW_EX}%%%:
        :%@@#{colorama.Fore.BLUE}+==-----------:::--:------==+*{colorama.Fore.LIGHTYELLOW_EX}#@#
         *@@@@{colorama.Fore.BLUE}*+==-------::::::--------=+*{colorama.Fore.LIGHTYELLOW_EX}#@%=
         :%@@@@%{colorama.Fore.BLUE}+=----:::::::::::---==+*{colorama.Fore.LIGHTYELLOW_EX}#%@@#
          -%@@@@@%{colorama.Fore.BLUE}*=---:::::::::--==+*{colorama.Fore.LIGHTYELLOW_EX}#%@@@#.
           -%@@@@@@@@@%#{colorama.Fore.BLUE}+=----==+*{colorama.Fore.LIGHTYELLOW_EX}#%@@@@@@*.
            .#@@@@@@@@@@@@@@@@@@@@@@@@@@%=
              :%@@@@@@@@@@@@@@@@@@@@@@%*
                :%@@@@@@@@@@@@@@@@@@%*
                =@@@@@@@@@@@@@@@@@@#*:
                =@@@@@@@@@@@@@@@@@@@@-
              .:+@@@@@@@@@@@@@@@@@@@%-.
              *#@@@@@@@@@@@@@@@@@@@@@+*+.
              #@@@*-=@@@@@@@@@@@@@@=-@@#.
              -@@@@@@@@@@@@@@@@@@@@@@@%.
              *%%%   :--=++++=@@@@@@-
                              .@@@@@{colorama.Fore.RESET}''')
            time.sleep(4)
            if color.lower() == 'blue':
                fortune_rand = random.randint(0, fortunes_len)
            elif color.lower() == 'red':
                fortune_rand = random.randint(1, fortunes_len)
            elif color.lower() == 'green':
                fortune_rand = 7 + random.randint(-1, 1)
            elif color.lower() == 'yellow':
                fortune_rand = 3 + random.randint(-3, 3)
            break
        else:
            print('Please enter a valid magic color.')
            color = input('[Blue/Red/Green/Yellow]\n')
    print('\n\nThe spirits are telling me...\n')
    time.sleep(1)
    if fortune_rand == 0:
        print('Congratulations!')
    elif fortune_rand == 3:
        print('We\'ve traced the call.')
    elif fortune_rand == 7:
        print('Oh no...')
        time.sleep(1)
    print()
    print(fortunes[fortune_rand])
    if fortune_rand == 6:
        time.sleep(1)
        sys.exit('Dispite having no legs the robot manages to leave')

elif question.lower() in ['n', 'no']:
    print('Suit yourself.')
    time.sleep(1)
    print('Goodbye.')