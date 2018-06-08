#!/usr/bin/env python
from sense_hat import SenseHat
import time 
import random
sense = SenseHat()

x = 1
for i, c in enumerate("Howdy"):
    r = random.randint(0,255)
    g= random.randint(0,255)
    b = random.randint(0,255)

    sense.show_letter("H", (r, g, b))
    print 'Random number r=',r, 'g=',g, 'b=',b
    time.sleep(1)
    sense.show_letter("O", (r, b, g))
    time.sleep(1)
    sense.show_letter("W", (g, r, b))
    time.sleep(1)
    sense.show_letter("D", (g, b, r))
    time.sleep(1)
    sense.show_letter("Y", (b, g, r))
    time.sleep(1)
    x = x + 1

sense.clear()
