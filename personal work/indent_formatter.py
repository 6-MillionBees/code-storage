# Arden Boettcher
# 12/20/24
# Indent Formatter


def indent_formatter(file_start, file_start_name):
  file_end = open(file_start_name[0: file_start_name.index('.')] + '_indent_formatted' + file_start_name[file_start_name.index('.'): ], 'w')

  while True: # This while loop continues until it gets a valid input (an integer)
    try:
      starting_whitespace = int(input('How many starting whitespace characters? (-1 to exit)\n'))
      print()
      final_whitespace = int(input('How many desired whitespace characters? (-1 to exit)\n'))
      print()
    except ValueError:
      print('Invalid Input: please enter a number')
    else:
      break

  if starting_whitespace == -1 or final_whitespace == -1:
    quit()


  file_start_read = file_start.read()
  current_index = -1
  cooldown = 0

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

  print('Your file has been completed. Thank you for using Bee\'s formatter!')


def quotation_formatter(file_start, file_start_name):

  file_end = open(file_start_name[0: file_start_name.index('.')] + '_quotation_formatted' + file_start_name[file_start_name.index('.'): ], 'w')

  file_start_read = file_start.read()
  for letter in file_start_read:
    if letter == "'":
      file_end.write('"')
    elif letter == '"':
      file_end.write("'")
    else:
      file_end.write(letter)

def main():

  while True:

    file_start_name = input('Please enter file name (0 to quit):\n')

    if file_start_name == '0':
      print('\nOkie doki bye bye now!\n')
      quit()

    try:
      file_start = open(file_start_name, "r")
    except FileNotFoundError:
      print('\nFile Not Found: please make sure it is the exact file name.')
      print('Remember to include the file format (eg. .txt or .json)\n')
    else:
      break

  while True:
    print('''Please choose a formatter
    1.) Indent Formatter
    2.) Quotation Formatter''')
    try:
      formatter = int(input())
      if formatter not in range(1, 3):
        raise ValueError
    except ValueError:
      print('Invalid Input: please enter a number')
    else:
      break


  if formatter == 1:
    indent_formatter(file_start, file_start_name)

  elif formatter == 2:
    quotation_formatter(file_start, file_start_name)





if __name__ == '__main__':
  main()