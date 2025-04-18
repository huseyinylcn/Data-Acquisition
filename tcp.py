import socket
import time
import json


class TCP:
    def __init__(self,tcpIp,port):
        self.tcpIp = tcpIp
        self.port = port
        self.tcpConnect()



    def tcpConnect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.tcpIp, self.port))
        except:
            pass
            

    def data_push(self,data):
        try:
            
            data = json.dumps(data).encode()
            self.client_socket.sendall(data)
        except Exception as e:
            print(e)


tcp = TCP('127.0.0.1',50000)


while True:
    tcp.data_push([1,1,1,1])
    time.sleep(0.2)