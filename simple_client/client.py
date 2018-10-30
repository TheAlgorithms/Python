# client.py

import socket

HOST, PORT = '127.0.0.1', 1400

s = socket.socket(

            socket.AF_INET,     #           ADDRESS FAMILIES
                                #Name                   Purpose
                                #AF_UNIX, AF_LOCAL      Local communication
                                #AF_INET                IPv4 Internet protocols
                                #AF_INET6               IPv6 Internet protocols
                                #AF_APPLETALK           Appletalk
                                #AF_BLUETOOTH           Bluetooth


            socket.SOCK_STREAM  #           SOCKET TYPES
                                #Name           Way of Interaction
                                #SOCK_STREAM    TCP
                                #SOCK_DGRAM     UDP
)
s.connect((HOST, PORT))

s.send('Hello World'.encode('ascii'))#in UDP use sendto()
data = s.recv(1024)#in UDP use recvfrom()

s.close()#end the connection
print(repr(data.decode('ascii')))
