import socket                   # Import socket module

ONE_CONNECTION_ONLY = True      # Set this to False if you wish to continuously accept connections

port = 12312                    # Reserve a port for your service.
sock = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
sock.bind((host, port))            # Bind to the port
sock.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = sock.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='mytext.txt'
    out_file = open(filename,'rb')
    data = out_file.read(1024)
    while (data):
       conn.send(data)
       print('Sent ',repr(data))
       data = out_file.read(1024)
    out_file.close()

    print('Done sending')
    conn.send(b'Thank you for connecting')
    conn.close()
    if ONE_CONNECTION_ONLY:  # This is to make sure that the program doesn't hang while testing
        break
sock.shutdown(1)
sock.close()
