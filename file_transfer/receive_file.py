import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12312

    sock.connect((host, port))
    sock.send(b"Merhaba sunucu!")

    with open("Alinan_dosya", "wb") as out_file:
        print("Dosya açıldı")
        print("Veri alınıyor...")
        while True:
            data = sock.recv(1024)
            if not data:
                break
            out_file.write(data)

    print("Dosya başarıyla alındı")
    sock.close()
    print("Bağlantı kapatıldı")


if __name__ == "__main__":
    main()
