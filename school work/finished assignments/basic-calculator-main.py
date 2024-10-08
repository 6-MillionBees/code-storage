# Eliot Clarke Arden Boettcher
# 10/8/24
# Basic Calculator

operation = input('''
Welcome to The Amazing Digital Calculator
    *By: Eliot & Arden*

Please enter your operation:
    1. Addition (+)
    2. Subtraction (-)
    4. Division (/)
enter a number (1-4): 
''')

num1 = int(input('\nplease enter your first number: '))
num2 = int(input('please enter your second number: '))
boolian = num1 == 0 or num2 == 0
print('')

if boolian and operation == '4':
    quit()

if operation == '1':
    print(f'{num1} plus {num2} equals {num1+num2}')
elif operation == '2':
    print(f'{num1} minus {num2} equals {num1-num2}')
elif operation == '3':
    print(f'{num1} times {num2} equals {num1*num2}')
elif operation == '4':
    print(f'{num1} divided by {num2} equals {num1/num2}')
else:
    print('Error: Invalid Operation \nError Code: p1s3nt3r4numfr0m1-4')
# ps. in case you're having trouble reading the error code it says "pls enter a num from 1-4" but some of the letters are replaced with numbers