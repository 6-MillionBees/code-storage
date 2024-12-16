# Arden Boettcher
# 12/2/24
# NPC Stats

from random import randint
from dice import *
from items import *
from world import luck_mod, difficulty

# Enemies
class enemy_npc:

    def __init__(self, name, health, weapon, mods, agro, exp, score):
        enemy_npc.name     = name
        enemy_npc.health   = health
        enemy_npc.weapon   = weapon
        enemy_npc.mods     = mods
        enemy_npc.alive    = True
        enemy_npc.agro     = agro
        enemy_npc.exp      = exp
        enemy_npc.score    = score
        enemy_npc.blocking = 1

    def __str__(self):
        return self.name

    def health_calc(self):
        self.health = self.health()



    def attack(self, tohit):
        if tohit == 'crit':
            print('\nCritical Hit!')
            damage = weapon_damage[self.weapon]() + self.mods[weapon_mod[self.weapon]] * 2
            cont()
            return damage
        elif tohit == True:
            print('\nAttack hit.')
            cont()
            return weapon_damage[self.weapon]() + self.mods[weapon_mod[self.weapon]]
        elif tohit == False:
            print('\nAttack missed.')
            cont()
            return 0
        else:
            print('\nAttack missed.')
            cont()
            return 0

    def turn(self, player):
        print('It\'s ' + self.name + '\'s turn')
        cont()

        roll = d10() + self.agro

        if roll > 6:
            print(self.name + ' is attacking.\n')

            damage = self.attack(roll_to_hit(d20(), player_ac, self.mods[weapon_mod[self.weapon]]))
            damage = round(damage * player.blocking)

            if damage > 50:
                print(f'You took {Fore.RED}{damage}{Fore.RESET} damage.')
            else:
                print(f'You took {damage} damage.')
                print()
            return 1, damage

        elif roll <= 6:
            print(self.name + ' is blocking.')
            cont()
            return 0.5, 0


goblin = enemy_npc(
    'Goblin',
    (lambda: int((d6(1) + 6) * difficulty)),
    'dagger',
    {'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1},
    5,
    int(50 * difficulty),
    20)

# Basic
goblin = {
    'name': 'Goblin', 'title': '', 'caster': False,
    'health': (lambda: int((d6(1) + 6) * difficulty)), 'weapon': 'dagger', 'ac': 5,
    'exp': int(50), 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1,
    'score': 20
}

kobold = {
    'name': 'Kobold', 'title': '', 'caster': False,
    'health': (lambda: int((d4(4) - 2))), 'weapon': 'dagger', 'ac': 7,
    'exp': int(25), 'agression': 4,
    'str mod': -2, 'dex mod': 2, 'end mod': -1, 'int mod': -1, 'wis mod': -2, 'cha mod': -1,
    'score': 20
}

slime = {
    'name': 'Slime', 'title': '', 'caster': False,
    'health': (lambda: int(d4(2))), 'weapon': 'slime', 'ac': 6,
    'exp': int(26), 'agression': 20,
    'str mod': -4, 'dex mod': -3, 'end mod': 5, 'int mod': -5, 'wis mod': -5, 'cha mod': 1,
    'score': 10
}

la_creatura = {
    'name': 'La Creatura', 'title': '',
    'health': (lambda: int(d4(8))), 'weapon': 'sickle', 'ac': 0,
    'exp': int(50), 'agrssion': 20,
    'str mod': 3, 'dex mod': -2, 'end mod': 4, 'int mod': -3, 'wis mod': -2, 'cha mod': -1,
    'score': 30
}


# Named

lily = {
    'name': 'Lily', 'title': '', 
    'health': (lambda: d6(3) + 10), 'weapon': 'lilys staff', 'ac': 8, 'exp': 250, 'agression': 0,
    'str mod': 0, 'dex mod': 1, 'end mod': 1, 'int mod': 3, 'wis mod': 2, 'cha mod': 1,
    'casting mod': 3,
    'spells': 'firebolt'
}

kile = {
    'name': 'Kile', 'title': ', With An I', 
    'health': (lambda: d4(4) + 20), 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1,
    'casting mod': 0
}

kyle = {
    'name': 'Kyle', 'title': ', With A Y',
    'health': (lambda: d4(4) + 20), 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1,
    'casting mod': 0
}

gronk = {
    'name': 'Gronk', 'title': ', The Killer', 'caster': False,
    'health': (lambda: d6(4) + 20), 'weapon': 'maul', 'ac': 13, 'exp': 200, 'agression': 3,
    'str mod': 4, 'dex mod': -1, 'end mod': 3, 'int mod': -2, 'wis mod': -1, 'cha mod': 0,
    'casting mod': 0
}

siffrin_traveler = {
    'name': 'Siffrin', 'title': ', The Traveler', 'caster': False,
    'health': (lambda: 50), 'weapon': 'dagger', 'ac': 13, 'exp': 500, 'agression': 6,
    'str mod': 0, 'dex mod': 5, 'end mod': 2, 'int mod': 1, 'wis mod': -1, 'cha mod': 2,
    'casting mod': 0
}

siffrin_lost = {
    'name': 'Siffrin', 'title': ', The Lost', 'caster': False,
    'health': (lambda: 999), 'weapon': 'sif dagger', 'ac': 15, 'exp': 9999, 'agression': 10,
    'str mod': 0, 'dex mod': 6, 'end mod': 3, 'int mod': 0, 'wis mod': -2, 'cha mod': 1,
    'casting mod': 0
}

dangolf = {
    'name': 'Dangolf', 'title': ', The Gold',
    'health': (lambda: 150), 'weapon': 'dangolf staff', 'ac': 10, 'exp': 1000, 'agression': 2,
    'str mod': -2, 'dex mod': -2, 'end mod': 2, 'int mod': 5, 'wis mod': 10, 'cha mod': 2,
    'casting mod': 0
}

godwin = {
    'name': 'Godwin', 'title': ', The Golden',
    'health': (lambda: 30), 'weapon': 'golden spirit', 'ac': 12, 'exp': 2000, 'agression': -3,
    'str mod': 5, 'dex mod': 2, 'end mod': 4, 'int mod': 1, 'wis mod': 2, 'cha mod': 10,
    'casting mod': 0
}

# loot tables

def item_pickup(items):
    global player_equipment
    num = 0
    for drop in items[0]:
        player_equipment[drop] += items[1][num]
        print(f'You picked up {items[1][num]} {drop}')
        num += 1


def common_table(no_of_items, enemy):
    drops = []
    numbers = []
    num = 0
    if enemy == dangolf:
        pickupweapon('dangolf staff')

    while num < no_of_items:
        rand = randint(1, 100) + luck_mod()
        if rand < 30:
            drops.append('copper pieces')
            numbers.append(randint(30, 90))
        elif rand > 30 and rand < 50:
            drops.append('arrows')
            numbers.append(randint(1, 10))
        elif rand > 50 and rand < 60:
            drops.append('silver pieces')
            numbers.append(randint(1, 3))
        elif rand > 60 and rand < 75:
            drops.append('health potion')
            numbers.append(1)
        elif rand > 75 and rand < 97:
            drops.append('rope')
            numbers.append(randint(25, 75))
        elif rand > 97:
            drops.append('gold pieces')
            numbers.append(1)
        num += 1
    return drops, numbers, # unique_items