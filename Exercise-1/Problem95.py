
# Python Program to Create a Countdown Timer

import time

def countdown(time_sec):
    while time_sec:
        mins,secs=divmod(time_sec,60)
        timeformat='{:02d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')

    print("stop")

countdown(5)
