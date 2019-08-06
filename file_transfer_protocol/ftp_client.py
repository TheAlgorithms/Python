import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine's name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(1024) # Recieve data in chunks of 1024 bytes
        print('data=%s', (data))
        if not data: # Stop when there is no more data
            break
        f.write(data) # Write data to a file

f.close()
print('Successfully get the file')
s.close()
print('Connection closed')
