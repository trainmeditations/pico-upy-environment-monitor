import os
from machine import RTC

def _writeCSV(fields, file):
    print(*fields, sep=",", file=file)

def _writeHeader(file):
    _writeCSV(("Timestamp","Temperature","Pressure","Humidity"), file)

class EnvLogger:
    _rtc=None
    _logFilename=None
    
    def __init__(self, file):
        self._rtc=RTC()
        self._logFilename=file
        try:
            os.stat(file)
        except OSError:
            newf=open(file, "a")
            _writeHeader(newf)
            newf.close()
    
    def logValues(self, values):
        t=self._rtc.datetime()
        timestamp='{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}'.format(t[0], t[1], t[2], t[4], t[5], t[6])
        with open(self._logFilename, "a") as file:
            _writeCSV((timestamp,)+values, file)
        
