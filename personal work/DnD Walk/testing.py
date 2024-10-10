# Arden boettcher
# 10/10/24
# dnd walk testing
'''
weapon_damage = {
    'club': d4(), 'dagger': d4(), 'great club': d10(), 'javelin': d6(), 'light hammer': d4(),
    'mace': d6(), 'quarterstaff': d8(), 'sickle': d4(), 'spear': d6(), 'battle axe': d8(),
    'flail': d8(), 'glaive': d10(), 'greataxe': d12(), 'greatsword': d6(2), 'halberd': d10(),
    'handaxe': d6(), 'lance': d8(), 'longsword': d8(), 'maul': d6(2), 'morningstar': d8(),
    'pike': d10(), 'rapier': d8(), 'scimitar': d6(), 'shortsword': d6(), 'trident': d8(),
    'war pick': d8(), 'warhammer': d8(), 'whip': d4()
}

weapon_mod = {
    'club mod': str_mod, 'dagger': str_mod, 'great club': str_mod, 'javelin': str_mod, 'light hammer': str_mod,
    'mace': str_mod, 'quarterstaff': str_mod, 'sickle': str_mod, 'spear': str_mod, 'battle axe': str_mod,
    'flail': str_mod, 'glaive': str_mod, 'greataxe': str_mod, 'greatsword': str_mod, 'halberd': str_mod,
    'handaxe': str_mod, 'lance': str_mod, 'longsword': str_mod, 'maul': str_mod, 'morningstar': str_mod,
    'pike': str_mod, 'rapier': str_mod, 'scimitar': str_mod, 'shortsword': str_mod, 'trident': str_mod,
    'war pick': str_mod, 'warhammer': str_mod, 'whip': str_mod
}

def attack(modifier, weapon, ac):
    roll = d20() + modifier 
    if ac > roll:
        print('Your attack did not hit')
        return 0
    if ac <= roll:
        print('')
        return weapon_damage[weapon] + weapon_mod[weapon]
    
'''