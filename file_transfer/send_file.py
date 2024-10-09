def dosya_gonder(dosya_adi: str = "mytext.txt", test: bool = False) -> None:
    import socket

    port = 12312  # Servisiniz için bir port ayırın.
    sock = socket.socket()  # Bir soket nesnesi oluşturun
    host = socket.gethostname()  # Yerel makine adını alın
    sock.bind((host, port))  # Porta bağlanın
    sock.listen(5)  # Şimdi istemci bağlantısını bekleyin.

    print("Sunucu dinliyor....")

    while True:
        conn, addr = sock.accept()  # İstemci ile bağlantı kurun.
        print(f"{addr} adresinden bağlantı alındı")
        data = conn.recv(1024)
        print(f"Sunucu aldı: {data = }")

        with open(dosya_adi, "rb") as in_file:
            data = in_file.read(1024)
            while data:
                conn.send(data)
                print(f"Gönderilen {data!r}")
                data = in_file.read(1024)

        print("Gönderim tamamlandı")
        conn.close()
        if test:  # Testin tamamlanmasına izin ver
            break

    sock.shutdown(1)
    sock.close()


if __name__ == "__main__":
    dosya_gonder()
