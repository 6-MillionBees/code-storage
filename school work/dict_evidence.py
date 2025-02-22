# Arden Boettcher
# 2/3/25
# Dictionary Assessment

my_dict = {
  "Tyler The Creator": "St. Chroma",
  "LiteralHat": "Count To 10",
  "Black Country New Road": "The Boy",
  "Remi Wolf": "Pink and White",
  "picdo": "My bread was Burnt to a Crisp"
}

print(my_dict, "\n")

my_dict.update({"Tyler The Creator": "Balloon"})
my_dict["Remi Wolf"] = "Woo!"

for key in my_dict.keys():
  print(key)
print()

for value in my_dict.values():
  print(value)
print()

for item in my_dict.items():
  print(item)
print()