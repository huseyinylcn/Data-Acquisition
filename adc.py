import random
import multiprocessing
import time
import sqlite3

class ADC:





    q = multiprocessing.Queue()
    def __init__(self):
        mp = multiprocessing.Process(target=self.add_queue, args=(self.q,))
        mp.start()







    def veritabanina_kaydet(veri):
        try:
            conn = sqlite3.connect("veriler.db")
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS sismik_veriler (
                                tarih TEXT,
                                deger1 INTEGER,
                                deger2 INTEGER,
                                deger3 INTEGER
                            )''')
            cursor.execute("INSERT INTO sismik_veriler VALUES (?, ?, ?, ?)", veri)
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Veritabanı hatası: {e}")
 
 
 
 
 
    def data_production(self):
        try:
            sayi = random.randint(10000, 99999)
            if sayi < 10000 or sayi > 99999:
                print("Geçersiz sayı üretildi")
                return None
            tarih = time.strftime("%d.%m.%Y %H:%M:%S")
            return [tarih, sayi, sayi, sayi]
        except Exception as e:
            print(f"Veri üretme hatası: {e}")
            return None





    def add_queue(self, q):
        while True:
            veri = self.data_production()
            if veri:
                q.put(veri)
            time.sleep(1)





    def data_read(self):
        while True:
            try:
                veri = self.q.get(timeout=5)
                print(veri)            
                self.veritabanina_kaydet(veri)

            except Exception as e:
                print(f"Veri okuma hatası: {e}")
                time.sleep(1)





if __name__ == "__main__":
    adc = ADC()
    adc.data_read()



