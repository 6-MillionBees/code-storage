# Arden Boettcher
#9/30/24
# Station Rotation - Station 5


# Task 1
superheros = {'Spiderman', 'Superman', 'Batman', 'Manbat'}

if 'Spiderman' in superheros:
    print('Spiderman is in this list.\n')
else:
    print('Spiderman is not in this list.\n')


# Task 2

quiz_score = int(input('Enter your quiz score: '))

if quiz_score >= 85:
    print('You got a B or above.\n')
else:
    print('You need to study more.\n')


# Task 3

quote = 'Mawwage is wat bwings uws tugetha tudawy - The Princess Bride'

if quote.startswith('M'):
    print('This quote starts with the letter M!\n')
else:
    print('This quote sucks and you should feel bad about it.\n')


# Task 4

filename = 'sillyface.png'

if filename.endswith('.png'):
    print('This file is a png.\n')
else:
    print('Error: file format not compatible\n')


# Task 5

registered = 'yes'

if_registered_yes = registered.endswith('yes')
if_registered_no = registered.endswith('no')

if if_registered_yes:
    print('You are registered to go to classes in NMC.')
elif if_registered_no:
    print('You are not registed to go to classes in NMC.')
else:
    print('yes or no')