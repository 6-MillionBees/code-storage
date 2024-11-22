# Arden Boettcher
# 11/22/24
# While Loops Starter

# Number Guess Game

from random import randint

goal_number = randint(1, 100)
print('I\'m thinking of a number between 1 and 100.\n')
guesses_taken = 0
win = False

while guesses_taken < 5:
    if guesses_taken == 1:
        print(f'You have {5 - guesses_taken} guess left.')
    else:
        print(f'You have {5 - guesses_taken} guesses left.')
    
    while True:
        try:
            guess = int(input('Enter your guess: '))
        except ValueError:
            print('Invalid Input: Please enter a valid integer.')
        else:
            break
    if guess < goal_number:
        print('That guess was too low.')
    elif guess > goal_number:
        print('That guess was too high!')
    elif guess == goal_number:
        print('You win!!!')
        win = True
        break
    guesses_taken += 1

if not win:
    print(f'You lost. The number I was thinking of was {goal_number}.')


# Managing a List

temperatures_f = []

while True:
    while True:
        try: # get it? TEMPorary TEMPerature I am a genius at wordplay
            temp_temp = int(input('Enter a temperature in Fahrenheit (-9999 to quit): '))
        except ValueError:
            print('Invalid Input: Please enter a valid integer.')
        else:
            break
    if temp_temp == -9999:
        break
    else:
        temperatures_f.append(temp_temp)


temperatures_f_str = [str(temp) for temp in temperatures_f]

print(f'Temperatures entered: {", ".join(temperatures_f_str)}')

average_temp_f = sum(temperatures_f) / len(temperatures_f)
print(f'Average temperature: {average_temp_f}')