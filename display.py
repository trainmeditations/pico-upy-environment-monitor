from machine import Timer, Pin

class DisplayAdapter:
    """Manages display devices"""
    
    _sleepTimer=Timer()
    _display=None
    _showTime=5000

    def __init__(self, display, showTime=0):
        self._display=display
        if showTime > 0:
            self._showtime=showTime

    def display_logo(self):
        d=self._display
        d.fill(0)
        d.fill_rect(0, 0, 32, 32, 1)
        d.fill_rect(2, 2, 28, 28, 0)
        d.vline(9, 8, 22, 1)
        d.vline(16, 2, 22, 1)
        d.vline(23, 8, 22, 1)
        d.fill_rect(26, 24, 2, 4, 1)
        d.text('MicroPython', 40, 0, 1)
        d.text('SSD1306', 40, 12, 1)
        d.text('OLED 128x64', 40, 24, 1)
        d.show()
    
    def display_time(self):
        d=self._display
        d.fill(0)
        d.text(str(starttime),0,8)
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
              callback=lambda _: pin.irq(trigger=Pin.IRQ_RISING, handler=self.dispButtonHandler))
