# Arden Boettcher
# 10/2/24
# Caesar Cipher

words = input('Enter text: ')
offset = int(input('Enter offset: '))
while offset >= 26:
    offset -= 26

for letter in words.lower():
    words_letter = ord(letter)
    if letter.isalpha(): # Stole the ideas off of stack overflow
        words_letter = ord(letter) + offset
        if words_letter > ord('z'):
            words_letter -= 26
    words_letter_final = chr(words_letter)
    print(words_letter_final,end= '')
print()
