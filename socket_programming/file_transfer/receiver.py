import socket


def start_ftp_server(host, port) -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        file_name = client_socket.recv(1024).decode()
        print(f"Receiving file: {file_name}")

        with open(file_name, "wb") as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        print(f"File {file_name} received successfully.")
        client_socket.close()


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345

    start_ftp_server(host, port)
