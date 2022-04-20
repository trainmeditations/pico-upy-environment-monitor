from machine import Timer, Pin, RTC
from micropython import schedule

class DisplayAdapter:
    """Manages display devices"""
    
    _sleepTimer=Timer()
    _display=None
    _showTime=5000
    _rtc=None

    def __init__(self, display, showTime=0):
        self._rtc=RTC()
        self._display=display
        if showTime > 0:
            self._showtime=showTime

    def display_logo(self):
        t=self._rtc.datetime()
        date='{:04d}-{:02d}-{:02d}'.format(t[0], t[1], t[2])
        time='{:02d}:{:02d}:{:02d}'.format(t[4], t[5], t[6])
        d=self._display
        d.fill(0)
        d.fill_rect(0, 0, 32, 32, 1)
        d.fill_rect(2, 2, 28, 28, 0)
        d.vline(9, 8, 22, 1)
        d.vline(16, 2, 22, 1)
        d.vline(23, 8, 22, 1)
        d.fill_rect(26, 24, 2, 4, 1)
        d.text('MicroPython', 40, 0, 1)
        d.text(date, 40, 12, 1)
        d.text(time, 40, 24, 1)
        d.show()
    
    def displaySensors(self, temp, press, hum):
        d=self._display
        self.display_logo()
        d.text("Temp: "+str(temp), 0, 34)
        d.text("Pres: "+str(press), 0, 44)
        d.text("Humi: "+str(hum), 0, 54)
        d.show()
        
    def show(self, time):
        self._sleepTimer.deinit()
        self._display.poweron()
        self._sleepTimer.init(period=time,
                         mode=Timer.ONE_SHOT,
                         callback=lambda _:self._display.poweroff())
        
    def dispButtonHandler(self, pin):
        pin.irq(handler=None)
        self.show(self._showTime)
        Timer(period=250,
              mode=Timer.ONE_SHOT,
              callback=lambda _: pin.irq(trigger=Pin.IRQ_RISING,
                                         handler=lambda a:schedule(self.dispButtonHandler, a)
                                         )
              )
