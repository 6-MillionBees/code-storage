# Arden B, Koen K
# 12/10/24
# Input Validation 1

user_input = input('Please input words: ')

if user_input.isalpha():
    print(f'Valid input: {user_input}')
else:
    print('Invalid input. Please enter only alphabetic characters')
