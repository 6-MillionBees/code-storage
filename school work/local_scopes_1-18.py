# Arden Boettcher
# 1/14/25
# Local Scope Challenges

def greet(fname:str):
  greeting = f"Welcome {fname.title()}!"
  return greeting # greeting has local scope due to it being inside a function

print(greet("Bruce"))

def count_vowels(words:str):
  vowel_count = 0
  for letter in words.lower():
    if letter in "aeiou":
      vowel_count += 1
  return vowel_count

print(count_vowels("abcdefghijklmnopqrstuvwxyz"))