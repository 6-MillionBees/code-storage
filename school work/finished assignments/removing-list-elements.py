# Arden Boettcher
# 10/30/24
# Removing List Elements

import time

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

print()
print()



# Part 2

# Guest list

guest_list = ['Abraham (The Prophet)', 'Leonardo Da Vinci', 'Laozi', 'Jesus Christ', 'Tony Hawk', 'Gautama Buddha']
# I don't want to eat dinner with anyone in particular so I'm choosing historical figures that would be the best to bring into our time
# I get that tony hawk is still alive but It'd be so funny
# A lot of these are founders of religions


print('Unfortunately Gautama Buddha is busy meditating for a few decades.')
guest_list.remove('Gautama Buddha')
input('Press enter to continue:\n')

for guest in guest_list:
    print(f'''
Congratulations {guest}!
    You\'ve been officially invited to the
inter-time dinner party. Please power on your
time machines and join us for dinner.

ps. You can sleep in you\'ll always be on time
''')
    time.sleep(1)

print('Oh my! It appears my fancy dinner table was lost in transit! :(')
print('I unfortunately can only seat 2 guests\n')

for x in range(3):
    guest_list.pop(0)

for guest in guest_list:
    print(f'Thankfully you are still invited, {guest}.')

del guest_list[:]

print(guest_list)