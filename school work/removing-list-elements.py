# Arden Boettcher
# 10/30/24
# Removing List Elements

# Favorites

favorites = ['team fortress 2', 'terraria', 'github', 'will wood', 'finland', 'bbq chicken']

print(favorites)

# The pop() method

favorites.pop() # Removes bbq
print(favorites)

favorites.pop(3) # Removes will wood
print(favorites)

# The remove() method

favorites.remove('github') # Removes github
print(favorites)

# Keyword del

del favorites[2] # Removes finland
print(favorites)




# Part 2

# Guest list

guest_list = ['Abraham Lincoln', 'Leonardo Da Vinci', 'Pluto', 'Jesus Christ', 'Tony Hawk', 'Gautama Buddha']
# I don't want to eat dinner with anyone so I'm choosing random historical figures

print('Keeping the exsistance of God a mystery Jesus failed to arrive.')
guest_list.remove('Jesus Christ')

for guest in guest_list:
    print(f'''
Congratulations {guest}
    You\'ve been invited to the inter-time
dinner party. Please power on your time machines
and join us for dinner''')