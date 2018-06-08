#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# this script will clear any LED's left in the 'on' state that a 
# different script may have left on 

sense.clear()
