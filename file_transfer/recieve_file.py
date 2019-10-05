if __name__ == "__main__":
    import socket  # Import socket module

    sock = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = 12312

    sock.connect((host, port))
    sock.send(b"Hello server!")

    with open("Received_file", "wb") as out_file:
        print("File opened")
        print("Receiving data...")
        while True:
            data = sock.recv(1024)
            print(f"data={data}")
            if not data:
                break
            out_file.write(data)  # Write data to a file

    print("Successfully got the file")
    sock.close()
    print("Connection closed")
