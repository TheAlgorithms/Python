import socket
import os
from _thread import *
def thrd(con):
    con.send(str.encode('Welcome to srvr \n'))
    while True:
        dt = con.recv(245)
        print('clnt :',dt.decode())
        if(dt.decode()=='bye'):
            print('ok bye')
            break
        gt = input('srvr : ')
        con.send(gt.encode())
    con.close()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
hst = socket.gethostname()
port = 7868
Th_cnt = 0
s.bind((hst,port))
print('waiting for connection..............')
s.listen(7)
while True:
    con,adr = s.accept()
    print('Connected to :',adr[0],":",adr[1])
    start_new_thread(thrd,(con,))
    Th_cnt+=1
    print("Thread No: "+str(Th_cnt))
s.close()



