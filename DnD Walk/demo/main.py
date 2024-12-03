# Arden Boettcher
# 11/26/24
# DnD walk demo (for class)

from colorama import Fore
from colorama import Back
from time import sleep

from dice import *
from default_functions import *


# Getting this out of the way from the start:
# This is a demo for a project I've been working on for 2, almost 3, months
# Most of this code is copied from the main thing and was probably written a month ago
# Though a bunch of the important stuff is quite recent

# For example these are some recent things:
# Everything to do with spells
# Map navigation & generation
# 


days = 0
difficulty = 1 + days / 25


first_name = input(Fore.GREEN +'\nWhat is your first name?\n' + Fore.RESET)
last_name = input(Fore.GREEN + '\nWhat is your last name?:\n' + Fore.RESET)

full_name = first_name.title() + last_name.title()

print(Fore.GREEN + 'Welcome ' + full_name + '! To my DnD demo!')
print('I\'d say it\'s pretty good (I am very biased)' + Fore.RESET)

cont()

print('To start we\'re going to assign your stats (this is permenent)')

from player_stats import *
from fighting_functions import *