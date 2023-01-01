import time
from machine import Timer, Pin
from micropython import schedule, alloc_emergency_exception_buf
alloc_emergency_exception_buf(100)
#from ssd1306 import SSD1306_I2C
from PiicoDev_SSD1306 import create_PiicoDev_SSD1306
from display import DisplayAdapter

#Devices
pico_led = Pin(25, Pin.OUT)
dispButton = Pin(22, Pin.IN, Pin.PULL_DOWN)

#need to do the following to avoid lockup, before secondary I2C setup?
#from PiicoDev_MS5637 import PiicoDev_MS5637

#Display
#dispI2C = I2C(1, freq=400000, sda=Pin(18), scl=Pin(19)) #separate I2C bus
#dispI2C = I2C(0, freq=400000)
#oled = SSD1306_I2C(128, 64, dispI2C)
oled = create_PiicoDev_SSD1306()
oled.poweroff()

oledP = create_PiicoDev_SSD1306(addr=0x3D)
oledP.poweroff()

oledDisplay = DisplayAdapter(oled)
oledDisplayP = DisplayAdapter(oledP)

#before here
# for x in range(1,12):
#     oledDisplay.printLine(str(x))
#     oledDisplay.show()
#     time.sleep_ms(1000)
oledDisplay.printLine("Displays Setup")
oledDisplay.show()

oledDisplayP.display_logo()

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
               handler=lambda pin:schedule(_dispButtonHandler, pin))

oledDisplay.printLine("Button Linked")
oledDisplay.show()
#dispButton.irq(trigger=Pin.IRQ_RISING,
#               handler=lambda a:micropython.schedule(oledDisplayP.dispButtonHandler, a))

#or sleep here (20ms not long enough)
#time.sleep_ms(100)
