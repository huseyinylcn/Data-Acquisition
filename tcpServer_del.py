import socket

# Sunucu IP ve Port ayarları
HOST = '0.0.0.0'  # Tüm IP'lerden gelen bağlantılara izin ver
PORT = 50000      # Herhangi bir port seçilebilir

# Soket oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

server_socket.listen(1)

print(f"Sunucu {PORT} portunu dinliyor...")

# Bağlantı bekle
conn, addr = server_socket.accept()
print(f"{addr} bağlandı.")

while True:
    data = conn.recv(1024)  # Veri al
    if not data:
        break
    print("Gelen veri:", data.decode())


