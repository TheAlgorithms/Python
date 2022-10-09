import socket
serverName = '127.0.0.1'
port = 5006
clientsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tup = (serverName,port)
clientsock.connect(tup)
input_file = input("Request a binary file name")
clientsock.send(input_file.encode())
output = clientsock.recv(2048)
print("Recieving File:",output)
file = open("requested_file.bin",'w')
file.write(clientsock.recv(2048).decode())
clientsock.close()
