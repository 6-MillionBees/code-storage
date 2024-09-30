# Arden Boettcher
# 9/10
# f-String Adventure Story

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information:

     - the hero's first name
     - the setting of the story (e.g., forest, desert, cave system)
     - the object the hero finds while on his/her adventure

3. Assign each piece of information collected to a variable with a short, specific name.

4. Declare (create) a variable named `story` and assign to it the `f-string` that is your adventure story

5. Use the `print( )` function to display your adventure story on the screen.

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''

bold = '\033[1m' # this stuff is purely formatting
end = '\033[0m' # making the variables bold lets them be easier to diferentiate from the other text

print('What is the hero\'s name?')

hero_name = input()

print('What is the story?')

story = input()

print('What do they find?')

item = input()

print('So to summerize: ' + bold + hero_name.title + end + ' is the name of the hero. ' + bold + story + end +  ' is the story during which they find ' + bold + item + end)