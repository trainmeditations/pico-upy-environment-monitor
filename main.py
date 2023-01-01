from machine import Timer
from micropython import schedule
from env_sensors import getCombinedValues
from logger import EnvLogger
#explicit import of oledDisplay to allow import of main from REPL
from boot import oledDisplay, oledDisplayP

#5 minutes
logtime=5*60*1000

envLogger=EnvLogger("log.csv")
logTimer=None

def logValues(_):
    readings=getCombinedValues()
    oledDisplayP.displaySensors(*readings)
    oledDisplay.printLine("Logging Values...")
    #oledDisplayP.show(1000)
    envLogger.logValues(readings)

def startLogging():
    global logTimer
    logValues(None)
    logTimer=Timer(period=logtime, mode=Timer.PERIODIC,
                   callback=lambda a:schedule(logValues,a))

oledDisplay.printLine("Starting Logging")
startLogging()