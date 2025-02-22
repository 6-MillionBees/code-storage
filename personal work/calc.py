# Arden Boettcher
# 1/8/25
# calculator

def a(*nums):
  for x in nums:
    print(x)
    if x <= -6:
      answer = abs(x -8)
      print("|x-8| =", answer)
    if -6 < x <= 1:
      answer = 2*x - x**2
      print("2*x - x**2 =", answer)
    if x > 1:
      answer = -4*x + 7
      print("-4*x + 7 =", answer)
    print()

a(8, 1, -7, -3, -0.5, (9/4))