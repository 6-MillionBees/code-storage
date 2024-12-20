
while True:
    num = int(input('Guess a number between 1 and 100 \n'))
    txt = 'Nope! Too txt'

    if num > 5:
        print(txt.replace('txt', 'high'))
    elif num < 5:
        print(txt.replace('txt', 'low'))
    elif num == 5:
        print('You did it!')
        break

# endswith() practice

div_by_two = input('enter a number: \n')
numbers = ('0', '2', '4', '6', '8')
x = div_by_two.endswith(numbers)

if x == True:
    print('This number is divisible by 2')
else:
    print('That number is not divisible by 2')

# join() practice

mytuple = ('something', 'another thing', 'and one more thing')

x = ', '.join(mytuple)
print(x)

# find practice

import time

find = input('put in a bunch of numbers: ')
num = input('What number do you want to find?: ')

findfind = find.find(num)

find_plus = int(findfind) + 2
find_minus = int(findfind) - 1 
find_plus_big = int(findfind) + 4
find_minus_big = int(findfind) - 3

print(find[find_minus_big : find_plus_big])
time.sleep(1)
print(f'Tracking {num}...')
time.sleep(2)
print('locating...')
time.sleep(2)
print(find[find_minus : find_plus])
time.sleep(1)
print('almost...')
time.sleep(3)
print('GOT IT!')
time.sleep(1)
print(find[findfind])