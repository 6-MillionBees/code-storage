# Arden Boettcher
# 11/18/24
# parameter defaults


# 8-3 T-Shirt

def make_shirt(size, message):
    print(f'size: {size} \nmessage: "{message}"')

make_shirt('medium', 'Do I look like I know what a Jpeg is?')

make_shirt(message = 'I just want a picture of a god dang hot dog.', size = 'medium')
print()

# 8-4 Large Shirts

def make_shirt(size = 'large', message = 'I love python'):
    print(f'size: {size} \nmessage: "{message}"')

make_shirt()

make_shirt('medium')

make_shirt(message = '(placeholder quote)')
print()

# 8-5 Cities

def describe_city(city_name, country = 'Finland'):
    print(f'{city_name.title()} is in {country.title()}')

describe_city('Helsinki')

describe_city('Tampere')

describe_city('Traverse City', 'The United States of America')