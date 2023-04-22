import socket

HOST = '10.128.67.23' # Replace with the IP address of the receiving computer
PORT = 8080 # Replace with a port number of your choice

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')