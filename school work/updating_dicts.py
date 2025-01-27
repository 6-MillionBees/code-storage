# Arden Boettcher
# 1/27/24
# Updating / Removing Dictionary items


gleep_glorp = {
  "name": "Gleep Glorp",
  "age":  "That's a rude thing to ask",
  "home planet": "Florgon VI",
  "color": "bright green"
}

for item in gleep_glorp.items():
  print(": ".join(item))

gleep_glorp.update({"num of eyes": "unknown"})

del gleep_glorp["age"]

print()
for item in gleep_glorp.items():
  print(": ".join(item))