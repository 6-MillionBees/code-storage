# Arden Boettcher
# 9/19/24
# "Simple" Recursive Sequence Finder

# import pygame
# pygame.init()

# screen = pygame.display.set_mode([600, 500])

valid_operations = ('+', '-', '*', '/', '^')
valid_decisions = ('#', '<', '>')

while True:
    try:
        start_number = int(input('Enter the starting number: '))
        operation = input("Enter operation. Input '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division, and '^' for exponents: ")
        if operation not in valid_operations:
            raise ValueError
        var = float(input('Enter the second number: '))
        decision = input("'#' for number of times, '<' for until it\'s less than a number, and '>' for until it\'s greater than a number: ")
        if decision not in valid_decisions:
            raise ValueError
    except ValueError:
        print('Invalid Input: Please try again')
        continue
    else:
        break

it_took = 0
base = 0



if decision == '#': # this is an increadibly brute force & stupid way to solve the problem.
    num_of_times = int(input('How many times?: ')) # This program is so stupid even a gpu could run it.
    print(start_number)
    if operation == '+':
        while base != num_of_times: 
            start_number += var
            print(start_number)
            base += 1
    elif operation == '-':
        while base != num_of_times:
            start_number -= var
            print(start_number)
            base += 1
    elif operation == '*':
        while base != num_of_times:
            start_number *= var
            print(start_number)
            base += 1
    elif operation == '/':
        while base != num_of_times:
            start_number /= var
            print(start_number)
            base += 1
    elif operation == '^':
        while base != num_of_times:
            start_number **= var
            print(start_number)
            base += 1


elif decision == '<':
    less_than = float(input('Put goal number: '))
    print(start_number)
    if operation == '+':
        while start_number > less_than:
            start_number += var
            print(start_number)
            base += 1
            it_took += 1
    elif operation == '-':
        while start_number > less_than:
            start_number -= var
            print(start_number)
            base += 1
            it_took += 1
    elif operation == '*':
        while start_number > less_than:
            start_number *= var
            print(start_number)
            base += 1
            it_took += 1
    elif operation == '/':
        while start_number > less_than:
            start_number /= var
            print(start_number)
            base += 1
            it_took += 1
    elif operation == '^':
        while start_number > less_than:
            start_number **= var
            print(start_number)
            base += 1
            it_took += 1
    print(f'it took {it_took} times to reach the goal')


elif decision == '>':
    greater_than = float(input('Put goal number: '))
    print(start_number)
    if operation == '+':
        while start_number < greater_than:
            start_number += var
            print(start_number)
            base += 1
            it_took += 1
    elif operation == '-':
        while start_number < greater_than:
            start_number -= var
            print(start_number)
            base += 1
            it_took += 1
    elif operation == '*':
        while start_number < greater_than:
            start_number *= var
            print(start_number)
            base += 1
            it_took += 1
    elif operation == '/':
        while start_number < greater_than:
            start_number /= var
            print(start_number)
            base += 1
            it_took += 1
    elif operation == '^':
        while start_number < greater_than:
            start_number **= var
            print(start_number)
            base += 1
            it_took += 1
    print(f'it took {it_took} times to reach the goal')