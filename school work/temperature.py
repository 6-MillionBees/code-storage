# Arden Boettcher
# 1/31/25
# Temperature Calculator


def to_celcius(fahrenheit):
  return (5/9)*(fahrenheit-32)

def to_fahren(celcius):
  return (9/5)*celcius + 32

def to_kelvin(celcius):
  return celcius + 273.15

def from_kelvin(kelvin):
  return kelvin - 273.15

print("1.)", to_fahren(30))
q2 = to_celcius(70)
print("2.)", q2, "&", to_kelvin(q2))
print("3.)", from_kelvin(277.65))
print("4.)", to_kelvin(to_celcius(10000)))