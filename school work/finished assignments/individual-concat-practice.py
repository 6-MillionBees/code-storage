# Arden Boettcher
# 9/11/24
# String Concatenation

# Part 1
# Use concatenation to build and display a string that displays which city and state you live in


city = 'Traverse City, '
state = 'Michigan'

print('I live in ' + city + state)


# Part 2
# Create a custom message that welcomes the user by first name to a game you created
# Create one variable to store the user's first name
# Create another variable that stores the welcome message
# Use concatenation to create the customized message


print('What\'s your first name?')

first_name = str(input())

print('Welcome ' + first_name + ' to Adventuria!')


# Part 3
# Assign a number to your age variable
# Use the built-in Python str( ) function to convert your age to a string (when doing concatenation)
# Use concatenation to display a sentence that tells us your first name and age


age = 16

print('I am ' + str(age) + ' years old.')


# Part 4
# Use an f-string to build and display a string that contains your first name, last name, and your height in inches


first_name2 = 'Arden'
last_name = 'Boettcher'
height = 'roughly 67'

print(f'My name is {first_name2} {last_name} and I am {height} inches tall ')
