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
            self.client_socket.settimeout(5)
            return True
        
        except socket.timeout:
            return "0x403" 
        except ConnectionRefusedError:
            return "0x404"
        except OSError as e:
            return "0x403"
        except Exception as e:
            return "0x403"
        

            

    def data_push(self,data):
        try:
            data = json.dumps(data).encode()
            self.client_socket.sendall(data)
            return True
        except Exception as e:
            return False



tcp = TCP('127.0.0.1',50000)


