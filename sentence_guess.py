#!/usr/bin/env python
from sense_hat import SenseHat 
sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

speed = 0.05
message = "Hello World"

sense.show_message(message, speed, text_colour=yellow, back_colour=black)
user_guess = raw_input("What is your guess?")

speed = speed + 0.01

sense.clear()
