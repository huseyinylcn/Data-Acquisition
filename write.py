import machine
import sdcard
import os



class Write:
    def __init__(self):
        self.spi = machine.SPI(0,    
                            sck=machine.Pin(2), 
                            mosi=machine.Pin(3),  
                            miso=machine.Pin(4))  
        self.cs = machine.Pin(5, machine.Pin.OUT)
        self.sd = sdcard.SDCard(self.spi, self.cs)
        self.vfs = os.VfsFat(self.sd)
        os.mount(self.vfs, "/sd")
        self.sayac = 0

    def dosya_olusturma(self,fileName):
        try:
            open(f"/sd/{fileName}","w").close()
            return True
        except Exception as e:
            return False
    
    def dosya_kontrol(self,filename):
		try:
			if os.path.exists(dosya_yolu):
				return True
			else:
				return "0x401"
		except Exception as e:
			print("hata 0")
			return False
		
    def dosya_acma(self,fileName):
        try:
            self.dosya = open(f"/sd/{fileName}","a")
            return True 
        except Exception as e:
			print("hata 1")
			return False
        
    def dosya_yaz(self,data):
        try:
			self.sayac += 1
			self.dosya.write(data)
			if self.sayac == 10000:
				self.dosya.flush()
				self.sayac = 0
			return True 
        except Exception as e:
			pass
    def dosya_kapat(self):
        try:
            if self.dosya is not None:
                self.dosya.close()
            return True 
        except Exception as e:
			pass



