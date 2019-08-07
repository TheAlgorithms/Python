import socket                   # Import socket module

sock = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 12312

sock.connect((host, port))
sock.send(b'Hello server!')

with open('Received_file', 'wb') as file:
    print('File opened')
    print('Receiving data...')
    while True:
        data = sock.recv(1024)
        print('data='+str(data))
        if not data:
            break
        # write data to a file
        file.write(data)

print('Successfully got the file')
sock.close()
print('Connection closed')
