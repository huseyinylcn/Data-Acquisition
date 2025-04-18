
import random
import multiprocessing
import time
import logging




class ADC:

    q = multiprocessing.Queue()
    def __init__(self):
        mp = multiprocessing.Process(target=self.data_production,args=(self.q,))
        mp.start()
    
   
    def data_production(self, q):
        
        try:
           sayi = random.randint(10000, 99999)  
           if sayi < 10000 or sayi > 99999:
               logging.error("Gecersiz sayi uretildi")
               return
           q.put([time.time(), sayi, sayi, sayi])  
           time.sleep(1)  
        except Exception as e:
           logging.error(f"Veri üretme hatası: {e}") 

            

    def data_read(self):

            try:
                veri = self.q.get(timeout=5)
                return veri
            except Exception as e:
                logging.error(f"Veri okuma hatası: {e}")
                time.sleep(1)


           
if __name__ == "__main__":
    adc = ADC()
    adc.data_read()




