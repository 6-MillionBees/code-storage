import random

def d10(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        rollnum = lambda: random.randint(1, 10)
        roll += rollnum()
    return roll

dict = {
    'a': (lambda num = 1: d10(num))
}

print(dict['a']())

print(dict['a']())