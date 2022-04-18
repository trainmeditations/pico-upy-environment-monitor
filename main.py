from env_sensors import getCombinedValues
from machine import Timer, RTC

#oledDisplay.display_logo()
#dispButton.irq(trigger=Pin.IRQ_RISING, handler=oledDisplay.dispButtonHandler)

LOGFILE="data.csv"

def writeCSV(fields,file):
    print(*fields, sep=",", file=file)

def writeHeader(file):
    writeCSV(("Timestamp","Temperature","Pressure","Humidity"), file)

def showValues(_):
    oledDisplay.displaySensors(*getCombinedValues())
    oledDisplay.show(10000)
    
logTimer=Timer(period=5*60*1000, mode=Timer.PERIODIC, callback=showValues)
