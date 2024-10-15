# Arden Boettcher
# 10/8/24
# print practice

import time

input('\nStart? ')

def progress(current, total, bar_length = 20):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '█' + '▒'
    idk = int(fraction * bar_length) * '█'
    padding = int(bar_length - len(arrow)) * '-'
    if fraction >= .99:
        print(f'''\n\033[A\033[A\rLoading...
{idk}{padding} {round(current)}%''', end= '')
    else:
        print(f'''\n\033[A\033[A\rLoading...
{arrow}{padding} {round(current)}%''', end= '')

total = 100
percent = 0.0
print('\n')
while percent <= total:
    progress(percent, total)
    percent += 1
    time.sleep(0.1)
print('\n\nLoading Complete!\n')