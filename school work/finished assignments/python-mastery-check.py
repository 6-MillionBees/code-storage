# Arden Boettcher
# 10/11/24
# Python Mastery Check

length = float(input('Please enter the length of your room in feet (only numbers please): '))
width = float(input('Please enter the width of your room in feet (only numbers please): '))

price_per_yard = float(input('Please enter the price per square yard for the desired carpet (only numbers please): '))

sq_yards = length / 3 * width / 3
price = price_per_yard * sq_yards 

print(f'You need {sq_yards:.2f} square yards of carpet.')
print(f'The price without tax is: ${price:.2f}')
print(f'The sales tax is: ${price * 0.06:.2f}')
print(f'Your total is: ${price * 1.06:.2f}')
