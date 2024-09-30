# Arden Boettcher
# 9/24/24
# Simple Math part 2

import time
import math

# Task 1:

item = input('Enter the cost of the discounted item: ')
float_item = float(item.replace('$', '')) # This removes the dollar sign if the user puts one in

product = float_item * 0.8

print(f'The cost of the discounted item is: ${product:.2f}\n')

# Task 2:

length = int(input('How long is the garden? '))
width = int(input('How wide is the garden? '))

print(f'The area of the garden is {length * width}\n')

# Task 3:

bacteria = 10
hours = 0

while hours <= 5:
    print(f'Hour {hours}: {bacteria}')
    bacteria *=2
    hours += 1

'''
while hours <= 5: # This one makes you wait a whole hour between loops! (For immersion)
    print(f'Hour {hours}: {bacteria}')
    bacteria *=2
    hours += 1
    time.sleep(3600)
'''

# Task 4:

distance = int(input('\nHow far away is your destination? (in kilometers): '))
velocity = int(input('How fast are you going? (in kilometers per hour): '))

time_took = distance / velocity

print(f'\nIt will take {time_took:.2f} hours.\n')

# Task 5:

# The instructions say "A group of 23 people want to share *A* pizza evenly" which does not work because 23 <= 8 == False.
print('You can\'t evenly split a single eight piece pizza between 23 people... but with multiple pizzas:\n')

# So I made it work under the assumption that there are multiple pizzas

people = int(input('How many people?: '))
pizza_slice = int(input('How many slices per pizza?: '))

pizzas = str(people / pizza_slice) 
pizza_rounded = math.ceil(people / pizza_slice) # Big fan of making things overly complicated
extra_pizza = 0

if float(pizzas).is_integer() == False: # There was a problem with pizzas being a whole number, this fixes it.
    pizza_float = float(pizzas[pizzas.find('.'):])
    extra_pizza = math.ceil(pizza_slice * (1 - pizza_float)) # This whole section has 7 different variables, 5 of them start with pizza.

print(f'\nYou would need {pizza_rounded} pizza(s) and you would have {int(extra_pizza)} slice(s) left over.\n')

# THERE WAS THE MODULUS OPERATOR THIS WHOLE TIME. I'm gonna cry myself to sleep tonight.
# Now with the modulus operator! :D
'''
people = int(input('How many people?: '))
pizza_slice = int(input('How many slices per pizza?: '))

pizza_rounded = math.ceil(people / pizza_slice)
extra_pizza = people % pizza_slice 

print(f'\nYou would need {pizza_rounded} pizza(s) and you would have {int(extra_pizza)} slice(s) left over.\n')

# WOW line 78 makes 5 OTHER LINES completely redundant, along with 2 hours of my life.
'''