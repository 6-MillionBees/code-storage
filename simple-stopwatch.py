# Arden Boettcher
# 10/5/24
# Simple Stopwatch

import keyboard
import time


input('Press enter to start the timer\n')


time_local_1 = 0
time_s = 0
time_local = time.localtime()
time_formatted = time.strftime('%H:%M:%S', time_local)
print('Press S to stop the timer')
print(f'Starting time {time_formatted}')

while True:
    if keyboard.is_pressed('s'):
        break
    else:
        time_local = time.localtime()
        time_formatted = time.strftime('%H:%M:%S', time_local)

        if time_local == time_local_1: # A problem that I ran into is that I couldn't have the input detection run while only printing the time every second.
            continue
# I solved this by letting the loop run forever but only printing once the local time changed, as a side effect the timer can start between seconds making it slightly inaccurate.

        time_m = time_s / 60 # there is 100% a better way to do this but I love it so much
        time_m = int(time_m)
        left_time_s = time_s % 60
        print(f'\r{time_m}:{left_time_s}  ', end = '')
        time_s += 1
        time_local_1 = time_local

print()
print(f'Ending time {time_formatted}')
print(f'Total time: {time_m} minutes and {left_time_s} seconds.')
input('Press enter to finish the program\n') # I use this to time my reading.