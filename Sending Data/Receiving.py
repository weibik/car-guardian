import socket

HOST = '' # Leave blank to accept connections from any IP address
PORT = 8080 # Same port number used on the sending computer

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        print(data)