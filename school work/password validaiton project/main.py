# Arden Boettcher
# 12/18/24
# Password Validation Project


def check_length(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters.'
    return

def check_last_three(password):
    if len(password) >= 3 and not password[-3:].isdigit():
        return 'The last three characters must be numbers.'
    return


def check_first_five(password):
    if len(password) >= 5 and not password[0:5].isalpha():
        return 'The first five characters must be letters.'
    return

def check_for_letter(password):
    for char in password:
        if char.isalpha():
            return
    return 'Your password must include a letter.'

def check_special_chararcters(password):
    for char in password:
        if char not in 'abcdefghijklmnopqrstuvwxyz0123456789':
            return
    return 'Your password must include a special character.'

def check_for_number(password):
    for char in password:
        if char.isdigit():
            return
    return 'Your password mus include a number.'



def validate_password(password):
    errors = []
    checks = [
        check_length(password),
        check_for_letter(password),
        check_for_number(password),
        check_special_chararcters(password),
        check_first_five(password),
        check_last_three(password)]

    for check in checks:
        if check:
            errors.append(check)

    if errors:
        print()
        for error in errors:
            print(error)
        print()
        return False
    else:
        return True




while True:
    password = input('Please enter your password: ')
    valid = validate_password(password)
    if valid:
        print('Password is valid!')
        break
