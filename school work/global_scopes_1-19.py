# Arden Boettcher
# 1/14/25
# Global Scope Challenges

message = "Live long and prosper!"

def spock():
  print(message)

spock()


count = 0

def increment_count():
  global count
  count += 1

print(count)
increment_count()
increment_count()
increment_count()
print(count)