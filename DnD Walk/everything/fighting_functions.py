from colorama import Fore
# from random import randint

from dice import *
from npc_stats import *
from items import *
from starting_functions import cont, roll_to_hit, rolling, bar
from player_stats import *
from spells import *




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
            spell = spells_menu
            if spell == -1:
                continue
            else:
                enemies = [enemy1, enemy2, enemy3, enemy4]
                casting = cast(spell, player_mods['casting_mod'], enemies)
                return 'cast', casting



        elif player_turn == 3:
            print('You are blocking.')
            return 'block', 0, ''







def fight(no_of_enemy, enemy1, enemy2 = empty_npc, enemy3 = empty_npc, enemy4 = empty_npc):
    global player_health
    global current_player_health
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

    if enemy2 != empty_npc:
        enemy2_is_alive = True
        initiative[d20() + enemy2['dex mod']] = enemy2['name']+'2'
        enemy2_health = enemy2['health']

    if enemy3 != empty_npc:
        enemy3_is_alive = True
        initiative[d20() + enemy3['dex mod']] = enemy3['name']+'3'
        enemy3_health = enemy3['health']

    if enemy4 != empty_npc:
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
                continue

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
                    cast_targets = player[1][0]

                    for target in cast_targets:
                        if target == 0:
                            current_player_health -= player[1][1]()

                            if current_player_health > player_health:
                                current_player_health = player_health

                        if target == 1:
                            enemy1_health -= player[1][1]()
                        if target == 2:
                            enemy2_health -= player[1][1]()
                        if target == 3:
                            enemy3_health -= player[1][1]()
                        if target == 4:
                            enemy4_health -= player[1][1]()


                if enemy1_is_alive:
                    if enemy1_health <= 0 and enemy1_is_alive:
                        print(f'{Fore.LIGHTRED_EX}You killed {enemy1["name"]}{Fore.RESET}')
                        enemy1_is_alive = False
                        no_of_enemy -= 1
                        exp += enemy1['exp']
                        print('+', enemy1['exp'], 'exp')
                if enemy2_is_alive:
                    if enemy2_health <= 0:
                        print(f'{Fore.LIGHTRED_EX}You killed {enemy2["name"]}{Fore.RESET}')
                        enemy2_is_alive = False
                        no_of_enemy -= 1
                        exp += enemy2['exp']
                        print('+', enemy2['exp'], 'exp')
                if enemy3_is_alive:
                    if enemy3_health <= 0:
                        print(f'{Fore.LIGHTRED_EX}You killed {enemy3["name"]}{Fore.RESET}')
                        enemy3_is_alive = False
                        no_of_enemy -= 1
                        exp += enemy3['exp']
                        print('+', enemy3['exp'], 'exp')
                if enemy4_is_alive:
                    if enemy4_health <= 0:
                        print(f'{Fore.LIGHTRED_EX}You killed {enemy4["name"]}{Fore.RESET}')
                        enemy4_is_alive = False
                        no_of_enemy -= 1
                        exp += enemy4['exp']
                        print('+', enemy4['exp'], 'exp')
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
        print(Fore.RED + 'You Lost.' + Fore.RESET)
        return 0
    elif no_of_enemy == 0:
        print(Fore.GREEN + 'You won!' + Fore.RESET)
        print(f'You gained {exp} exp')
        return 1, exp