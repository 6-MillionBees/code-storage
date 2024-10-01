# Arden Boettcher
# 10/1/14
# If-Else starter


# Task 1

task1_complete = True

# Task 2

alien_color = 'green'

if alien_color == 'green':
    print('You earned 5 points!\n')
else:
    print('You earned 10 points!\n')

# Task 3

username = input('Please enter your username: ')
username_len = len(username)

if username_len <= 5:
    print('Welcome!\n')
elif username_len > 5:
    print('Username too short.\n')

# Task 4

alph = input('Please enter a letter from the alphabet: ')
alphlower = alph.lower

if 'a' or 'e' or 'i' or 'o' or 'u' in alphlower:
    print('That letter is a vowel\n')
elif 'y' in alphlower:
    print('Depends on who you ask.\n')
else:
    print('That letter is a consonant\n')

# Task 5

int1 = int(input('Please enter a number: '))
int2 = int(input('Please enter another number: '))
left = int1 % int2

if left == 0:
    print(f'{int1} is divisible by {int2}.\n')
else:
    print(f'{int1} is not divisible by {int2}.\n')
