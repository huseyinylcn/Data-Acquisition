import network
import time
import urequests
from machine import Pin

class Network:
    def __init__(self, ssid, password, wifitime):
        self.ssid = ssid
        self.password = password
        self.wifitime = wifitime
        self.wifi_error_led = Pin(20, Pin.OUT)
        self.wifi_connect_led = Pin(21, Pin.OUT)
        self.wifi_error_led.value(0)
        self.wifi_connect_led.value(0)
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.connect_attempt_time = 0
        self.connecting = False
     
    def wifi_connect(self):
        # Eğer zaten bağlanma işlemi devam ediyorsa, işlem yapmadan dön
        if self.connecting:
            return False
            
        # LED durumlarını ayarla
        self.wifi_error_led.value(1)
        self.wifi_connect_led.value(0)
        
        # Bağlantıyı başlat ve hemen dön
        print(f"Bağlanma isteği gönderildi: {self.ssid}")
        self.wlan.connect(self.ssid, self.password)
        self.connecting = True
        self.connect_attempt_time = time.time()
        return False  # Henüz bağlantı kurulmadı
    
    def check_connection_status(self):
        # Eğer bağlantı işlemi başlatılmadıysa
        if not self.connecting:
            return False
            
        # Mevcut durumu kontrol et
        status = self.wlan.status()
        
        # Bağlantı başarılı
        if status == network.STAT_GOT_IP:
            self.wifi_error_led.value(0)
            self.wifi_connect_led.value(1)
            self.connecting = False
            ip_info = self.wlan.ifconfig()
            print(f"Bağlantı başarılı! IP: {ip_info[0]}")
            return True
            
        # Zaman aşımı kontrolü
        if time.time() - self.connect_attempt_time > self.wifitime:
            print("Bağlantı zaman aşımına uğradı!")
            self.wifi_error_led.value(1)
            self.wifi_connect_led.value(0)
            self.connecting = False
            return False
            
        # Hata durumu
        if status != network.STAT_CONNECTING:
            print(f"Bağlantı hatası, durum kodu: {status}")
            self.wifi_error_led.value(1)
            self.wifi_connect_led.value(0)
            self.connecting = False
            return False
            
        # Hala bağlanıyor
        return False
            
    def control(self):
        # Bağlantı kontrolü - bağlı değilse false döndür
        if not self.wlan.isconnected():
            self.wifi_error_led.value(1)
            self.wifi_connect_led.value(0)
            return False
            
        # LED durumlarını güncelle
        self.wifi_error_led.value(0)
        self.wifi_connect_led.value(1)
        return True
    
    def is_connected(self):
		result = self.wlan.isconnected()
		if result:
			self.wifi_error_led.value(0)
			self.wifi_connect_led.value(1)
			
		return self.wlan.isconnected()

