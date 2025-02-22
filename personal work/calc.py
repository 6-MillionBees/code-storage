# Arden Boettcher
# 1/8/25
# calculator

# def f(*args):
#   for x in args:
#     if x < -2:
#       print(x**2 - 1)
#     elif x >= -2:
#       print(5 * x + 3)


# f(-5, -2, 7)


# def g(*args):
#   for x in args:
#     if x <= 4:
#       print(0.5*x + 3)
#     if -4 < x < 1:
#       print(-x-1)
#     if x >= 1:
#       print(2*(x**3) + 9)
#     print()

# g(2, -1, -6)


def g(x):
  if x <= -5:
    print((x, -1))
  if -5 < x < 1:
    print((x, -x - 3))
  if x >= 1:
    print((x, 6))
  print()


for x in range(-10, 10):
  g(x)
