# Arden Boettcher
# 1/14/25
# *args


def calc_sum(*args:int):
  return sum(args)

print(calc_sum(4, 9, 16, 5, 19))


def format_message(*args:str):
  return " ".join(args)

print(format_message("Words Words Words", "Split a whole into thirds", "thirds thirds"))


def average_of_numbers(*args:int):
  return sum(args) / len(args)

print(average_of_numbers(4, 9, 16, 5, 19))