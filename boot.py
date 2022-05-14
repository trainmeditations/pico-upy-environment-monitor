import time
from machine import Timer, Pin, I2C
from micropython import schedule
from ssd1306 import SSD1306_I2C
from PiicoDev_SSD1306 import create_PiicoDev_SSD1306
from display import DisplayAdapter
import micropython
micropython.alloc_emergency_exception_buf(100)

#Devices
pico_led = Pin(25, Pin.OUT)
dispButton = Pin(22, Pin.IN, Pin.PULL_DOWN)

#need to do the following to avoid lockup, before secondary I2C setup?
#from PiicoDev_MS5637 import PiicoDev_MS5637

#Display
#dispI2C = I2C(1, freq=400000, sda=Pin(18), scl=Pin(19)) #separate I2C bus
dispI2C = I2C(0)
oled = SSD1306_I2C(128, 64, dispI2C)
oled.poweroff()

oledP = create_PiicoDev_SSD1306(addr=0x3D)
oledP.poweroff()

oledDisplay = DisplayAdapter(oled)
oledDisplayP = DisplayAdapter(oledP)

#before here
oledDisplay.display_logo()
oledDisplayP.display_logo()

oledDisplay.show()
oledDisplayP.show()

displays=[oledDisplay,oledDisplayP]

def _dispButtonHandler(pin):
    pin.irq(handler=None)
    for display in displays:
        display.show(display._showTime)
    Timer(period=250,
          mode=Timer.ONE_SHOT,
          callback=lambda _: pin.irq(trigger=Pin.IRQ_RISING,
                                     handler=lambda pin:schedule(_dispButtonHandler, pin)))
dispButton.irq(trigger=Pin.IRQ_RISING,
               handler=lambda pin:micropython.schedule(_dispButtonHandler, pin))


#dispButton.irq(trigger=Pin.IRQ_RISING,
#               handler=lambda a:micropython.schedule(oledDisplayP.dispButtonHandler, a))

#or sleep here (20ms not long enough)
#time.sleep_ms(100)
