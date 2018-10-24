# client.py

import socket

HOST, PORT = '127.0.0.1', 1400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(b'Hello World')
data = s.recv(1024)

s.close()
print(repr(data.decode('ascii')))
