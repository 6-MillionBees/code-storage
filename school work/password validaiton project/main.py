# Arden Boettcher
# 12/18/24
# Password Validation Project


def check_length(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters.'
    return

def check_last_three(password):
    if len(password) >= 3 and not password[-3:-1].isdigit():
        return 'The last three characters must be numbers.'
    return



def check_first_five(password):
    if len(password) >= 5 and not password[0:5].isalpha():
        return 'The first five characters must be letters'
    return