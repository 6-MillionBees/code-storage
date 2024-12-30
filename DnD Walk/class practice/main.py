# Arden Boettcher
# 11/26/24
# DnD walk demo (for class)


# Getting this out of the way from the start:
# This is a demo for a project I've been working on for 2, almost 3, months
# Most of this code is copied from the main thing and was probably written a month ago
# Though a bunch of the important stuff is quite recent

# For example these are some recent things:
# Everything to do with spells
# Map navigation & generation
# The entire gameplay loop
# The Class "player"
# A lot

# You might notice that there are multiple files
# This was a decision I made and I regret it at all times
# It might've been a little worth it solely for the learning experience
# Programming :D

if __name__ == "__main__":
    from colorama import Fore
    import default_functions as d

    def show_scores():
        try:
            scores = open('scores.txt', 'r')
        except:
            return

        scores_list = [int(i) for i in scores.readlines()]
        scores_list.sort(reverse= False)
        for score in scores_list:
            print(score)

        d.cont()


    show_scores()

    name = input(Fore.GREEN +'\nWhat is your name?\n' + Fore.RESET)
    name_title = name.title()

    print()
    print(Fore.GREEN + 'Welcome ' + name_title + '! To my RPG demo!')
    print('I\'d say it\'s pretty good (I am very biased)' + Fore.RESET)
    print()

    d.cont()

    print('To start we\'re going to assign your stats (this is permenent)')

    from player_stats import player

    user = player(3)
    user.equipment['equipped weapon'] = 'handaxe'
    user.define_stats()

    print('Total Health: ', user.health)
    print('Current Health: ', user.current_health)
    d.cont()




    import world as w


    dungeon = w.make_dungeon()
    print(f'you are here > {Fore.GREEN}+{Fore.RESET}')

    while user.isalive():

        w.print_dungeon(dungeon)
        movement = w.movement_menu(dungeon)
        if movement[0] == True:
            dungeon = movement[1]
        elif movement[0] == False:
            user.rest(movement[1])

        print()
        effects = w.dungeon_effects(dungeon, user)
        d.cont()

        if effects[0] == None:
            pass
        elif effects[0] == 'trap':
            user.current_health -= effects[1]

        elif effects[0] == 'encounter':
            if effects[1] == False:
                print('Game over :(')
                break
            else:
                user.current_exp += effects[1]
                user.current_health = effects[2]

        elif effects[0] == 'chest':
            if effects[1][0] == 'basic':
                print(f'You obtained {effects[1][2]} {effects[1][1]}')
                user.equipment[effects[1][1]] += effects[1][2]
            elif effects[1][0] == 'weapon':
                user.pickupweapon(effects[1][1])

        elif effects[0] == 'exit':
            if effects[1]:
                dungeon = w.make_dungeon()
                rested = False


        print(user.current_exp, user.needed_exp)
        print(user.current_exp >= user.needed_exp)

        if user.current_exp >= user.needed_exp:
            user.level_up()


    user.count_coints()

    score = w.dun_level * 1000 + round(user.equipment['copper pieces'] * 0.1) + user.equipment['silver pieces'] * 10 + user.equipment['gold pieces'] * 1000

    print(f'''Score:
    Dungeon Floors ({w.dun_level}): {w.dun_level * 1000}
    Coins (c:{user.equipment['copper pieces']}, s:{user.equipment['silver pieces']}, g: {user.equipment['gold pieces']}): {user.equipment['copper pieces'] + user.equipment['silver pieces'] * 100 + user.equipment['gold pieces'] * 1000}ftgyhujikolp

    difficulty({w.difficulty}): {w.difficulty * 1000}

    Total: {score}''')

    print()

    save_score = open('dnd_score.txt', 'a')
    save_score.write(str(score) + '\n')