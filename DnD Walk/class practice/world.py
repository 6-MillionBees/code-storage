# Arden Boettcher
# 12/2/24
# World Variables

from dice import *
from main import user
from player_stats import skill_save

# distance_traveled = 0

karma = 1

luck_bonus = 0

dun_level = 1
difficulty = 1 + (dun_level - 1) / 5

luck = lambda: (karma - 1) * 8 + 10 + luck_bonus
luck_mod = lambda: int((luck() - 10) / 2)

WIDTH = 5
HEIGHT = 5
dun_level = 1
player_is_alive = True

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
    print(f'Floor {dun_level}')
    printing_dungeon = ''
    for row in dungeon:
        for column in row:
            if column[2] == True:
                printing_dungeon += f'{Fore.GREEN}+{Fore.RESET}'
            elif column[3]:
                printing_dungeon += '█'
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


from npc_stats import *
from fighting_functions import fight


def dungeon_encounters(column):
    if column[1] == 'goblin':
        no_of_enemies = randint(2, 4)
        if no_of_enemies == 2:
            encounter = fight(goblin, goblin)
        elif no_of_enemies == 3:
            encounter = fight(goblin, goblin, goblin)
        elif no_of_enemies == 4:
            encounter = fight(goblin, goblin, goblin, goblin)

    elif column[1] == 'kobold':
        no_of_enemies = randint(3, 4)
        if no_of_enemies == 3:
            encounter = fight(kobold, kobold, kobold)
        elif no_of_enemies == 4:
            encounter = fight(kobold, kobold, kobold, kobold)

    elif column[1] == 'slime':
        no_of_enemies = randint(1, 4)
        if no_of_enemies == 1:
            encounter = fight(slime)
        elif no_of_enemies == 2:
            encounter = fight(slime, slime)
        elif no_of_enemies == 3:
            encounter = fight(slime, slime, slime)
        elif no_of_enemies == 4:
            encounter = fight(slime, slime, slime, slime)
    
    elif column[1] == 'mixed':
        encounter = fight(goblin, kobold, slime)

    elif column[1] == 'la cretura':
        encounter = fight(la_creatura, slime)

    elif column[1] == 'kyle':
        print('You walk into a room, and you see a person standing there like a weirdo.')
        print('He asks you "Is K?le spelled with an I or a Y?".')

        while True:
            answer = int_input('''    1.) "With an I!"
        2.) "With a Y!"
    > ''')
            if answer == 1:
                print('He gets visibly angry with your answer and he charges at you with his sword drawn.')
                encounter = fight(kyle)
                break
            elif answer == 2:
                print('He gets visibly angry with your answer and he charges at you with his sword drawn.')
                encounter = fight(kile)
                break
            else:
                invalid()

    elif column[1] == 'gronk':
        encounter = fight(gronk, lily)
    
    elif column[1] == 'dangolf':
        encounter = fight(dangolf)

    elif column[1] == 'siffrin traveler':
        encounter = fight(siffrin_traveler)

    elif column[1] == 'siffrin lost':
        encounter = fight(siffrin_lost)
    
    else:
        encounter = fight(goblin, goblin)

    return encounter




def dungeon_trap(column):

    damage = 0

    if column[3] == False:
        print('You\'ve been here before')
        return 0

    rolling('')
    wis_save = skill_save(user.mods['wis mod'], 10 + int(difficulty / 2))

    if column == 'dart':
        int_save = False
        if wis_save == True:

            print()
            print('You spot small holes in the walls.')
            print('You know from experience that this is a dart trap.')
            print('Unfortunately the door to the previous room has closed.')
            print('The only way forward is to defuse it.\n')
            cont()

            rolling('Intelegence Save')
            int_save = skill_save(user.mods['int mod'], 10 + int(difficulty / 3))

            if int_save == True:
                print('You manage to defuse the trap, letting you move forward.')
                return damage

        if wis_save == False or int_save == False:
            print('The dart trap inside of the room goes off!')
            rolling('Dexterity Save')
            dex_save = skill_save(user.mods['dex mod'], 10 + int(difficulty / 2))
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
        return damage

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
            str_save = skill_save(user.mods['str mod'], 10 + int(difficulty / 2))

            if str_save == True:
                print('You just barely manage to jump over the gap.')
                cont()
                return damage
        else:
            print('You fall into a spike trap!')
            rolling('Dexterity Save')
            dex_save = skill_save(user.mods['dex mod'], 10 + int(difficulty / 2))
            if dex_save == True:
                print('You manage to flail your arms enough to keep balance')
                print(f'You took no damage.')
            elif dex_save == False:
                damage = d4(3)
                print('You fell right into the traps thorny embrace.')
                print(f'You took {damage} damage.')
        return damage


from items import *

def dungeon_chest():
    rarity = randint(luck_mod() * 10, 100)
    if rarity <= 25:
        print('You find a chest')
        print('The chest is empty.')
        print(':(')

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
        item_rand = randint(1, 10)
        print('You found a rare chest.')
        cont()
        rolling('for goodies')
        if item_rand <= 5:
            item = ['basic', 'health potion', 10]
        elif item_rand <= 7:
            item = ['basic', 'silver pieces', 75]
        if item_rand == 8:
            item = ['basic', 'gold pieces', randint(1, 2)]
        if item_rand == 9:
            item = ['weapon', 'greataxe']
        if item_rand == 10:
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

    try:
        if item[0] == 'basic':
            print(f'You obtained {item[2]} {item[1]}')
            player_equipment[item[1]] += item[2]
        elif item[0] == 'weapon':
            pickupweapon(item[1])
    except UnboundLocalError:
        return




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
    global player_exp
    global current_player_health
    global player_is_alive

    for row in dungeon:
        for column in row:
            if column[2] == True:
                if column[0] == 'encounter':
                    if column[3]:
                        player_is_alive = dungeon_encounters(column)
                        if player_is_alive == False:
                            return
                        print(user.current_exp, user.needed_exp)
                        print(user.current_exp >= user.needed_exp)
                        if user.current_exp >= user.needed_exp:
                            user.level_up()
                        column[3] = False
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
                    if column[3]:
                        user.current_health -= dungeon_trap(column[1])
                        if user.current_health <= 0:
                            player_is_alive = False
                            return
                        column[3] = False
                    print(user.current_health, user.health)

                elif column[0] == 'exit':
                    column[3] = False
                    exit_choice = dungeon_exit()
                    if exit_choice == True:
                        return True

                elif column[0] == 'empty':
                    print('The room is empty.')
                    column[3] = False

                elif column[0] == 'entrance':
                    print('You are at the entrance')




def player_move_left(dungeon):
    while True:
        for row in dungeon:
            for column in row:
                if column[2] == True:
                    try:
                        if row.index(column) - 1 == -1:
                            raise IndexError
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
                        if dungeon.index(dungeon[dungeon.index(row)]) - 1 == -1:
                            raise IndexError
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


from main import user

def movement_menu(dungeon):
    global rested
    while True:
        print('Please pick a direction:')
        print('''    1.) Up
    2.) Down
    3.) Left
    4.) Right
    5.) Menu
    6.) Rest''')
        direction = int_input()
        if direction == 6:
            user.rest(False)
            return dungeon
        
        elif direction == 5:
            user.rest(True)
            return dungeon

        elif direction == 1:
            return player_move_up(dungeon)

        elif direction == 2:
            return player_move_down(dungeon)

        elif direction == 3:
            return player_move_left(dungeon)

        elif direction == 4:
            return player_move_right(dungeon)

        else:
            invalid()