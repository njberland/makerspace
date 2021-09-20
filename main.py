# code that will run on micropython on startup
# to run forever make a loop of type "while True"

import machine
import time

from machine import Pin

# create an output pin on pin #0                                                                                                             
p13 = Pin(13, Pin.OUT)
for i in range(2):
    p13.value(1)
    time.sleep(1)
    p13.value(0)
    time.sleep(1)
