#! /usr/bin/env python

"""
    Script Name: stopwatch.py
       Function: This script mimics a stopwatch with a lap timer
                 The directions are given below. 
                 Make sure you display start when the stopwatch start.
                 Be sure that for a lap time you give the lap number
                 the total time and the lap time. 
                 Use a <Ctrl-c> to exit from the script cleanly.
                 remember that a try: except: block will
                 capture a <Ctrl-c>
"""
import time

directions = \
"""
   Press ENTER to begin. 
   Afterwards, press ENTER to get lap time. 
   Press Ctrl-C to quit.
   
"""
print(directions)

input('Press ENTER to Start')
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input('Press ENTER to get lap time')
        lapStopTime = time.time()
        lapTime = round(lapStopTime - lastTime, 2)
        totalTime = round(lapStopTime - startTime, 2)
        print('Lap #%s: %ss (%ss)' % (lapNum, totalTime, lapTime))
        lapNum += 1
        lastTime = lapStopTime 
except KeyboardInterrupt:
    print('\nEnd of stopwatch')
