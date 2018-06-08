#!/bin/env python
# this script uses the Touch Switch to Toggle 

import RPi.GPIO as GPIO
import time

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Touch Switch; pin 31 = GPIO 6
touch_pin = 31

# set Touch Switch pin's mode as input 
GPIO.setup(touch_pin,GPIO.IN)

# create infinite loop that reads Touch Switch input
while True: 
    if GPIO.input(touch_pin) == 0:
        # add code to turn off a sensor
        if GPIO.input(touch_pin) == 1:
        # add code to turn on a sensor

    
