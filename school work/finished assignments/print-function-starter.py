# Student name
# Current date
# f-String Adventure Story


bold = '\033[1m'
end = '\033[0m'

print('What is the hero\'s name?')

hero_name = input()

print('What is the story?')

story = input()

print('What do they find?')

item = input()

print('So to summerize: ' + bold + hero_name + end + ' is the name of the hero. ' + bold + story + end +  ' is the story during which they find ' + bold + item + end)