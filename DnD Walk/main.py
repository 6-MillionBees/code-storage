# Arden Boettcher
# 1/22/25
# Dnd Main

import random
from time import sleep
from colorama import Fore


def d100(num = 1):
  roll = 0
  for x in range(num):
    num += 1
    roll += random.randint(1, 100)
  return roll

def d20(num = 1):
  roll = 0
  for x in range(num):
    num += 1
    roll += random.randint(1, 20)
  return roll

def d12(num = 1):
  roll = 0
  for x in range(num):
    num += 1
    roll += random.randint(1, 12)
  return roll

def d10(num = 1):
  roll = 0
  for x in range(num):
    num += 1
    roll += random.randint(1, 10)
  return roll

def d8(num = 1):
  roll = 0
  for x in range(num):
    num += 1
    roll += random.randint(1, 8)
  return roll

def d6(num = 1):
  roll = 0
  for x in range(num):
    num += 1
    roll += random.randint(1, 6)
  return roll

def d4(num = 1):
  roll = 0
  for x in range(num):
    num += 1
    roll += random.randint(1, 4)
  return roll

def get_int(text):
  while True:
    try:
      num = int(input(text))
    except ValueError:
      continue
    else:
      break

  return num



class player:
  def __init__(self) -> None:
    self.level = 3
    self.rested = False
    self.damage_increase = 0
    self.needed_exp = 100
    self.exp = 0
    self.ac = 0
    self.max_spell_slots = {0: -1, 1: 3, 2: 99}
    self.spell_slots = {0: -1, 1: 3, 2: 99}
    self.max_health = 0
    self.current_health = 0
    self.stats = {
      "str": 0,
      "dex": 0,
      "con": 0,
      "int": 0,
      "wis": 0,
      "cha": 0
    }
    self.mods = {
      "str": 0,
      "dex": 0,
      "con": 0,
      "int": 0,
      "wis": 0,
      "cha": 0
    }
    self.equipment = {
      "equipped right": "", "equipped left": "",
      "stored weapons": [],
      "equipped armor": "",
      "copper": 0, "silver": 0, "gold": 0,
      "arrows": 0, "rope": 0, "health potions": 0,
      "keys": 0
    }
    self.spells = {
      0: [],
      1: [],
      2: [],
      3: [],
      4: [],
      5: [],
      6: [],
      7: [],
      8: [],
      9: []
    }

  def define_stats(self):
    stats_selected = False

    while not stats_selected:









def main():
  pass





if __name__ == "__main__":
  main()