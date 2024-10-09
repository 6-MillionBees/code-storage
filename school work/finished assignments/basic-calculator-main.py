# Eliot Clarke Arden Boettcher
# 10/8/24
# Basic Calculator

operation = input('''
Welcome to The Amazing Digital Calculator
    *By: Eliot & Arden*

Please enter your operation:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
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
    print(f'{num1} + {num2} = {num1+num2}')
elif operation == '2':
    print(f'{num1} - {num2} = {num1-num2}')
elif operation == '3':
    print(f'{num1} * {num2} = {num1*num2}')
elif operation == '4':
    print(f'{num1} / {num2} = {num1/num2:.2f}')
else:
    print('Error: Invalid Operation \nError Code: p1s3nt3r4numfr0m1-4')
#                                                 plsenteranumfrom1-4