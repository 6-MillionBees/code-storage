# Arden Boettcher
# 12/2/24
# World Variables

from dice import *


# distance_traveled = 0

karma = 1

luck_bonus = 0

dun_level = 1
difficulty = 1 + dun_level / 5

luck = lambda: (karma - 1) * 8 + 10 + luck_bonus
luck_mod = lambda: int((luck() - 10) / 2)

WIDTH = 5
HEIGHT = 5
dun_level = 1

from default_functions import *

def make_dungeon():
    dungeon = []
    for row in range(WIDTH):
        dungeon.append([])

        for column in range(HEIGHT):
            type = randint(1, 25)

            if type <= 4:
                encounter_type_num = randint(1, 100)
                encounter_type = 'goblin'
                if encounter_type_num <= 20:
                    encounter_type = 'goblin'
                elif encounter_type_num > 20 and encounter_type_num <= 40:
                    encounter_type = 'kobold'
                elif encounter_type_num > 40 and encounter_type_num <= 50:
                    encounter_type = 'slime'
                elif encounter_type_num > 50 and encounter_type_num <= 70:
                    encounter_type = 'mixed'
                elif encounter_type_num > 70 and encounter_type_num <= 80:
                    encounter_type = 'la creatura'
                elif encounter_type_num > 80 and encounter_type_num <= 85:
                    encounter_type = 'kyle'
                elif encounter_type_num > 85 and encounter_type_num <= 90:
                    encounter_type = 'gronk'
                elif encounter_type_num > 90 and encounter_type_num <= 96 and difficulty >= 3:
                    encounter_type = 'dangolf'
                elif encounter_type_num > 96 and encounter_type_num <= 99:
                    encounter_type = 'siffrin traveler'
                elif encounter_type_num == 100 and difficulty >= 5:
                    encounter_type = 'siffrin lost'
                else:
                    encounter_type = 'slime'

                dungeon[row].append(['encounter', encounter_type, False, True])

            elif 4 < type <= 6:
                dungeon[row].append(['chest', None, False, True])

            elif 6 < type <= 8:
                trap_type_rand = randint(1, 10)
                if trap_type_rand <= 5:
                    trap_type = 'dart'
                elif 5 < trap_type_rand <= 10:
                    trap_type = 'spike'
                dungeon[row].append(['trap', trap_type, False, True])

            else:
                dungeon[row].append(['empty', None, False, True])

    def find_entrance(dungeon):
        while True:
            for row in dungeon:
                for column in row:
                    if column[0] == 'empty':
                        entrance_rand = randint(1, 25)
                        if entrance_rand == 1:
                            column[0] = 'entrance'
                            column[2] = True
                            column[3] = False
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
            if column[3]:
                printing_dungeon += '█'
            elif column[2] == True:
                printing_dungeon += f'{Fore.GREEN}+{Fore.RESET}'
            elif column[0] == 'empty':
                printing_dungeon += '·'
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


from fighting_functions import *
from npc_stats import *



def dungeon_encounters(column):
    if column[1] == 'goblin':
        no_of_enemies = randint(2, 4)
        if no_of_enemies == 2:
            encounter = fight(goblin, goblin)
        elif no_of_enemies == 3:
            encounter = fight(goblin, goblin, goblin)
        elif no_of_enemies == 4:
            encounter = fight(goblin, goblin, goblin, goblin)

    if column[1] == 'kobold':
        no_of_enemies = randint(3, 4)
        if no_of_enemies == 3:
            encounter = fight(kobold, kobold, kobold)
        elif no_of_enemies == 4:
            encounter = fight(kobold, kobold, kobold, kobold)

    if column[1] == 'slime':
        no_of_enemies = randint(1, 4)
        if no_of_enemies == 1:
            encounter = fight(slime)
        elif no_of_enemies == 2:
            encounter = fight(slime, slime)
        elif no_of_enemies == 3:
            encounter = fight(slime, slime, slime)
        elif no_of_enemies == 4:
            encounter = fight(slime, slime, slime, slime)
    
    if column[1] == 'mixed':
        encounter = fight(goblin, kobold, slime)

    if column[1] == 'la cretura':
        encounter = fight(la_creatura, slime)

    if column[1] == 'kyle':
        random_kyile = randint(1, 2)
        if random_kyile == 1:
            encounter = fight(kile)
        elif random_kyile == 2:
            encounter = fight(kyle)

    if column[1] == 'gronk':
        encounter = fight(gronk, godwin)
    
    if column[1] == 'dangolf':
        encounter = fight(dangolf)

    if column[1] == 'siffrin traveler':
        encounter = fight(siffrin_traveler)

    if column[1] == 'siffrin lost':
        encounter = fight(siffrin_lost)

    return encounter




