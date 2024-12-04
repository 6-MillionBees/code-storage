# Arden Boettcher
# 12/2/24
# World Variables

from dice import *


days = 0
# distance_traveled = 0

karma = 1

luck_bonus = 0

difficulty = 1 + days / 10 * karma

luck = lambda: (karma - 1) * 8 + 10 + luck_bonus
luck_mod = lambda: int((luck() - 10) / 2)

WIDTH = 5
HEIGHT = 5

from default_functions import *

def make_dungeon():
    dungeon = []
    for row in range(WIDTH):
        dungeon.append([])

        for column in range(HEIGHT):
            type = randint(1, 25)

            if type <= 4:
                encounter_type_num = randint(1, 100)
                if encounter_type_num <= 20:
                    encounter_type = 'goblin'
                elif encounter_type_num > 20 and encounter_type_num <= 40:
                    encounter_type = 'kobold'
                elif encounter_type_num > 40 and encounter_type_num <= 50:
                    encounter_type_num = 'slime'
                elif encounter_type_num > 50 and encounter_type_num <= 70:
                    encounter_type = 'mixed'
                elif encounter_type_num > 70 and encounter_type_num <= 80:
                    encounter_type = 'la creatura'
                elif encounter_type_num > 80 and encounter_type_num <= 85:
                    encounter_type = 'kyle'
                elif encounter_type_num > 85 and encounter_type_num <= 90:
                    encounter_type = 'gronk'
                elif encounter_type_num > 90 and encounter_type_num <= 96 and difficulty < 3:
                    encounter_type = 'goblin'
                elif encounter_type_num > 90 and encounter_type_num <= 96 and difficulty >= 3:
                    encounter_type = 'dangolf'
                elif encounter_type_num > 96 and encounter_type_num <= 99:
                    encounter_type = 'siffrin traveler'
                elif encounter_type_num == 100:
                    encounter_type = 'siffrin lost'
                else:
                    encounter_type = 'goblin'
                dungeon[row].append(['encounter', encounter_type])
            elif 4 < type <= 6:
                dungeon[row].append(['chest'])
            elif 6 < type <= 8:
                dungeon[row].append(['trap'])
            else:
                dungeon[row].append(['empty'])

    def find_entrance(dungeon):
        while True:
            for row in dungeon:
                for column in row:
                    if column[0] == 'empty':
                        entrance_rand = randint(1, 25)
                        if entrance_rand == 1:
                            column[0] = 'entrance'
                            column.append('player')
                            return dungeon

    def find_exit(dungeon):
        while True:
            for row in dungeon:
                for column in row:
                    if column[0] == 'empty':
                        entrance_rand = randint(1, 25)
                        if entrance_rand == 1:
                            column[0] = 'exit'
                            return dungeon

    dungeon = find_entrance(dungeon)
    dungeon = find_exit(dungeon)

    return dungeon




def print_dungeon(dungeon):
    printing_dungeon = ''
    for row in dungeon:
        for column in row:
            print(column) # WIP
            if column[-1] == 'player':
                printing_dungeon += f'{Fore.GREEN}+{Fore.RESET}'
            elif column[0] == 'empty':
                printing_dungeon += '.'
            elif column[0] == 'exit':
                printing_dungeon += 'E'
            elif column[0] == 'encounter':
                printing_dungeon += 'F'
            elif column[0] == 'chest':
                printing_dungeon += 'C'
            elif column[0] == 'trap':
                printing_dungeon += 'T'
            elif column[0] == 'entrance':
                printing_dungeon += 'e'
        printing_dungeon += '\n'
    print(printing_dungeon)



def player_move_left(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[-1] == 'player':
                    try:
                        row[row.index(column) - 1][-1] = 'player'
                        column.remove(column[-1])
                    except IndexError:
                        invalid()
                        return dungeon
                    return dungeon

def player_move_right(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[-1] == 'player':
                    try:
                        row[row.index(column) + 1][-1] = 'player'
                        column.remove(column[-1])
                    except IndexError:
                        invalid()
                        return dungeon
                    return dungeon




dungeon = make_dungeon()
print_dungeon(dungeon) # REMOVE AFTER TESTING

print('move right')
dungeon = player_move_right(dungeon)
print_dungeon(dungeon)

print('move left')
dungeon = player_move_left(dungeon)
print_dungeon(dungeon)
