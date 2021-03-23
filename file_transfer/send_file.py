def send_file(filename: str = "mytext.txt", testing: bool = False) -> None:
    import socket

    port = 12312  # Reserve a port for your service.
    sock = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    sock.bind((host, port))  # Bind to the port
    sock.listen(5)  # Now wait for client connection.

    print("Server listening....")

    while True:
        conn, addr = sock.accept()  # Establish connection with client.
        print(f"Got connection from {addr}")
        data = conn.recv(1024)
        print(f"Server received {data}")

        with open(filename, "rb") as in_file:
            data = in_file.read(1024)
            while data:
                conn.send(data)
                print(f"Sent {data!r}")
                data = in_file.read(1024)

        print("Done sending")
        conn.close()
        if testing:  # Allow the test to complete
            break

    sock.shutdown(1)
    sock.close()


if __name__ == "__main__":
    send_file()
