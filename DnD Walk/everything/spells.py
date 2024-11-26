# Arden Boettcher
# 11/20/24
# Spells

from starting_functions import invalid, cont

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

player_spell_slots = { # WIP
    '0': 'yes',
    '1': 3,
    '2': 1,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}


def spells_menu():
    num = 0
    player_spells

    while True:
        print('Spells:')
        for spell_level in player_spells.keys():
            if player_spells[spell_level] == []:
                continue
            print(f'    {num}.) {print_spell_level[num]}: {", ".join(player_spells[spell_level])}')
            num += 1

        while True:
            try:
                spell_level = int(input('Which spell level? (-1 to cancel): '))
            except ValueError:
                invalid()
                continue
            else:
                break

        if spell_level == -1:
            return False
        elif spell_level in range(0, num):

            if spell_level != 0:
                print(f'You have {player_spell_slots[str(spell_level)]} {print_spell_level[str(spell_level)]}')
            print('Which spell?: ')

            num = 0
            for spell in player_spells[spell_level]:
                num += 1
                print('    {0}.) '.format(num) + {spell})
        else:
            invalid()
            continue





def cast_acid_splash():
    print('wip')
def cast_fireball():
    print('wip')

spells_menu()





























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