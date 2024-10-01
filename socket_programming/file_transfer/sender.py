import socket


def send_file_to_server(host, port, file_path) -> None:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    file_name = file_path.split("/")[-1]
    client_socket.send(file_name.encode())

    with open(file_path, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    print(f"File {file_name} sent successfully.")
    client_socket.close()


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345

    file_path = "file.txt"

    send_file_to_server(host, port, file_path)
