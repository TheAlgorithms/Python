import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    filename = 'mytext.txt'
    with open(filename, 'rb') as f:
        in_data = f.read(1024)
        while in_data:
            conn.send(in_data)
            print('Sent ', repr(in_data))
            in_data = f.read(1024)

    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()
