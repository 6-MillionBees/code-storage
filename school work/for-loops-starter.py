# Arden Boettcher
# 11/6/24
# For Loops Starter

# 4-3 Counting to Twenty

print()

for num in range(21):
    print(num, end = ' ')
print()

input('Press enter when you want a wall of numbers to cover the output above.\n')

# 4-4 One Million

one_million = range(1000001)

for num in one_million:
    print(num, end = ' ')
print()


# 4-5 Summing a Million

print(min(one_million))
print(max(one_million))

print(sum(one_million))


# 4-6 Odd Numbers

odd = [x for x in range(1, 21, 2)]

for x in odd:
    print(x, end = ' ')
print()


# 4-7 Threes

threes = range(3, 31, 3)

for x in threes:
    print(x, end = ' ')
print()


# 4-8 Cubes

cubes = [x*x*x for x in range(1, 11)]

for x in cubes:
    print(x, end = ' ')