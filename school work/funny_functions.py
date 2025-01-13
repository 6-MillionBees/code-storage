# Arden Boettcher
# 1/8/25
# Simple Functions


def get_city():
  city = input("Please enter the name of the city you live in: ")
  return city

def get_age():
  age = input("Please enter your age: ")
  return age

def build_output(city, age):
  return f"You live in {city.title()} and you are {age} years old."


print(build_output(get_city(), get_age()))