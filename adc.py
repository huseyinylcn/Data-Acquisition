
import random
import multiprocessing
import time


class ADC:

    q = multiprocessing.Queue()
    def __init__(self):
        mp = multiprocessing.Process(target=self.data_production,args=(self.q,))
        mp.start()
    
   
    def data_production(self,q):

            sayi = random.randint(10000, 99999)

            q.put([time.time(),sayi,sayi,sayi])
            time.sleep(1)
            

    def data_read(self):
        while True:
            print(self.q.get())






           
if __name__ == "__main__":
    adc = ADC()
    adc.data_read()











    
