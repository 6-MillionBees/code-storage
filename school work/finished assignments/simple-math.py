# Arden Boettcher
# 9/23/24
# Basic Math part 1

import time
from colorama import Fore

# Practice 1:

num1 = 7
num2 = 2

product = num1 ** num2

print(f'{num1} to the power of {num2} = {product}\n')


# Practice 2:

length = float(input('Please write the length of the square in feet: '))
width = float(input('Please write the length of the square in feet: '))

square_feet = length * width

print(f'\nThe area of the {length} ft by {width} ft square is {square_feet} square feet.\n')


# Practice 3:

# Part 1
name = 'Arden Boettcher'
age = 16

print('My name is {0} and I am {1} years old'.format(name, age))

# Part 2
eggs = 3.00
milk = 2.64
bread = 3.16

total = (eggs + milk + bread) * 1.06

print('\nI want to buy eggs, milk, and bread, but I don\'t know how much it costs. *frowny face*\n')
time.sleep(3)
print(Fore.GREEN + 'I know who can help!\n' + Fore.RESET)
time.sleep(2)
print('WOAH! GROCERY MAN!!!\n')
time.sleep(2)
print(Fore.GREEN + 'That\'s right! It\'s me! GROCERY MAN!!!\n')
time.sleep(1.5)
print(f'And YOU good citizen, your total for eggs, milk, and bread comes out to be: ${total:.2f}.\n' + Fore.RESET)
time.sleep(1.5)
print('OH thank you Grocery Man, what would we ever do without you?\n')
time.sleep(1.5)
print(Fore.GREEN + 'Oh please, I\'m just doing my civic duty as a man with a calculator.\n\n*whoosh sound effect*\n' + Fore.RESET)

# Part 3

sentence = 'My friend\'s first name is {0} and we go to the same school; {school}.' # I'm displaying my understanding by using both techniques when it comes to the format method

print(sentence.format('Oliver', school = 'The Greenspire Highschool'))