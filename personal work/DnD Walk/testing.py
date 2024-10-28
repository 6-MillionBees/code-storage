import random

def item_pickup(drops, numbers):
    global player_equipment
    num = 0
    for item in drops:
        player_equipment[item] += numbers[num]
        num += 1


def common_table(no_of_items):
    drops = []
    numbers = []
    num = 0
    while num < no_of_items:
        rand = random.randint(1, 100)
        if rand < 30:
            drops.append('copper pieces')
            numbers.append(random.randint(30, 90))
        elif rand > 30 and rand < 50:
            drops.append('arrows')
            numbers.append(random.randint(1, 10))
        elif rand > 50 and rand < 60:
            drops.append('silver pieces')
            numbers.append(random.randint(1, 5))
        elif rand > 60 and rand < 75:
            drops.append('rocks')
            numbers.append(1)
        elif rand > 75 and rand < 97:
            drops.append('rope')
            numbers.append(random.randint(25, 75))
        elif rand > 97:
            drops.append('gold pieces')
            numbers.append(1)
        num += 1
    return drops, numbers

player_equipment = {
    'copper pieces': 0, 'silver pieces': 0,  'gold pieces': 0, 'arrows': 0, 'rocks': 0, 'rope': 0
}

looting = common_table(10)
print(looting[0])
print(looting[1])

item_pickup(looting[0], looting[1])

print(player_equipment)