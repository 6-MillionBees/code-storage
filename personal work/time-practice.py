import time



n = 0

while n <= 10:
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)
    print(f'Current time = {current_time}')
    n += 1
    time.sleep(1)
    

