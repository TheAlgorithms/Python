import socket
wr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hst = socket.gethostname()
port = 7868
wr.connect((hst,port))
dt = wr.recv(767)
print('Srvr :',dt.decode())
while True:
    gt = input('C3 : ')
    wr.send(gt.encode())
    if(gt=='bye'):
        break
    dt1 = wr.recv(767)
    print('Srvr :', dt1.decode())
wr.close()