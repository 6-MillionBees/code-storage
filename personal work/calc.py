# Arden Boettcher
# 1/8/25
# calculator

def f(x):
  answer = 8 - 3*(x)
  print(f"8 - 3*({x}) = ", answer)
  return answer

def g(x):
  answer = (x)**2 + 2*(x)
  print(f"(x)**2 + 2*({x}) = ", answer)
  return answer

def h(x):
  answer = -5/2*(x) - 1
  print(f"-5/2*({x}) - 1 = ", answer)
  return answer

print(3 * h(2) - f(-9))
