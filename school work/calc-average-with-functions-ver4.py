# Arden Boettcher
# 1/14/25
# Debug


# Calculate the average of two quiz scores
# Version 3.0

# How could we shorten/simplify this script?
# I didn't really shorten it and I might've made it more complicated
# but it works a lot better and won't break if the user messes up

# Identify and correct the error that pops up when you run this script
# You get a TypeError because it was concatenating float to str (which you shouldn't)

def get_float(text:str):
  while True:
    try:
      output = float(input(text))
    except ValueError:
      continue
    else:
      break
  return output

def get_int(text:str):
  while True:
    try:
      output = int(input(text))
    except ValueError:
      continue
    else:
      break
  return output


def get_quiz_scores():
  scores = []
  num_of_scores = get_int("How many quizes?: ")
  for x in range(num_of_scores):
    scores.append(get_float(f"Enter score for Quiz {x + 1}: "))
  if scores:
    return scores


def calculate_average(scores:list):
  try: # In case items in the list aren't integers
    average = sum(scores)/len(scores) # Calculates the average
  except (ValueError, TypeError):
    print("Error: Invalid input.\nPlease check your previous input(s).")
  else:
    return average


# Function calls
scores = get_quiz_scores()

my_average = calculate_average(scores) # Step 3: Calculate average

print("Your average score:", my_average) # Step 4: Print the average quiz score