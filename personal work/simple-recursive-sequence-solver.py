# Arden Boettcher
# 9/18/24
# Simple Recursive Sequence Solver

import math
import string

superscript_map = { # this whole thing is because I want the powers and square roots to be in superscript
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶",
    "7": "⁷", "8": "⁸", "9": "⁹"} # literally just stole this from a guy on stack overflow

trans = str.maketrans(
    ''.join(superscript_map.keys()),
    ''.join(superscript_map.values()))

main = input('\nput 3 numbers in a sequence THEY MUST BE SEPARATED WITH A SPACE:\n\n')

listmain = main.split() # This whole thing makes main a functioning tuple
tuplemain = tuple(listmain) # I also stole this from a guy on stack overflow

tuple0 = float(tuplemain[0])
tuple1 = float(tuplemain[1])
tuple2 = float(tuplemain[2])
num3c1 = tuple1 - tuple0
num3c2 = tuple2 - tuple1 # The reason there's two of each is for confirming that whether the sequence is using addition or multiplication
if num3c1 != 0 and num3c2 != 0: # This prevents dividing by 0 related problems
    num3c3 = tuple1 / tuple0
    num3c4 = tuple2 / tuple1
    dif1 = num3c2 / num3c1
    dif2 = dif1*tuple0 - tuple1
    rounded_dif1 = float(f'{dif1:.4f}') # I got shifted geometric to be working
    rounded_dif2 = float(f'{dif2:.4f}') # I'm so fucking smart
    is_shifted_plus = rounded_dif1 * tuple0 + rounded_dif2 == tuple1
    is_shifted_minus = rounded_dif1 * tuple0 - rounded_dif2 == tuple1
exponent_num = tuple1
exponent_num2 = tuple0
power = 0
root = 0


while exponent_num > 1: # this decides if it's to the power of anything and then counts how many powers
    exponent_num /= tuple0
    power += 1 

while exponent_num2 > 1: # this is for square roots
    exponent_num2 /= tuple1
    root += 1 

if num3c1 == 0:
    print('\nUn = Un-1')
elif num3c1 == num3c2: # This is where the output is decided and finally printed
    print(f'\nUn = Un-1 (+{num3c1})\n')
elif num3c3 == num3c4:
    print(f'\nUn = Un-1 (*{num3c3})\n')
elif exponent_num == 1:
    print(f'\nUn = Un-1({str(power).translate(trans)})\n')
elif exponent_num2 == 1:
    print(f'\nUn = ({str(root).translate(trans)}√)Un-1\n')
elif is_shifted_plus:
    print(f'Un = ({rounded_dif1})Un(+{rounded_dif2})\n')
elif is_shifted_minus:
    print(f'Un = ({rounded_dif1})Un(-{rounded_dif2})\n')
else:
    print('\nyou did not math correctly\n')