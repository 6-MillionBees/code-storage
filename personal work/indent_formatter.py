# Arden Boettcher
# 12/20/24
# Indent Formatter


while True:

  file_start_name = input('Please enter file name (0 to quit):\n')

  if file_start_name == '0':
    print('\nOkie doki bye bye now!\n')
    quit()

  try:
    file_start = open(file_start_name, "r")
  except FileNotFoundError:
    print('\nFile Not Found: please make sure it is the exact file name.')
    print('Make sure to include the file format (eg. .txt or .json)\n')
  else:
    break

while True:
  try:
    starting_whitespace = int(input('How many starting whitespace characters? (-1 to exit)\n'))
    print()
    final_whitespace = int(input('How many desired whitespace characters? (-1 to exit)\n'))
    print()
  except ValueError:
    print('Invalid Input: please enter a number')
  else:
    break



period_index = file_start_name.index('.')
file_end = open(file_start_name[0: period_index] + '_formatted' + file_start_name[period_index: ], 'w')

file_start_read = file_start.read()
current_index = -1
cooldown = 0
letter_cooldown = 0

for letter in file_start_read:
  current_index += 1

  if file_start_read[current_index: current_index + starting_whitespace] == ' ' * starting_whitespace:
    if cooldown <= 0:
      file_end.write(' ' * final_whitespace)
      cooldown = starting_whitespace - 1
    else:
      cooldown -= 1

  else:
    if cooldown <= 0:
      file_end.write(letter)
    cooldown -= 1