# Arden Boettcher
# 11/22/24
# Try Except Starter


# Doing Addition


while True:
    try:
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))
    except ValueError:
        print('Invalid Input: Please enter a valid integer')
    else:
        break

print(f'The sum of {num1} and {num2} is {num1 + num2}')


# Invalid List Element

my_scores = []

while True:
    try:
        list_element = int(input('Please enter a number:'))
    except ValueError:
        print('Invalid Input: Please enter a valid integer')
    else:
        my_scores.append(list_element)
        break

# Invalid Index

my_nums = [10, 20, 30, 40, 50, 60]

while True:
    try:
        index_num = int(input('Enter an integer between 0 and 5'))
        print(f'The item you are looking for is: {my_nums[index_num]}')
    except IndexError:
        print('Index Out Of Range: Enter an index between 0 and 5')
    except ValueError:
        print('Invalid Input: Please enter a valid ingeger')
    else:
        break