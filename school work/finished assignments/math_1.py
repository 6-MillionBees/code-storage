# Arden Boettcher
# 9/11/24
# Basic Math Challenges


# question 1

print('What is the width')

width = int(input())

print('what is the length')

length = int(input())

print(length * width)

# question 2

print('What is the bill?')

bill = float(input())

total = bill * 1.20

print('the total is: $' + "{:.2f}".format(round(total, 2)))

# question 3

print('What is the width?')

width_cube = int(input())

print('What is the length?')

length_cube = int(input())

print('What is the hight?')

hight_cube = int(input())

volume = length_cube * width_cube * hight_cube

print(f'The volume is {volume}')

surface_area = (length_cube * width_cube * 2) + (length_cube * hight_cube * 2) + (width_cube * hight_cube * 2)

print(f'The total surface area is {surface_area}')


