from machine import Timer
from micropython import schedule
from env_sensors import getCombinedValues
from logger import EnvLogger

#logtime=5*60*1000
logtime=30000

envLogger=EnvLogger("log.csv")

def logValues(_):
    readings=getCombinedValues()
    oledDisplay.displaySensors(*readings)
    oledDisplay.show(1000)
    envLogger.logValues(readings)

logTimer=Timer(period=logtime, mode=Timer.PERIODIC,
               callback=lambda a:schedule(logValues,a))
