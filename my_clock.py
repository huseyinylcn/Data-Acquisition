from machine import RTC, Timer
import utime

class My_Clock:
    def __init__(self):
        self.rtc = RTC()
        self.rtc.datetime((2025, 4, 23, 3, 23, 58, 0, 0))
        self.start_time_us = utime.ticks_us() 
        self.last_capture_time = 0
        self.capture_interval_us = 10000 
    
    def clock_setting(self): 
        dt = self.rtc.datetime()
        elapsed_us = utime.ticks_diff(utime.ticks_us(), self.start_time_us) % 1000000
        timestamp = {
            "year": dt[0],
            "month": dt[1],
            "day": dt[2],
            "hour": dt[4],
            "minute": dt[5],
            "second": dt[6],
            "microsecond": elapsed_us
        }
        
        return timestamp
    
    def format_clock(self, ts):
        return "{:02d}:{:02d}:{:02d}.{:06d}".format(
            ts["hour"], ts["minute"], ts["second"], ts["microsecond"]
        )
    
    def get_clock(self):
        ts = self.clock_setting()
        formatted_time = self.format_clock(ts)
        self.last_capture_time = utime.ticks_us() 
        return formatted_time
        
    def get_date(self):
        ts = self.clock_setting()
        formatted_date = "{:04d}-{:02d}-{:02d}".format(
            ts["year"], ts["month"], ts["day"]
        )
        return formatted_date


