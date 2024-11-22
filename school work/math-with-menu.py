from math import pi
from time import sleep
from colorama import Fore



def numbered_input(words):
    while True:
        try:
            choice = int(input(f'{words}:\n'))
        except ValueError:
            print(Fore.RED + 'Invalid Input: please try again' + Fore.RESET)
            continue
        else:
            break
    return choice


def calc_circle_area(radius):
    area = pi * (radius ** 2)
    return area

def calc_power_base(base, exponent):
    result = base ** exponent
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


def main():
    while True:
        display_menu()

        try: # I'm not using the function I defined at the top for obvious reasons
            choice = int(input('Choose an option:\n'))
            if choice not in range(1, 5):
                raise ValueError

        except ValueError:
            display_menu()
            print(Fore.RED + 'Invalid Input: please try again' + Fore.RESET)
            continue


        if choice == 1: # I could have the whole calculating thing in one line but this looks nicer
            radius = numbered_input('Enter the circle\'s radius')
            result = calc_circle_area(radius)
            print(f'The area of the circle is: {result} units².')

        elif choice == 2:
            base = numbered_input('What is the base?')
            exponent = numbered_input('What is the exponent?')
            result = calc_power_base(base, exponent)
            print(f'The result is: {result}.')

        elif choice == 3:
            base = numbered_input('What is the base?')
            height = numbered_input('What is the height?')
            result = calc_triangle_area(base, height)
            print(f'The area of the triangle is: {result} units².')

        elif choice == 4:
            for num in range(1, 4): # Love a good *dot dot dot* as a loading bar (and it's really simple)
                print(f'\rExiting{"." * num}', end = '')
                sleep(0.5)
            
            print('\n') # Everyone online allways calls me bees as my username is a mouthfull so it's kindof my ailias
            print(Fore.YELLOW + 'Thank you for using Bee\'s Calculator' + Fore.RESET)
            return

main()