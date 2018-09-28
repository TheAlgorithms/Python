# server.py

import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.socket = conn
        self.addr = addr
        print('[+]New Thread Started for {}'.format(addr))

    def run(self):
        while 1:
            # receive data from client
            data = conn.recv(1024)

            # sent data to client
            if not data:
                break
            conn.send(data + b' [ addition by server ]')


# The TCP port number this server is bound to
HOST, PORT = '127.0.0.1', 1400

# create a socket object, bind it to (HOST,PORT)
# listen for incoming connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    # accept a connection
    conn, addr = s.accept()

    # start thread
    t = ClientThread(conn,addr)
    t.start()
    print('connected to:', addr)