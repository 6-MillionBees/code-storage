# Arden Boettcher
# 9/18/24
# IPO part 2 / Python Simple-Calc

num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))

total = num1 + num2

total_find = str(total).find('.') # This is my overly complex way to limit the number of decimal places to keep the answer from going off the rails
offset = int(total_find) + 3


print('The sum of the two numbers is ' + str(total)[0:offset])