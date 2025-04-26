
import socket
import json
import time
from machine import Pin



class TCP:
   
    def __init__(self,ip,port):
		self.ip = ip
		self.port = port
		self.client_socket = None
		self.connected = False
		self.tcp_led = Pin(22, Pin.OUT)
		self.tcp_led.value(0)


    def connect(self):
        try:

            if self.client_socket:
                try:
                    self.client_socket.close()
                except:
                    pass

            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.ip, self.port))
            self.client_socket.settimeout(None)
            self.connected = True
            self.tcp_led.value(1)
            return True
            # burada tcp başarılı ledleri yak bence
#         except KeyboardInterrupt:
#             print("The program was stopped by the user")
#             self.connected = False
#             self.tcp_led.value(0)
#             return False
#             # burada tcp başarısız ledini yak
        except Exception as e:
            print("TCP General Error")
            self.tcp_led.value(0)
            self.connected = False
            return False
            # tcp başarısız ledini yak
      
    
    def send(self,data):
        if not self.connected or not self.client_socket:
            print("Cannot send: Not connected")
            self.tcp_led.value(0)
            return False
        
        try:
			
            data = json.dumps(data).encode()
            self.client_socket.sendall(data+ "\n")
            return True

        except Exception as e:
			print("Failed to Send Data!")
			self.connected = False
			self.tcp_led.value(0)
			return False
	
	def status(self):
		return self.connected










