# Arden Boettcher
# 11-11-24
# zip-function


# 2

last_names = ['CLAPTON', 'WAYNE', 'SANTANA']
first_names = ['Eric', 'Bruce', 'Carlose']

for last_name, first_name in zip(last_names, first_names):
    print(f'{last_name}, {first_name}')


# 4

names = ['Lucas', 'Keily']
cities = ['Interlochen', 'Elk Rapids']
counties = ['Grand Traverse', 'Antrim']

for name, city, county, in zip(names, cities, counties):
    print(f'{name} lives near {city} in {county} county')