import json
import socket


def request(
    sock: socket.socket, req_type: str, endpoint: str, headers: list[str], body: str
):
    """
    Request HTTP connection

    :param sock: socket client
    :param req_type: request type (ex: GET, POST)
    :param endpoint: endpoint
    :param headers: http headers
    :param body: http body
    :return:
    """
    if body:
        headers.append(f"Content-Length: {len(body)}")
    headers_serialized = "\n".join(headers)
    host, _ = sock.getsockname()
    data = (
        f"{req_type} {endpoint} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"{headers_serialized}\r\n\r\n"
        f"{body}"
    )

    print(f"\n<<<< SEND <<<<\n{data}")
    sock.send(bytes(data, "iso-8859-1"))


def request_json_data(sock: socket.socket, body: str):
    """
    Request json style data

    :param sock: socket client
    :param body: json encoded string
    :return:
    """
    headers = [
        "Content-Type: application/json",
    ]
    request(sock, req_type="POST", endpoint="/", headers=headers, body=body)


def response(sock: socket.socket):
    """
    Print received data

    :param sock: socket client
    :return:
    """
    res = sock.recv(1024)
    print(f"\n>>>> RECV >>>>\n{res.decode()}")


def main():
    host = "example.com"
    port = 80

    sock = socket.socket()
    sock.connect((host, port))
    request_json_data(sock, json.dumps({"key": "value"}))
    response(sock)


if __name__ == "__main__":
    main()
