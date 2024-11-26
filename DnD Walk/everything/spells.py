# Arden Boettcher
# 11/20/24
# Spells


player_spells = {}

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