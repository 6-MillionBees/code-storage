# Arden Boettcher
# 10/5/24
# Time Practice

import keyboard
import time
import math


start_timer = input('start timer? Y/N\n')


if start_timer.lower() == 'y':
    time_local_1 = 0
    time_s = 0
    print('press N to break the loop')
    while start_timer != 'n':
        if keyboard.press_and_release('n'):
            break
        else:
            time_local = time.localtime() # WHO NEEDS ASYNCIO WHEN WE GOTS THE MATH
            time_thing = time.strftime('%H:%M:%S', time_local)
            if time_local == time_local_1:
                continue
            time_m = time_s / 60 # there is 100% a better way to do this but I love it so damn much
            time_m = math.floor(time_m)
            left_time_s = time_s % 60
            print(f'{time_m}.{left_time_s}')
            time_s += 1
            time_local_1 = time_local
    print(f'Total time: {time_m} minutes and {left_time_s} seconds.')
elif start_timer.lower() == 'n':
    print('Okie doke! I guess you didn\'t want to see something really cool.')
else:
    print('Y or N ONLY')