# Arden Boettcher
# 10/5/24
# Time Practice

import keyboard
import time
import math


start_timer = input('start timer? Y/N\n')


if start_timer.lower() == 'y':
    time_local_1 = 0
    time_s = 0 # I made it wait for a tick before it starts counting because 
    print('press N to break the loop')
    time_local = time.localtime()
    time_thing = time.strftime('%H:%M:%S', time_local)
    print(f'starting time {time_thing}')
    while True:
        if keyboard.is_pressed('n'):
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
            time.sleep(0.05) # This is here to save processing power without it the loop would just be going crazy with your computers resources
    print(f'end time {time_thing}')
    print(f'Total time: {time_m} minutes and {left_time_s} seconds.')
    input('Press enter to finish the program\n')
elif start_timer.lower() == 'n':
    print('Okie doke! I guess you didn\'t want to see something really cool.')
else:
    print('Y or N ONLY')