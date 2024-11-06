# Arden Boettcher
# 11/6/ 24
# For Loops Part 2

# Counting Up and Down

while True:
    try:
        user_number = int(input('Please enter a number'))
    except ValueError:
        print('Invalid Input: please try again')
    else:
        break

for x in range(user_number + 1):
    