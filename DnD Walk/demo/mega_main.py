# Arden Boettcher
# 12/1/24
# Mega Main (testing)

from time import sleep
from colorama import Fore
from random import randint

def d100(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 100)
    return roll

def d20(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 20)
    return roll

def d12(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 12)
    return roll

def d10(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 10)
    return roll

def d8(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 8)
    return roll

def d6(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 6)
    return roll

def d4(number = 1):
    num = 0
    roll = 0
    while num < number:
        num += 1
        roll += randint(1, 4)
    return roll

# I don't want to type this out every time (or copy-paste)
# better on the fingers to have a tiny function do it
def cont(): 
    input('Press enter to continue')
    print()


def invalid(): # same use as cont()
    print(Fore.RED + 'Invalid Input: Please try again' + Fore.RESET)
    cont()

def confirm(): # used to confirm user input
    while True: # like if they make an important decision
        try:
            print('''Are you sure?
    1.) Yes
    2.) No''')
            sure = int(input())
        except ValueError:
            invalid()
        else:
            if sure == 1:
                sure = True
            elif sure == 2:
                sure = False
            else:
                invalid()
                continue
            return sure




def rolling(rolling_for = ''): # this is used for drama *jazz hands*
    x =0
    while x <= 3:
        xperiod = x * '.'
        print(f'\rRolling {rolling_for}{xperiod}',end='')
        x += 1
        sleep(1)
    print()

def roll_to_hit(roll, dc, mod): # use this in combat to check if it hit
    rolling('to hit')
    print(f'{roll}')
    if roll + mod >= 20:
        print(Fore.RED + '\n!!!CRITICAL HIT!!!' + Fore.RESET)
        return 'crit'
    elif roll == 1:
        print('\nCritical Fail.')
        return False
    elif roll + mod < dc:
        print('\nFail.')
        return False
    elif roll + mod >= dc:
        print('\nSuccess!')
        return True

def bar(current, total, bar_length = 20): # This is a bar for health and other things (I'll see what I use it for)
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '█' + '▒'
    padding = int(bar_length - len(arrow)) * '-'
    return f'{arrow}{padding} {round(current)}hp'

def int_input(words = ''):
    while True:
        try:
            choice = int(input(words))
        except ValueError:
            invalid()
            continue
        else:
            break
    return choice


from dice import *


def roll_against(agressor_mod, agressor, defender, defender_mod):
    agressor_roll = d20() + agressor[agressor_mod]
    defender_roll = d20() + defender[defender_mod]
    if agressor_roll > defender_roll:
        return True
    elif agressor_roll < defender_roll:
        return False




def damage_over_time(target, duration, damage, damage_type = ''):
    print('dnd\'s mechanics are going to be my 13 reason.')



def npc_attack(tohit, weapon, enemy):
    if tohit == 'crit':
        print('\nCritical Hit!')
        damage = weapon_damage[weapon]() + enemy[weapon_mod[weapon]] * 2
        cont()
        return damage
    elif tohit == True:
        print('\nAttack hit.')
        cont()
        return weapon_damage[weapon]() + enemy[weapon_mod[weapon]]
    elif tohit == False:
        print('\nAttack missed.')
        cont()
        return 0
    else:
        print('\nAttack missed.')
        cont()
        return 0

def attack(tohit, weapon):
    if tohit == 'crit':
        print(Fore.RED + '\nCritical' + Fore.RESET +' Hit!')
        cont()
        return weapon_damage[weapon]() + player_mods[weapon_mod[weapon]] * 2
    elif tohit == True:
        print('\nYour attack hit.')
        cont()
        return weapon_damage[weapon]() + player_mods[weapon_mod[weapon]]
    elif tohit == False:
        print('\nYou missed.')
        cont()
        return 0
    else:
        print('\nYou missed.')
        cont()
        return 0



