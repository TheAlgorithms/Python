# server.py

import socket

HOST, PORT = '127.0.0.1', 1400

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print('connected to:', addr)

while 1:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data + b' [ addition by server ]')
        
conn.close()
