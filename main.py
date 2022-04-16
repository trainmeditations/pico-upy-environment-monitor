from env_sensors import getCombinedValues

#oledDisplay.display_logo()
#dispButton.irq(trigger=Pin.IRQ_RISING, handler=oledDisplay.dispButtonHandler)

def showValues():
    oledDisplay.displaySensors(*getCombinedValues())
    
#showValues();