def dungeon_trap(column):
    global current_player_health

    rolling('')
    wis_save = skill_save('wis mod', 10 + int(difficulty / 2))

    if column == 'dart':
        if wis_save == True:

            print()
            print('You spot small holes in the walls.')
            print('You know from experience that this is a dart trap.')
            print('Unfortunately the door to the previous room has closed.')
            print('The only way forward is to defuse it.\n')
            cont()

            rolling('Intelegence Save')
            int_save = skill_save('int mod', 10 + int(difficulty / 3))

            if int_save == True:
                print('You manage to defuse the trap, letting you move forward.')
                cont()
                return

        if wis_save == False or int_save == False:
            print('The dart trap inside of the room goes off!')
            rolling('Dexterity Save')
            dex_save = skill_save('dex mod', 10 + int(difficulty / 2))
            if dex_save == True:
                damage = d4()
                print('You managed to dodge the majority of the darts!')
                print(f'You only took {damage} damage.')
                cont()
            elif dex_save == False:
                damage = d4(3)
                print('You don\'t manage to react in time.')
                print(f'You took {damage} damage.')
                cont()
            current_player_health -= damage

    elif column == 'spike':
        if wis_save == True:

            print()
            print('You spot a poorly hidden pit.')
            print('it\'s filled with deadly spikes')
            print('(who keeps on making these things???)')
            print('The door behind you closed.')
            print('Looks like you\'re going to have to jump it.')
            cont()

            rolling('Strength Save')
            str_save = skill_save('str mod', 10 + int(difficulty / 2))

            if str_save == True:
                print('You just barely manage to jump over the gap.')
                cont()
                return
        elif str_save == False or wis_save == False:
            print('You fall into a spike trap!')
            rolling('Dexterity Save')
            dex_save = skill_save('dex mod', 10 + int(difficulty / 2))
            if dex_save == True:
                damage = d4()
                print('You manage to flail your arms enough to keep balance')
                print(f'You took no damage.')
                cont()
            elif dex_save == False:
                damage = d4(3)
                print('You fell right into the traps thorny embrace.')
                print(f'You took {damage} damage.')
                cont()
            current_player_health -= damage


from items import *

def dungeon_chest():
    rarity = randint(luck_mod * 10, 100)
    if rarity <= 25:
        print('You find a chest')
        print('The chest is empty.')
        print(':(')
        cont()

    elif rarity <= 75:
        item_rand = randint(1, 25)
        print('You found a common chest!')
        print('You open it')
        cont()
        rolling('for goodies')
        if item_rand <= 5:
            item = ['weapon', 'dagger']
        elif item_rand <= 10:
            item = ['basic', 'health potion', 5]
        elif item_rand <= 15:
            item = ['basic', 'silver pieces', 40]
        elif item_rand <= 20:
            item = ['weapon', 'trident']
        elif item_rand <= 24:
            item = ['weapon', 'warhammer']
        elif item_rand == 25:
            item = ['weapon', 'greataxe']

    elif rarity <= 99:
        item_rand = randint(1, 5)
        print('You found a rare chest.')
        cont()
        rolling('for goodies')
        if item_rand <= 2:
            item = ['basic', 'silver pieces', 75]
        if item_rand == 3:
            item = ['basic', 'gold pieces', randint(1, 2)]
        if item_rand == 4:
            item = ['weapon', 'greataxe']
        if item_rand == 5:
            item = ['weapon', 'maul']

    elif rarity == 100:
        item_rand = randint(1, 6)
        print('JACKPOT!!!!')
        print('You found a Legendary chest.')
        cont()
        rolling('for goodies')
        if item_rand <= 2:
            item = ['weapon', 'golden spirit']
        elif item_rand <= 4:
            item = ['weapon', 'player sif\'s dagger']
        elif item_rand == 5:
            item = ['weapon', 'dangolf staff']
        elif item_rand == 6:
            item = ['weapon', 'gun']

    if item[0] == 'basic':
        player_equipment[item[1]] += item[2]
    elif item[0] == 'weapon':
        pickupweapon(item[1])




def dungeon_exit():
    global dun_level

    print('You found a starecase leading down!')
    while True:
        print('do you want to go down?')
        print('''
        1.) Yes
        2.) No''')
        go_down = int_input('')
        if go_down == 1:
            dun_level += 1
            return True
        elif go_down == 2:
            return False
        else:
            invalid()

def dungeon_effects(dungeon):
    global player_is_alive

    for row in dungeon:
        for column in row:
            if column[2] == True:
                if column[0] == 'encounter':
                    if column[3]:
                        dungeon_encounters(column)
                        if current_player_health <= 0:
                            player_is_alive = False
                            return
                    else:
                        print('You\'ve been here before.')

                elif column[0] == 'chest':
                    if column[3]:
                        dungeon_chest()
                        column[3] = False
                        return
                    else:
                        print('You\'ve been here before.')

                elif column[0] == 'trap':
                    dungeon_trap(column[1])
                    if current_player_health <= 0:
                        player_is_alive = False
                        return

                elif column[0] == 'exit':
                    if column[3]:
                        column[3] = False
                    exit_choice = dungeon_exit()
                    if exit_choice == True:
                        return True

                elif column[0] == 'empty':
                    print('The room is empty.')
                elif column[0] == 'entrance':
                    print('You are at the entrance')




def player_move_left(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        row[row.index(column) - 1][2] = True
                        column[2] = False
                    except IndexError:
                        invalid()
                        return dungeon
                    print('You move to the left.')
                    return dungeon

def player_move_right(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        row[row.index(column) + 1][2] = True
                        column[2] = False
                    except IndexError:
                        invalid()
                        return dungeon
                    print('You move to the right.')
                    return dungeon

def player_move_up(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        dungeon[dungeon.index(row) - 1][row.index(column)][2] = True
                        column[2] = False
                    except IndexError:
                        invalid()
                        return dungeon
                    print('You move up.')
                    return dungeon

def player_move_down(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        dungeon[dungeon.index(row) + 1][row.index(column)][2] = True
                        column[2] = False
                    except IndexError:
                        invalid()
                        return dungeon
                    print('You move down.')
                    return dungeon


from player_stats import rest
# from main import dungeon

def movement_menu():
    global dungeon

    while True:
        print('Please pick a direction:')
        print('''    1.) Up
    2.) Down
    3.) Left
    4.) Right
    5.) Rest''')
        direction = int_input()
        if direction == 5:
            rest()
            rested = True
            break
        elif direction == 1:
            dungeon = player_move_up(dungeon)
            break
        elif direction == 2:
            dungeon = player_move_down(dungeon)
            break
        elif direction == 3:
            dungeon = player_move_left(dungeon)
            break
        elif direction == 4:
            dungeon = player_move_right(dungeon)
            break
        else:
            invalid()



