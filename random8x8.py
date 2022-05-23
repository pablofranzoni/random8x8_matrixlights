"""
MicroPython random lights 8x8 LED matrix max7219
https://github.com/mcauser/micropython-max7219

MIT License
Copyright (c) 2022 Pablo Franzoni

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from machine import Pin, SPI
from max7219 import Matrix8x8
import time
import random 

#ESP32 configuration
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(14), mosi=Pin(13))
ss = Pin(15, Pin.OUT)
display = Matrix8x8(spi, ss, 1)
display.fill(0)
display.show()
 
while True:
    for i in range(64):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        t = random.randint(0, 1)
        display.pixel(x,y,t)
        time.sleep_ms(10)
        display.show()
