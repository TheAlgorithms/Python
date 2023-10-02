# it is a basic port scanner written in python


import socket ,datetime ,threading

host = socket.gethostbyname(input("enter the ip:"))
start = 1
end = 65535


def scan(i):
    ts = datetime.datetime.now()
    # print(ts, ">>> scanning port:", i)
    s = socket.socket()
    s.settimeout(4)
    result = s.connect_ex((host, i))
    if result == 0:
        print(i," port open")
    # else:
    #     print(i, " port is close\n")
    s.close()

for i in range(start, end+1):
    t = threading.Thread(target=scan,args=(i, ))
    t.start()