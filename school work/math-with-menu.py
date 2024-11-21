import math
import time



def calc_circle_area(radius):
    area = math.pi * radius ^ 2
    return area

def calc_power_base(base, exponent):
    result = base ^ exponent
    return result

def calc_triangle_area(base, height):
    area = 0.5 * base * height
    return area

def display_menu():
    print('''Menu:

    1. Calculate area of a circle
    2. Raise a number to a power
    3. Calculate area of a right triangle
    4. Exit
''')

display_menu()

while True:
    try:
        choice = int(input('Choose an option:\n'))
        if choice not in range(1, 5):
            raise ValueError
    except ValueError:
        print('Invalid Input: please try again')
        continue
    else:
        break

if choice == 1:
    radius = int(input('Enter the radius: '))
    result = 