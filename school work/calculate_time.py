# Issac, Elliot, Arden
# 1/6/24
# Pairs Activity 1 - Calculate time



def calculate_time(distance, speed):
  if distance < 0:
    return "Error: Invalid Distance"
  time = distance / speed
  if int(time) < time:
    time_float = time - int(time)
    minutes = int(60 * time_float)
    return f"At {speed} mph, it will take {int(time)} hour(s) and {minutes} minute(s) to drive {distance} miles."
  return f"At {speed} mph, it will take {int(time)} hour(s) to drive {distance} miles."

try:
  speed = int(input("Please enter speed (mph): "))
  distance = int(input("Please enter distance (miles): "))
except ValueError:
  print("Invalid input please try again.")
else:
  print(calculate_time(speed = speed, distance = distance))