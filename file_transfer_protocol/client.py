import socket                   # Import socket module

sock = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 12312

sock.connect((host, port))
sock.send(b'Hello server!')

with open('Received_file', 'wb') as in_file:
    print('File opened')
    print('Receiving data...')
    while True:
        data = sock.recv(1024)
        print(f"data={data}")
        if not data:
            break
        # write data to a file
        in_file.write(data)

print('Successfully got the file')
sock.close()
print('Connection closed')
