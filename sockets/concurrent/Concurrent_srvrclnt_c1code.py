import socket
jk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hst = socket.gethostname()
port = 7868
jk.connect((hst,port))
dt = jk.recv(767)
print('Srvr :',dt.decode())
while True:
    gt = input('C1 : ')
    jk.send(gt.encode())
    if(gt=='bye'):
        break
    dt1 = jk.recv(767)
    print('Srvr :', dt1.decode())
jk.close()
