import socket
import csv
import time

# Sunucu IP ve Port ayarları
HOST = '0.0.0.0'  # Tüm IP'lerden gelen bağlantılara izin ver
PORT = 50000      # Herhangi bir port seçilebilir

# Soket oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Sunucu {PORT} portunu dinliyor...")


conn, addr = server_socket.accept()
print(f"{addr} bağlandı.")

# CSV dosyasının adı
csv_file = "veri.log"

while True:
    try:
        data = conn.recv(1024)  # Veri al
        if not data:
            break
            
        received_data = data.decode()
      
        
        # Alınan veriyi CSV dosyasına yaz
        with open(csv_file, 'a', newline='') as file:

            file.write(received_data)
            
    except Exception as e:
        print(f"Hata oluştu: {e}")
        break

# Bağlantıyı kapat
conn.close()
server_socket.close()
print("Sunucu kapatıldı.")