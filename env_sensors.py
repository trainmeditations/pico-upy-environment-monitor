from PiicoDev_BME280 import PiicoDev_BME280
from PiicoDev_TMP117 import PiicoDev_TMP117
from PiicoDev_MS5637 import PiicoDev_MS5637

envSensor=PiicoDev_BME280()
pTempSensor=PiicoDev_TMP117()
pPresSensor=PiicoDev_MS5637()

def getCombinedValues():
    tempC, presPa, humRH = envSensor.values()
    pTemp = pTempSensor.readTempC()
    pPres = pPresSensor.read_pressure()
    return pTemp, pPres, humRH