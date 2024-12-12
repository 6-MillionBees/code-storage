from colorama import Fore
# from random import randint

from player_stats import * # IMPORT
from items import weapon_damage, weapon_mod


def roll_against(agressor_mod, agressor, defender, defender_mod):
    agressor_roll = d20() + agressor[agressor_mod]
    defender_roll = d20() + defender[defender_mod]
    if agressor_roll > defender_roll:
        return True
    elif agressor_roll < defender_roll:
        return False




def damage_over_time(target, duration, damage, damage_type = ''):
    print('dnd\'s mechanics are going to be my 13 reason.')
    # I'm not finishing some things because I don't need to ¯\_(ツ)_/¯



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




from spells import * # IMPORT

def npc_turn(enemy, current_health, blocking):
    global current_player_health
    print('It\'s ' + enemy['name'] + '\'s turn')
    cont()

    roll = d10() + enemy['agression']

    if roll > 6:
        print(enemy['name'] + ' is attacking.\n')

        damage = npc_attack(roll_to_hit(d20(), player_ac, enemy[weapon_mod[enemy['weapon']]]), enemy['weapon'], enemy)
        damage = round(damage * blocking)

        if damage > 50:
            print(f'You took {Fore.RED}{damage}{Fore.RESET} damage.')
        else:
            print(f'You took {damage} damage.')
            print()
        return 0, damage

    elif roll <= 6:
        print(enemy['name'] + ' is blocking.')
        cont()
        return 0.5, 0







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
                enemies = [enemy1, enemy2, enemy3, enemy4]
                for num in range(1, no_of_enemy + 1):
                    if enemies[num - 1] != '':
                        print(f'{num}.) {enemies[num - 1]["name"]}')
                choice = int_input('Which enemy?: ')
                print()



                if choice == 1:
                    damage =  attack(roll_to_hit(d20(), enemy1['ac'], player_mods[weapon_mod[player_equipment['equipped weapon']]]), player_equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy1["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy1["name"]} for {damage}')
                    return 'attack', damage, enemy1['name']

                elif choice == 2:
                    damage =  attack(roll_to_hit(d20(), enemy2['ac'], player_mods[weapon_mod[player_equipment['equipped weapon']]]), player_equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy2["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy2["name"]} for {damage}')
                    return 'attack', damage, enemy2['name']

                elif choice == 3:
                    damage =  attack(roll_to_hit(d20(), enemy3['ac'], player_mods[weapon_mod[player_equipment['equipped weapon']]]), player_equipment['equipped weapon'])
                    if damage > 50:
                        print(f'You attack {enemy3["name"]} for {Fore.RED}{damage}{Fore.RESET}')
                    else:
                        print(f'You attack {enemy3["name"]} for {damage}')
                    return 'attack', damage, enemy3['name']

                elif choice == 4:
                    damage =  attack(roll_to_hit(d20(), enemy4['ac'], player_mods[weapon_mod[player_equipment['equipped weapon']]]), player_equipment['equipped weapon'])
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

                enemies = []
                for enemy in [enemy1, enemy2, enemy3, enemy4]:
                    if enemy == "":
                        continue
                    elif enemy != "":
                        enemies.append(enemy)
                casting = cast(spell, enemies)
                return 'cast', casting



        elif player_turn == 3:
            print('You are blocking.')
            return 'block', 0, ''




from npc_stats import *

# If it ain't broke don't fix it
player_dict = {'initiative': 0, 'name': 'You'}

def fight(enemy1_og, enemy2_og = '', enemy3_og = '', enemy4_og = ''):
    global player_health
    global current_player_health
    global player_exp
    no_of_turns = 0
    exp = 0

    rolling('for Initiative')
    initiative = []

    enemy2_is_alive = False
    enemy3_is_alive = False
    enemy4_is_alive = False
    enemy1_blocking = 1
    enemy2_blocking = 1
    enemy3_blocking = 1
    enemy4_blocking = 1
    enemy2_health = 0
    enemy3_health = 0
    enemy4_health = 0


    enemy1 = dict(enemy1_og)
    enemy1['name'] = enemy1['name'] + ' 1'
    no_of_enemy = 1
    enemy1_is_alive = True
    enemy1_health = enemy1['health']()
    initiative.insert(randint(0, len(initiative)), enemy1)

    if enemy2_og != '':
        enemy2 = dict(enemy2_og)
        enemy2['name'] = enemy2['name'] + ' 2'
        enemy2_is_alive = True
        enemy2_health = enemy2['health']()
        no_of_enemy += 1
        initiative.insert(randint(0, len(initiative)), enemy2)


    if enemy3_og != '':
        enemy3 = dict(enemy3_og)
        enemy3['name'] = enemy3['name'] + ' 3'
        enemy3_is_alive = True
        enemy3_health = enemy3['health']()
        no_of_enemy += 1
        initiative.insert(randint(0, len(initiative)), enemy3)

    if enemy4_og != '':
        enemy4 = dict(enemy4_og)
        enemy4['name'] = enemy4['name'] + ' 4'
        enemy4_is_alive = True
        enemy4_health = enemy4['health']()
        no_of_enemy += 1
        initiative.insert(randint(0, len(initiative)), enemy4)

    initiative.insert(randint(0, len(initiative)), player_dict)

    print()
    print('Initiative Order:')
    initiative_print_num = 0
    for turn in initiative:
        if initiative_print_num == 0:
            print(turn['name'], end = '')
            initiative_print_num += 1
        else:
            print(f', {turn["name"]}', end = '')
    print()
    cont()

    while no_of_enemy > 0 and current_player_health > 0:
        if player_health <= 0:
            break
        blocking = 1

        for turn in initiative:
            no_of_turns += 1
            if current_player_health <= 0:
                break

            if turn == player_dict:

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
                            damage = player[1][1]()
                            current_player_health -= damage
                            if damage < 0:
                                print(f'You restored {Fore.GREEN}{damage}{Fore.RESET} health.')
                            else:
                                print(f'You took {damage} damage.')

                            if current_player_health > player_health:
                                current_player_health = player_health

                        if target == 1 and enemy1_is_alive:
                            spell_damage = player[1][target]
                            spell_damage = spell_damage * enemy1_blocking
                            enemy1_health -= spell_damage
                            print(f'{enemy1["name"]} took {spell_damage} damage.')

                        if target == 2 and enemy2_is_alive:
                            spell_damage = player[1][target]
                            spell_damage = spell_damage * enemy2_blocking
                            enemy2_health -= spell_damage
                            print(f'{enemy2["name"]} took {spell_damage} damage.')

                        if target == 3 and enemy3_is_alive:
                            spell_damage = player[1][target]
                            spell_damage = spell_damage * enemy3_blocking
                            enemy3_health -= spell_damage
                            print(f'{enemy3["name"]} took {spell_damage} damage.')

                        if target == 4 and enemy4_is_alive:
                            spell_damage = player[1][target]
                            spell_damage = spell_damage * enemy4_blocking
                            enemy4_health -= spell_damage
                            print(f'{enemy4["name"]} took {spell_damage} damage.')


                if enemy1_health <= 0 and enemy1_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy1["name"]}{Fore.RESET}')
                    enemy1_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy1['exp']
                    print('+', enemy1['exp'], 'exp')
                    item_pickup(common_table(2, enemy1))
                    cont()

                if enemy2_health <= 0 and enemy2_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy2["name"]}{Fore.RESET}')
                    enemy2_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy2['exp']
                    print('+', enemy2['exp'], 'exp')
                    item_pickup(common_table(2, enemy2))
                    cont()

                if enemy3_health <= 0 and enemy3_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy3["name"]}{Fore.RESET}')
                    enemy3_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy3['exp']
                    print('+', enemy3['exp'], 'exp')
                    item_pickup(common_table(2, enemy3))
                    cont()

                if enemy4_health <= 0 and enemy4_is_alive:
                    print(f'{Fore.LIGHTRED_EX}You killed {enemy4["name"]}{Fore.RESET}')
                    enemy4_is_alive = False
                    no_of_enemy -= 1
                    exp += enemy4['exp']
                    print('+', enemy4['exp'], 'exp')
                    item_pickup(common_table(2, enemy4))
                    cont()


            elif turn == enemy1 and enemy1_is_alive:
                enemy1_turn = npc_turn(enemy1, enemy1_health, blocking)
                enemy1_blocking = enemy1_turn[0]
                current_player_health -= enemy1_turn[1] * blocking

            elif turn == enemy2 and enemy2_is_alive:
                enemy2_turn = npc_turn(enemy2, enemy2_health, blocking)
                enemy2_blocking = enemy2_turn[0]
                current_player_health -= enemy2_turn[1] * blocking

            elif turn == enemy3 and enemy3_is_alive:
                enemy3_turn = npc_turn(enemy3, enemy3_health, blocking)
                enemy3_blocking = enemy3_turn[0]
                current_player_health -= enemy3_turn[1] * blocking

            elif turn == enemy4 and enemy4_is_alive:
                enemy4_turn = npc_turn(enemy4, enemy4_health, blocking)
                enemy4_blocking = enemy4_turn[0]
                current_player_health -= enemy4_turn[1] * blocking

    if current_player_health <= 0:
        global player_is_alive
        print(Fore.RED + 'You Died.' + Fore.RESET)
        player_is_alive = False
        return False

    elif no_of_enemy == 0:
        print(Fore.GREEN + 'You Won!' + Fore.RESET)
        print(f'You gained {exp} exp')
        player_exp += exp
        print(bar(player_exp, exp_needed, 15, 'exp'))
        return True