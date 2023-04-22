import socket
import json

# adres IP i numer portu odbiorcy
HOST = '10.128.79.116'
PORT = 8080

# przygotowanie danych do wysłania
data = {"imie": "Jan", "nazwisko": "Kowalski", "wiek": 30}
json_data = json.dumps(data).encode('utf-8')

# utworzenie połączenia i wysłanie danych
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(json_data)