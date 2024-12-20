# Arden
# 9/18/24
# Numbers Practice

from colorama import Fore # Everything that starts with Fore is for coloring the text

num1 = float(input('Enter a number: '))
operation = input(f"Enter your Operation \nYou may {Fore.RED}ONLY{Fore.RESET} type '+' for addition, '-' for subtraction, '*' for multiplication, '/' for division. and '^' for exponents\n")
num2 = float(input('Enter another number: '))

while True:
    if operation == '+':
        total = num1 + num2
        break
    elif operation == '-':
        total = num1 - num2
        break
    elif operation == '*':
        total = num1 * num2
        break
    elif operation == '/':
        total = num1 / num2
        break
    elif operation == '^':
        total = num1 ** num2
        break
    else:
        print(Fore.RED + '\nInvalid operation please try again. \n' + Fore.RESET)
        operation = input(Fore.GREEN + "Renter your Operation \nType '+' for addition, '-' for subtraction, '*' for multiplication, and '/' for division. No spaces of \n" + Fore.RESET)

total_find = str(total).find('.')
offset = int(total_find) + 3

print('Your total is ' + Fore.GREEN + str(total)[0:offset] + Fore.RESET)