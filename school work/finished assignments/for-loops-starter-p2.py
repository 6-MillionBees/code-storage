# Arden Boettcher
# 11/6/ 24
# For Loops Part 2

import time
import string


# Counting Up and Down

while True:
    try:
        user_number = int(input('Please enter a number:\n'))
    except ValueError:
        print('Invalid Input: please try again')
    else:
        break

for x in range(user_number, -1, -1):

    print(f'\r{x}           ', end = '')
    time.sleep(0.5)
print
print('We have lift off!')


# Number Cubes

for number in range(1, 11):
    print(f'The cube of {number} is {number * number * number}')

print()

# Multiplication Table

number = 7

for num in range(1, 11):
    print(f'{num} times {number} equals {num * number}')


# The Cooler Multiplication Table

print()

print('Welcome to the cooler Multiplication Table')
print('*NOW WITH ADJUSTABLE LENGTH / WIDTH*\n')


while True:
    try:
        length = int(input('Please enter the length:\n'))
        width = int(input('Please enter the width:\n'))
    except ValueError:
        print('Invalid Input: please try again.')
        continue
    else:
        break

print()

table_dict = {}
loop = 1

for num_length in range(1, length + 1):
    for num_width in range(1, width + 1):
        table_dict[loop] = num_length * num_width
        loop += 1


for loops in table_dict:
    if loops % width == 0:
        print(table_dict[loops], end= ',\n')
        continue
    print(table_dict[loops], end= ', ')


# List Iteration

total = 0
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num_elements = len(numbers)

# You could skip out on using the len() and the range() functions and just put the list directly in the for loop
# Lists are called an iterable for a reason
# Like so:

# for i in numbers:
#     total += i


for i in range(num_elements):
    total += numbers[i]

print()

print(total)
print(sum(numbers))