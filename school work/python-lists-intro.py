# Arden Boettcher
# 10/21/24
# Python Lists Intro

print('3-1 and 3-2')
names = ['Oliver', 'Sophie', 'Evelyn']

for x in names:
    print(f'''
Hi {x}!
    I'm just checking in, hope you're having a wonderful day!
Don't forget that we're walking to goodwill this wednesday, I can't wait!''')

print()
print('3-3')

from time import sleep
from random import randint

trans = ['Car', 'Bike', 'Train', 'Plane']

print(f'I would like to own my dad\'s {trans[0]}, But I need to get a job first :(')


print('Extra little thing')
input('Press enter to roll the dice\n')
boolian = True
num = 0.05
x = randint(0, 3)

while boolian:
    if num < 0.5:
        num += 0.05
    else:
        num += 0.1
    if x > 3:
        x -= 4
    if num > 1:
        break
    print(f'\r{trans[x]}  ', end = '')
    x += 1
    sleep(num)

if x == 3:
    x = 2

print('\rWe Have a Winner!!!')
print(f'The best mode of transportation is:\n{trans[x]}')