def npc_turn(enemy, current_health, blocking):
    global current_player_health
    print('It\'s ' + enemy['name'] + '\'s turn')

    if enemy['caster'] == False:
        roll = d10() + enemy['agression']

        if roll > 6:
            print(enemy['name'] + ' is attacking.\n')

            damage = npc_attack(roll_to_hit(d20(), player_ac, weapon_mod[enemy['weapon']]), enemy['weapon'], enemy)
            damage = round(damage * blocking)

            if damage > 50:
                print(f'You took {Fore.RED}{damage}{Fore.RESET} damage.')
            else:
                print(f'You took {damage} damage.')

        elif roll <= 6:
            enemy_blocking = 0.5
            damage = 0
            print(enemy['name'] + ' is blocking.')

        return 0, damage
    
    elif enemy['caster'] == True:
        roll = d10() + enemy['int mod']

        if roll > 5:
            spell = randint(0, len(enemy['spells']) - 1)
            spell_cast = cast(spell)
    
    return enemy_blocking
    cont()






def player_turn(no_of_enemy, enemy1, enemy2, enemy3, enemy4):
    while True:
        while True:
            print('Your turn.\n')
            print(f'''Player Stats
        Level.............{level}
        Weapon............{weapon_name[player_equipment["equipped weapon"]]} ({weapon_print_damage[player_equipment['equipped weapon']]})
        Health {bar(current_player_health, player_health, 20)}''')
            try:
                player_turn = int(input(f'''
                1. Attack 
                2. Cast
                3. Block\n'''))
            except ValueError:
                invalid()
            else:
                if player_turn in range(1, 4):
                    break
                else:
                    invalid()
        
        if player_turn == 1:
            while True:
                if no_of_enemy == 1:
                    print(f'You attack {enemy1["name"]}')
                    choice = 1

                elif no_of_enemy > 1:
                    print(f'''\nChoose who to attack:
        1. {enemy1["name"]}{enemy1["title"]}
        2. {enemy2["name"]}{enemy2["title"]}''')

                elif no_of_enemy > 2:
                    print(f'    3. {enemy3["name"]}{enemy3["title"]}')

                elif no_of_enemy > 3:
                    print(f'    4. {enemy4["name"]}{enemy4["title"]}')
                print()



                if choice == 1:
                    damage =  attack(roll_to_hit(d20(), enemy1['ac'], weapon_mod[player_equipment['equipped weapon']]), player_equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy1["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy1["name"]} for {damage}')
                    return 'attack', damage, enemy1['name']

                elif choice == 2:
                    damage =  attack(roll_to_hit(d20(), enemy2['ac'], weapon_mod[player_equipment['equipped weapon']]), player_equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy2["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy2["name"]} for {damage}')
                    return 'attack', damage, enemy2['name']

                elif choice == 3:
                    damage =  attack(roll_to_hit(d20(), enemy3['ac'], weapon_mod[player_equipment['equipped weapon']]), player_equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy3["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy3["name"]} for {damage}')
                    return 'attack', damage, enemy3['name']

                elif choice == 4:
                    damage =  attack(roll_to_hit(d20(), enemy4['ac'], weapon_mod[player_equipment['equipped weapon']]), player_equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy4["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy4["name"]} for {damage}')
                    return 'attack', damage, enemy4['name']

                else:
                    print(f'{Fore.RED}Please enter a valid number.{Fore.RESET}')

        elif player_turn == 2:
            spell = spells_menu()
            if spell == -1:
                continue
            else:
                casting = cast(spell, [enemy1, enemy2, enemy3, enemy4])
                return 'cast', casting



        elif player_turn == 3:
            print('You are blocking.')
            return 'block', 0, ''




from npc_stats import *


def fight(enemy1, enemy2 = '', enemy3 = '', enemy4 = ''):
    global player_health
    global current_player_health
    global player_exp
    no_of_turns = 0
    exp = 0

    rolling('for Initiative')
    player_initiative = d20() + player_mods['dex mod'] + initiative_bonus
    initiative = {
        player_initiative: 0
    }
    print(f'\nYou rolled a {player_initiative} for initiative.')

    enemy2_is_alive = False
    enemy3_is_alive = False
    enemy4_is_alive = False
    enemy1_blocking = 1
    enemy2_blocking = 1
    enemy3_blocking = 1
    enemy4_blocking = 1

    enemy1_is_alive = True
    initiative[d20() + enemy1['dex mod']] = enemy1['name']+'1'
    enemy1_health = enemy1['health']

    if enemy2 != '':
        enemy2_is_alive = True
        initiative[d20() + enemy2['dex mod']] = enemy2['name']+'2'
        enemy2_health = enemy2['health']

    if enemy3 != '':
        enemy3_is_alive = True
        initiative[d20() + enemy3['dex mod']] = enemy3['name']+'3'
        enemy3_health = enemy3['health']

    if enemy4 != '':
        enemy4_is_alive = True
        initiative[d20() + enemy4['dex mod']] = enemy4['name']+'4'
        enemy4_health = enemy4['health']

    list_initiative = list(initiative.keys())
    list_initiative.sort(reverse = True)
    initiative = {item: initiative[item] for item in list_initiative}
    list_initiative = list(initiative.values())

    print(f'''
    You Face:
{enemy1['name'], enemy1['title']}
{enemy2['name'], enemy2['title']}
{enemy3['name'], enemy3['title']}
{enemy4['name'], enemy4['title']}''')
    
    initiative_string = [str(item) for item in list_initiative]

    print('Initiative Order:')
    print(', '.join(initiative_string))
    cont()

    while no_of_enemy > 0 and current_player_health > 0:
        if player_health <= 0:
            break
        blocking = 1

        for turn in list_initiative:
            no_of_turns += 1
            if current_player_health <= 0:
                break

            if turn == 0:

                player = player_turn(no_of_enemy, enemy1, enemy2, enemy3, enemy4)

                if player[0] == 'block':
                    blocking = 0.25
                elif player[0] == 'attack':
                    blocking = 1
                    if player[2] == enemy1['name']:
                        enemy1_health -= player[1] * enemy1_blocking
                    elif player[2] == enemy2['name']:
                        enemy2_health -= player[1] * enemy2_blocking
                    elif player[2] == enemy3['name']:
                        enemy3_health -= player[1] * enemy3_blocking
                    elif player[2] == enemy4['name']:
                        enemy4_health -= player[1] * enemy4_blocking

                elif player[0] == 'cast':

                    # I have it in a for loop so it can hit a single target multiple times
                    for target in player[1].keys(): 
                        if target == 0:
                            damage = player[1][0]()
                            current_player_health -= player[1][1]()
                            if damage < 0:
                                print(f'You gained {Fore.GREEN}{damage * -1}{Fore.RESET} health.')
                            else:
                                print(f'You took {damage} damage.')

                            if current_player_health > player_health:
                                current_player_health = player_health

                        if target == 1 and enemy1_is_alive:
                            spell_damage = player[1][1]()
                            enemy1_health -= spell_damage * enemy1_blocking
                            print(f'{enemy1["name"]} took {damage} damage.')

                        if target == 2 and enemy2_is_alive:
                            spell_damage = player[1][1]()
                            enemy2_health -= spell_damage * enemy2_blocking
                            print(f'{enemy2["name"]} took {spell_damage} damage.')

                        if target == 3 and enemy3_is_alive:
                            spell_damage = player[1][1]()
                            enemy3_health -= spell_damage * enemy3_blocking
                            print(f'{enemy3["name"]} took {spell_damage} damage.')

                        if target == 4 and enemy4_is_alive:
                            spell_damage = player[1][1]()
                            enemy4_health -= spell_damage * enemy4_blocking
                            print(f'{enemy4["name"]} took {spell_damage} damage.')


                if enemy1_health <= 0 and enemy1_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy1["name"]}{Fore.RESET}')
                    enemy1_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy1['exp']
                    print('+', enemy1['exp'], 'exp')
                    item_pickup(common_table(2))
                    cont()

                if enemy2_health <= 0 and enemy2_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy2["name"]}{Fore.RESET}')
                    enemy2_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy2['exp']
                    print('+', enemy2['exp'], 'exp')
                    item_pickup(common_table(2))
                    cont()

                if enemy3_health <= 0 and enemy3_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy3["name"]}{Fore.RESET}')
                    enemy3_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy3['exp']
                    print('+', enemy3['exp'], 'exp')
                    item_pickup(common_table(2))
                    cont()

                if enemy4_health <= 0 and enemy4_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy4["name"]}{Fore.RESET}')
                    enemy4_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy4['exp']
                    print('+', enemy4['exp'], 'exp')
                    item_pickup(common_table(2))
                    cont()


            elif str(turn).endswith('1') and enemy1_is_alive:
                enemy1_blocking = npc_turn(enemy1, enemy1_health, blocking)

            elif str(turn).endswith('2') and enemy2_is_alive:
                enemy2_blocking = npc_turn(enemy2, enemy2_health, blocking)

            elif str(turn).endswith('3') and enemy3_is_alive:
                enemy3_blocking = npc_turn(enemy3, enemy3_health, blocking)

            elif str(turn).endswith('4') and enemy4_is_alive:
                enemy4_blocking = npc_turn(enemy4, enemy4_health, blocking)

    if current_player_health <= 0:
        global player_is_alive
        print(Fore.RED + 'You Died.' + Fore.RESET)
        player_is_alive = False
        return False
    elif no_of_enemy == 0:
        print(Fore.GREEN + 'You Won!' + Fore.RESET)
        print(f'You gained {exp} exp')
        player_exp += exp
        return True

karma = 1

luck_bonus = 0

dun_level = 1
difficulty = 1 + dun_level / 5

luck = lambda: (karma - 1) * 8 + 10 + luck_bonus
luck_mod = lambda: int((luck() - 10) / 2)

WIDTH = 5
HEIGHT = 5
dun_level = 1


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
    wis_save = skill_save(player_mods['wis mod'], 10 + int(difficulty / 2))

    if column == 'dart':
        if wis_save == True:

            print()
            print('You spot small holes in the walls.')
            print('You know from experience that this is a dart trap.')
            print('Unfortunately the door to the previous room has closed.')
            print('The only way forward is to defuse it.\n')
            cont()

            rolling('Intelegence Save')
            int_save = skill_save(player_mods['int mod'], 10 + int(difficulty / 3))

            if int_save == True:
                print('You manage to defuse the trap, letting you move forward.')
                cont()
                return

        if wis_save == False or int_save == False:
            print('The dart trap inside of the room goes off!')
            rolling('Dexterity Save')
            dex_save = skill_save(player_mods['dex mod'], 10 + int(difficulty / 2))
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
            str_save = skill_save(player_mods['str mod'], 10 + int(difficulty / 2))

            if str_save == True:
                print('You just barely manage to jump over the gap.')
                cont()
                return
        elif str_save == False or wis_save == False:
            print('You fall into a spike trap!')
            rolling('Dexterity Save')
            dex_save = skill_save(player_mods['dex mod'], 10 + int(difficulty / 2))
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
                    column[3] = False

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



def movement_menu(dungeon):

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
            rest()
            rested = True
            return dungeon
        
        elif direction == 5:
            rest_without_the_rest()
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


goblin = {
    'name': 'Goblin', 'title': '', 'caster': False,
    'health': (lambda: int(d6(1) + 6 * difficulty)), 'weapon': 'dagger', 'ac': 5,
    'exp': int(50 * difficulty), 'agression': 5,
    'str mod': -1, 'dex mod': 2, 'end mod': 0, 'int mod': 0, 'wis mod': -1, 'cha mod': -1,
    'casting mod': 0
}

kobold = {
    'name': 'Kobold', 'title': '', 'caster': False,
    'health': (lambda: int((d4(4) - 2) * difficulty)), 'weapon': 'dagger', 'ac': 7,
    'exp': int(25 * difficulty), 'agression': 4,
    'str mod': -2, 'dex mod': 2, 'con mod': -1, 'int mod': -1, 'wis mod': -2, 'cha mod': -1,
    'casting mod': 0
}

slime = {
    'name': 'Slime', 'title': '', 'caster': False,
    'health': (lambda: int(d4(2) * difficulty)), 'weapon': 'dagger', 'ac': 6,
    'exp': int(26 * difficulty), 'agression': 20,
    'str mod': -4, 'dex mod': -3, 'con mod': 5, 'int mod': -5, 'wis mod': -5, 'cha mod': 1,
    'casting mod': 0
}

la_creatura = {
    'name': 'La Creatura', 
}


# Named

lily = {
    'name': 'Lily', 'title': '', 'caster': True,
    'health': d6(3) + 10, 'weapon': 'staff', 'ac': 8, 'exp': 250, 'agression': 0,
    'str mod': 0, 'dex mod': 1, 'end mod': 1, 'int mod': 3, 'wis mod': 2, 'cha mod': 1,
    'casting mod': 3,
    'spells': 'firebolt'
}

kile = {
    'name': 'Kile', 'title': ', With An I', 'caster': False,
    'health': d4(4) + 20, 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1,
    'casting mod': 0
}

kyle = {
    'name': 'Kyle', 'title': ', With A Y',
    'health': d4(4) + 20, 'weapon': 'longsword', 'ac': 12, 'exp': 225, 'agression': 2,
    'str mod': 2, 'dex mod': 1, 'end mod': 2, 'int mod': 0, 'wis mod': 0, 'cha mod': 1,
    'casting mod': 0
}

gronk = {
    'name': 'Gronk', 'title': ', The Killer', 'caster': False,
    'health': d6(4) + 20, 'weapon': 'maul', 'ac': 13, 'exp': 200, 'agression': 3,
    'str mod': 4, 'dex mod': -1, 'end mod': 3, 'int mod': -2, 'wis mod': -1, 'cha mod': 0,
    'casting mod': 0
}

siffrin_traveler = {
    'name': 'Siffrin', 'title': ', The Traveler', 'caster': False,
    'health': 50, 'weapon': 'dagger', 'ac': 13, 'exp': 500, 'agression': 6,
    'str mod': 0, 'dex mod': 5, 'end mod': 2, 'int mod': 1, 'wis mod': -1, 'cha mod': 2,
    'casting mod': 0
}

siffrin_lost = {
    'name': 'Siffrin', 'title': ', The Lost', 'caster': False,
    'health': 999, 'weapon': 'sif dagger', 'ac': 15, 'exp': 9999, 'agression': 10,
    'str mod': 0, 'dex mod': 6, 'end mod': 3, 'int mod': 0, 'wis mod': -2, 'cha mod': 1,
    'casting mod': 0
}

dangolf = {
    'name': 'Dangolf', 'title': ', The Gold',
    'health': 150, 'weapon': 'dangolf staff', 'ac': 10, 'exp': 1000, 'agression': 2,
    'str mod': -2, 'dex mod': -2, 'end mod': 2, 'int mod': 5, 'wis mod': 10, 'cha mod': 2,
    'casting mod': 0
}

godwin = {
    'name': 'Godwin', 'title': ', The Golden',
    'health': 30, 'weapon': 'golden spirit', 'ac': 12, 'exp': 2000, 'agression': -3,
    'str mod': 5, 'dex mod': 2, 'end mod': 4, 'int mod': 1, 'wis mod': 2, 'cha mod': 10,
    'casting mod': 0
}



# loot tables

def item_pickup(items):
    global player_equipment
    for item, numbers in items:
        player_equipment[item] += numbers
        print(f'You picked up {numbers} {item}')


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
            numbers.append(randint(1, 5))
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
    return zip(drops, numbers), # unique_items