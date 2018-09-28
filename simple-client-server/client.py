# client.py

import socket


HOST, PORT = '127.0.0.1', 1400

# create a socket object, connect to (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# send data to server
s.send(b'Hello World')

# receive data from server
data = s.recv(1024)

s.close()

# print data
print(repr(data.decode('ascii')))
