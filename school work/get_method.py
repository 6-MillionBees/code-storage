# Arden Boettcher
# 1/24/25
# Get Method

friends = {
  "oliver": 1234,
  "rayden": 4321,
  "ben":    9876
}

for key in friends:
  print(key + ":", friends[key])

id_num = friends.get("placeholder", -1)

print(f"\nStuden Id for Placeholder: {id_num}")

if id_num == -1:
  print("Requested key not found!")
