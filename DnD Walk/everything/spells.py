# Arden Boettcher
# 11/20/24
# Spells

from starting_functions import invalid, cont, int_input
from dice import *
from npc_stats import *
from colorama import Fore

player_spells = { # WIP
    0: ['acid splash', 'fire bolt', 'light', 'poison spray'],
    1: ['burning hands', 'magic missile'],
    2: ['fireball'],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}

print_spell_level = {
    0: 'cantrips',
    1: 'level 1',
    2: 'level 2',
    3: 'level 3',
    4: 'level 4',
    5: 'level 5',
    6: 'level 6',
    7: 'level 7',
    8: 'level 8',
    9: 'level 9',
}

c_player_spell_slots = { # WIP
    0: -1,
    1: 3,
    2: 1,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

m_player_spell_slots = { # WIP
    0: -1,
    1: 3,
    2: 1,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0
}

spell_descriptions = {
    'acid splash': f'''{Fore.GREEN}    cantrip, single, 1d6{Fore.RESET}
details: You swing a bubble of acid towards an enemy
dealing 1d6 damage''',

    'fire bolt': f'''{Fore.GREEN}    cantrip, single, 1d10{Fore.RESET}
details: You throw a small ball of fire towards one
unlucky enemy damaging it for 1d10 fire damage.''',

    'light': f'''{Fore.GREEN}    cantrip, non-combat
details: You hover a glowing ball of light over your
palm, letting you see in the dark.''',

    'poison spray': f'''{Fore.GREEN}    cantrip, single, 1d12 {Fore.RESET}
details: You sent a puff of noxious gas towards one
enemy, they take 1d12 damage on a failed constitution
save and half that on a success.''',

    'burning hands': f'''{Fore.GREEN}    level 1, AOE, 3d6 {Fore.RESET}
details: You spread your fingers sending out a wave 
of flame hitting 3 adjacent enemies for 3d6.''',

    'magic missile': f'''{Fore.GREEN}    level 1, multi-hit, 1d4 + 1 {Fore.RESET}
details: You fire three homing bolts of glowing blue
magic dealing 1d4 + 1 to three enemies of your choice.''',

    'fireball': f'''{Fore.GREEN}    level 2, AOE, 8d6 {Fore.GREEN}
details : You throw a hurtling ball of fire that
explodes on contact dealing 8d6 to all enemies.'''

}


# This is so complicated because of customizability
# It works regardless of any other variable
# you could have hundreds of spells and it'd still keep on chuggin
def spells_menu():

    while True:
        print('Spells:')

        num = 0
        for spell_level in player_spells.keys():
            if player_spells[spell_level] == []:
                continue
            print(f'    {num}.) {print_spell_level[num]}: {", ".join(player_spells[spell_level])}')
            num += 1

        spell_level = int_input('Choose a spell level (-1 to go back): ')
        print()

        if spell_level == -1:
            return False
        elif spell_level in range(0, num):

            if spell_level != 0:
                print(f'You have {c_player_spell_slots[spell_level]} {print_spell_level[spell_level]} spell slots')
            print('Which spell?: ')

            num = 0
            for spell in player_spells[spell_level]:
                num += 1
                print('    {0}.) '.format(num) + spell)
            spell_choice = int_input('Which spell (-1 to go back): ')

            if spell_choice == -1:
                continue
            elif spell_choice in range(1, num + 1):
                print(f'You cast {player_spells[spell_level][spell_choice - 1].title()}')
                return player_spells[spell_level][spell_choice - 1]
            else:
                invalid()
                continue

        else:
            invalid()
            continue


def cast(spell, casting_mod): # WIP
    if spell == 'acid splash':
        return cast_acid_splash()
    elif spell == 'fire bolt':
        return cast_fire_bolt()
    elif spell == 'fireball':
        return cast_fireball()


def cast_acid_splash(enemies):
    print('You cast Acid Splash')
    while True:
        for enemy in enemies:
            print(f'{enemies.index(enemy) + 1}.) {enemy['name']}')
        
        choice = int_input('Which enemy do you attack?: ')
        if choice in range(1, len(enemies) + 1):
            break
        else:
            invalid()
            continue
    return choice, lambda: d6()


def cast_fire_bolt(enemies):
    print('wip')

# def cast_light():

def cast_fireball():
    print('You cast Fireball.')
    cont()
    return [1, 2, 3, 4], lambda: d6(8)

enemies = [goblin, kobold, goblin, goblin]

print(cast(spells_menu(), 0, enemies))





























bard_spells = {
    'cantrips': [
        'blade ward', 'dancing lights', 'friends', 'light', 'mage hand',
        'mending', 'minor illision', 'prestidigitation', 'true strike',
        'vicious mockery'
    ],

    'level 1': [
        'animal Friendship', 'bane', 'charm person', 'comprehend languages',
        'cure wounds', 'detect magic', 'disguise self', 'dissonant whispers',
        'faerie fire', 'feather fall', 'healing word', 'herosim', 'identify','longstrider', 'speak with animals', 'thunderwave',
    ],

    'level 2': [
        'animal messenger', 'blindness deafness', 'calm emotions', 
        'cloud of daggers', 'crown of madness', 'detect thoughts',
        'enhance ability', 'enthrall', 'heat metal', 'hold person',
        'invisibility', 'knock', 'lesser resotration',
        'locate animals or plants', 'locate object', 'magic mouth',
        'phantasmal force', 'see invisibility', 'shatter', 'silence',
        'suggestion', 'zone of truth'
    ],

    'level 3': [
        'bestow curse', 'clairvoyance', 'dispell magic', 'fear',
        'feign death', 'glyph of warding', 'hypnotic pattern',
        'leomunds tiny hut', 'major image', 'nondetection', 
        'plant growth', 'sending', 'speak with dead', 'speak with plants',
        'stinking cloud', 'toungues'
    ],

    'level 4': [
        'compulsion', 'confusion', 'dimension door', 'freedom of movement',
        'greater invisibility', 'hallucinatory terrain', 'locate creature',
        'polymorph'
    ],

    'level 5': [
        'animate objects', 'awaken', 'dominate person', 'dream', 'geas',
        'greater restoration', 'hold monster', 'legend lore', 
        'mass cure wounds', 'mislead', 'modify memory', 'planar binding',
        'raise dead', 'scrying', 'seeming', 'teleportation circle'
    ],

    'level 6': [
        'eyebite', 'find the path', 'guards and wards', ''
    ]
}

# Every Single Dnd Spell (and whether it's going to be in the game)

dnd_spells = {
    'acid splash':          True,
    'aid':                  True,
    'alarm':                False,
    'alter self':           [True, 'changed'],
    'animal friendship':    True,
    'animal messenger':     False,
    'animal shapes':        False,
    'animate dead':         True,
    'animate objects':      True,
    'antlife shell':        True,
    'antimagic field':      True,
    'antipathy/sympathy':   False,
    'arcane eye':           False,
    'arcane gate':          False,
    'arcane lock':          True,
    'armor of agathys':     True,
    'arms of hadar':        True,
    'astral projection':    False,
    'aura of life':         True,
    'aura of purity':       True,
    'aura of vitality':     True,
    'awaken':               False,
    'bane':                 False,
    'banishing smite':      [True, 'changed'],
    'banishment':           True,
    'barkskin':             [True, 'changed'],
    'beacon of hope':       False,
    'beast sense':          False,
    'bestow curse':         True,
    'bigbys hand':          [True, 'changed'],
    'blade barrier':        False,
    'blade ward':           True,
    'bless':                True,
    'blight':               True,
    'blinding smite':       True,
    'blindness/deafness':   True,
    'blink':                False,
    'blur':                 True,
    'branding smite':       False,
    'burning hands':        True,
    'call lightning':       True,
    'calm emotions':        False,
    'chain lightning':      True,
    'charm person':         False,
    'chill touch':          True,
    'chromatic orb':        True,
    'circle of death':      True,
    'cicle of power':       False,

    # Now I'm doing JUST the ones I think would be cool
    'cloud of daggers':     True,

}