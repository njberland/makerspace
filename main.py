# code that will run on micropython on startup
# to run forever make a loop of type "while True"

from machine import Pin
import time

# configure pin 13                                                                                                           
p13 = Pin(13, Pin.OUT)

# run for a few seconds
for i in range(2):
    p13.value(1)
    time.sleep(1)
    p13.value(0)
    time.sleep(1)
