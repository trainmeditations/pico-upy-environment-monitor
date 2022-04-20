import time
from machine import Timer, Pin, I2C
from ssd1306 import SSD1306_I2C
from display import DisplayAdapter
import micropython
micropython.alloc_emergency_exception_buf(100)

#Devices
pico_led = Pin(25, Pin.OUT)
dispButton = Pin(22, Pin.IN, Pin.PULL_DOWN)

#need to do the following to avoid lockup, before secondary I2C setup?
#from PiicoDev_MS5637 import PiicoDev_MS5637

#Display
dispClockI2C = I2C(1, freq=400000, sda=Pin(18), scl=Pin(19))
oled = SSD1306_I2C(128, 64, dispClockI2C)
oled.poweroff()

oledDisplay = DisplayAdapter(oled)

#before here
oledDisplay.display_logo()

dispButton.irq(trigger=Pin.IRQ_RISING,
               handler=lambda a:micropython.schedule(oledDisplay.dispButtonHandler, a))

#or sleep here (20ms not long enough)
time.sleep_ms(100)
