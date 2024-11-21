# Arden Boettcher
# 11/19/24
# Return Starter


# Destination Europe

def describe_vacation(destination, activity, season = 'summer'):
    return f'I am going to {destination} during {season} where I will {activity}.'

description1 = describe_vacation('Finland', 'walk around')
description2 = describe_vacation('Thailand', 'sweat to death', 'spring')

print(description1)
print(description2)
print()


# Student Major

def show_major(first_name, university, major = 'Sports Medicine'):
    return f'{first_name.title()} attends the {university} and is majoring in {major}'

print(show_major('joffery', 'North Michigan College', 'Computer Science'))
print(show_major('Karla', 'Michigan State Univercity'))
print()
