from machine import Timer
from micropython import schedule
from env_sensors import getCombinedValues
from logger import EnvLogger
#explicit import of oledDisplay to allow import of main from REPL
from boot import oledDisplay

#5 minutes
logtime=5*60*1000

envLogger=EnvLogger("log.csv")

def logValues(_):
    readings=getCombinedValues()
    oledDisplay.displaySensors(*readings)
    oledDisplay.show(1000)
    envLogger.logValues(readings)

def startLogging():
    logValues(None)
    logTimer=Timer(period=logtime, mode=Timer.PERIODIC,
                   callback=lambda a:schedule(logValues,a))

startLogging()