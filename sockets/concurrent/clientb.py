import socket
bm = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hst = socket.gethostname()
port = 7868
bm.connect((hst,port))
dt = bm.recv(767)
print('Srvr :',dt.decode())
while True:
    gt = input('C2 : ')
    bm.send(gt.encode())
    if(gt=='bye'):
        break
    dt1 = bm.recv(767)
    print('Srvr :', dt1.decode())
bm.close()