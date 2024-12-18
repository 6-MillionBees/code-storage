# Arden B, Koen K
# 12/10/24
# Input Validation 2

user = input('Please enter a string: ')

if user.isalpha() or user.isdigit():
    if 6 <= len(user) < 10:
        print(f'Valid input: {user}')
    else:
        print('Input must be between 6 and 10 characters long.')
else:
    print('Input must be alphabetic or numeric (but not both)')