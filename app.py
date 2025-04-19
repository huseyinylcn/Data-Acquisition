from tcp import tcp
from  network import netFunc 

import threading
import time


t1 = threading.Thread(target=netFunc)
t1.start()



while True:


   tcpstatus = tcp.data_push([1,1,1,1])
   time.sleep(0.5)

   if tcpstatus != True:
      tcp.tcpConnect()
      print(tcpstatus)
