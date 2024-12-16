# Arden Boettcher
# 12/16/24
# Password Checker

def check_password(password):
    numbered = False
    lower = False
    upper = False
    punctuation = False
    length = False
    for character in password:
        if character.isnumeric():
            numbered = True
        elif character in "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~":
            punctuation = True
        elif character.lower() == character:
            lower = True
        elif character.upper() == character:
            upper = True

    if len(password) >= 8:
        length = True
    
    if length and lower and upper and numbered and punctuation:
        print('Valid password.')
        return True
    if length == False:
        print('Password too short.')
    elif lower == False:
        print('Please include lowercase letters.')
    elif upper == False:
        print('Please include uppercase letters.')
    elif numbered == False:
        print('Please include a number.')
    elif punctuation == False:
        print('Please include a special character.')
    return False



while True:
    print()
    password = input('Please enter your password: ')

    if check_password(password):
        break
