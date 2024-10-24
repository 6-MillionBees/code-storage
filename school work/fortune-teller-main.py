# Arden Boettcher
# 10/24/24
# Fortune Teller

import random
import sys
import time
import colorama

fortunes = [
    'You are a winner!', 'A secret admirer will soon send you a sign of affection!', 'The one you love is much closer than you think', 'The call is coming from inside the house!', 'Good things will happen to you by the end of the day today!', 'Fame and fortune will be yours if you take the time to learn python!', 'I\'m just a computer program, why are you asking me for advice?'
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

    if color.lower() in magic_colors:
        print('Now... place your hand on the orb')
        print(f'''                                                       
    {colorama.Fore.BLUE}                    ..:::..                        
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
                              .@@@@@                   {colorama.Fore.RESET}''')
        time.sleep(4)
        print('Feel the power of the orb.')
        time.sleep(4)
    else:
        print('womp womp')

elif question.lower() in ['n', 'no']:
    print('Suit yourself')