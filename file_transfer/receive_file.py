def receive(saveas, host='', port='', debug=False):
    import socket  # Import socket module

    sock = socket.socket()  # Create a socket object
    host = socket.gethostname() if not host else host  # Get local machine name
    port = 12312 if not port else port

    sock.connect((host, port))
    sock.send(b"Hello server!")

    with open(saveas, "wb") as out_file:
        print("File opened")
        print("Receiving data...")
        while True:
            data = sock.recv(1024)
            if debug:
                print(f"data={data}")
            if not data:
                break
            out_file.write(data)  # Write data to a file

    print("Successfully got the file")
    sock.close()
    print("Connection closed")
