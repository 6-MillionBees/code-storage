# Arden Boettcher
# 1/10/25
# Passing Values

def square_number(number):
  print(f"{number} squared equals {number**2}")
  return number ** 2

def add_squares(num1, num2):
  result = num1 + num2
  print(f"The sum of {num1} and {num2} is {result}")
  return result

def get_int(words): # This is very similar to the c function with the same name.
  while True:
    try:
      result = int(input(words))
    except ValueError:
      continue
    else:
      break
  return result

def main():
  num1 = get_int("Please enter a number: ")
  num1_squared = square_number(num1)

  num2 = get_int("\nPlease enter another number: ")
  num2_squared = square_number(num2)

  add_squares(num1_squared, num2_squared)


if __name__ == "__main__":
  main()