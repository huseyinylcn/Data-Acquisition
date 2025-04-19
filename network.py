import network
import time
import urequests
from machine import Pin



class Network():
    def __init__(self,ssid,password,wifitime):
        self.ssid = ssid
        self.password = password
        self.wifitime = wifitime


        self.wifi_error_led = Pin(20, Pin.OUT)
        self.wifi_connect_led = Pin(21, Pin.OUT)

        self.wifi_error_led.value(0)
        self.wifi_connect_led.value(0)


        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wifi_connect()


    def wifi_connect(self):
        
        self.wlan.connect(self.ssid, self.password)
        
        
        
        while self.wifitime > 0:

            self.wifitime -= 1
            
            self.wifi_error_led.value(1)
         

            time.sleep(0.5)
            self.wifi_error_led.value(0)
            time.sleep(0.5)
            
            if self.wlan.status() < 0 or self.wlan.status() >= 3:
                self.wifi_error_led.value(1)
                self.wifi_connect_led.value(0)
                break 

           
            
           
        if self.wlan.status() != 3:
            self.wifi_error_led.value(1)
            self.wifi_connect_led.value(0)
            self.wifi_connect()
        else:
           
            self.wifi_error_led.value(0)
            self.wifi_connect_led.value(1)
            print("connect")
            

            durum = self.wlan.ifconfig()
            print(durum[0])
            
            
        self.wlan = self.wlan
        return self.wlan

    def control(self):
        if self.wlan is None or not self.wlan.isconnected():
            self.wifi_connect()
            return False
        
        try:
            yanit = urequests.get('http://www.google.com', timeout=5)
            yanit.close()
            return True
        except:
            return False
        




def netFunc():
   net = Network("Hy","12345678",20)
   while True:

        result = net.control()
        print(result)
        time.sleep(10)








