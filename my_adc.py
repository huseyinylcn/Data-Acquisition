from machine import I2C, Pin
import time
from ads1x15 import ADS1115




class myADC:
    def __init__(self):
        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14))
        self.sensor = ADS1115(self.i2c)
    
    def adcRead(self):
        channel0 = self.sensor.read(rate=7, channel1=0)
        voltage0 = self.sensor.raw_to_v(channel0)
        
        channel1 = self.sensor.read(rate=7, channel1=1)
        voltage1 = self.sensor.raw_to_v(channel1)
        
        channel2 = self.sensor.read(rate=7, channel1=2)
        voltage2 = self.sensor.raw_to_v(channel2)
        
        return voltage0, voltage1, voltage2


