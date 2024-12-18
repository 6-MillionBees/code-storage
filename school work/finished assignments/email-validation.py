# Arden Boettcher
# 12/10/24
# Input Validation

username = input('Please enter your username: ')

def validate_username(name):
    if name.isalpha():
        return 'Username is valid (consists of letters only)\n'
    elif name.isdigit():
        return 'Username is valid (consists of digits only)\n'
    else:
        return 'Invalid username!\n'

print(validate_username(username))