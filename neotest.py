from machine import Pin
from neopixel import NeoPixel
import time

# make sure the pin number and pixel count are correct
PIN = 21
PIXELS = 16

def demo(pin, n):
    np = NeoPixel(Pin(pin), n)

    # cycle                                                                                                                                  
    for i in range(8 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce                                                                                                                                 
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out                                                                                                                            
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear                                                                                                                                  
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

demo(PIN,PIXELS)
