import socket

HOST = '10.128.79.116'  # adres IP serwera
PORT = 8000  # numer portu serwera

# utworzenie gniazda i nasłuchiwanie na połączenia
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print('Połączono z:', addr)

    # odbiór danych i wysłanie odpowiedzi
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode('utf-8')
        print('Otrzymane dane:', data)
        response = 'Otrzymałem dane: ' + data
        conn.sendall(response.encode('utf-8'))