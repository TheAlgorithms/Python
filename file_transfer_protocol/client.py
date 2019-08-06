import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 12312

s.connect((host, port))
s.send(b'Hello server!')

with open('Received_file', 'wb') as f:
    print('File opened')
    print('Receiving data...')
    while True:
        data = s.recv(1024)
        print('data='+str(data))
        if not data:
            break
        # write data to a file
        f.write(data)

print('Successfully got the file')
s.close()
print('Connection closed')
