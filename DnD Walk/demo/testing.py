from dice import *
from npc_stats import goblin
from default_functions import int_input, invalid

spell_damage_increase = 0

enemies = [goblin, goblin, goblin, goblin]

print('You cast Magic Missile')
choice = []
num = 0
while num < 3:
    var = 0
    for enemy in enemies:
        var += 1
        print(f'{var}.) {enemy["name"]}')

    temp_choice = int_input('Which enemy do you attack?: ')
    if temp_choice in range(1, var + 1):
        choice.append(temp_choice)
        num += 1
        continue
    else:
        invalid()
        continue

dictionary = {}
for target in choice:
    dictionary[target] = 0
for target in choice:
    dictionary[target] += d4(1 + int(spell_damage_increase / 2) + 1)

print(dictionary)