# Arden Boettcher
# 11/14/24
# Positional Arguments


# POSITIONAL ARGUMENTS
# Start by writing the code to create the three functions outlined below
# You'll use only positional arguments in the first three functions
# Test your code and correct any errors

# Greet The User
# Write a function that takes two parameters -- first name and age
# Use an f-string to welcome the user by first name and to display his/her age

def greet(fname, age):
    print(f'Hello {fname}, your age is {age}')

greet('Nolan', 45)


# Area of a Rectangle
# Write a function to calculate the area (in square feet) of a rectangle
# Your two parameters will be length and width
# The print statement in the function should display the length, width and area (in square feet) of your rectangle

def area_calc(length, width):
    area = length * width
    print(f'The square with the dimensions of {length} by {width} has an area of {area}')

area_calc(8, 7)

# Sum of Numbers
# Write a function that finds the sum of three numbers
# Your three parameters will be num1, num2, and num3
# The print statement in the function should display the sum of the three numbers

def sum_of(num1, num2, num3):
    sum = num1 + num2 + num3
    print(f'the sum of {num1}, {num2}, {num3} is {sum}')

sum_of(13, 16, 21)

# KEYWORD ARGUMENTS
# Create the three functions outlined below
# In these last three functions, you'll use only keyword arguments 
# Test your code and correct any errors

# Greet By Title
# Write a function that greets the user by title, first name and last name
# Examples of titles include: Mr., Ms., Mrs. and Dr.
# When calling your function, change the order of your keyword arguments so that they don't match the order of your function parameters

def greet_by_title(title, name):
    print(f'Hello {title} {name}')

greet_by_title(name = 'Nolan', title = 'Mr.')

# Describe Your Pet
# Write a function that says what type of pet you have and what your pet's name is
# Your function parameters will be pet_type and pet_name

def pet(pet_type, pet_name):
    print(f'I\'m going to stick with the classics and get a {pet_type}, and I\'m going to name it {pet_name}')

pet(pet_name = 'Megatron', pet_type = 'cat')

# Updated Function
# Choose any ONE of the first three functions from this project and rewrite it below using keyword arguments

area_calc(width = 92, length = 47)