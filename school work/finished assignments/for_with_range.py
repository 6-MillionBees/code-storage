# Arden Boettcher
# 12/11/24
# For with Range

CONVERSION_RATIO = 1.8

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CONVERSION_RATIO) + 32
    return fahrenheit

for temperature in range(0, 21):
    temp_temp = convert_to_fahrenheit(temperature)
    print(f'Celsius: {temperature}   Fahrenheit: {temp_temp:.1f}')