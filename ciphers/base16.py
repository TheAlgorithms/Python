def base16_encode(data: bytes) -> str:
    """
    Verilen baytları base16 formatına kodlar.

    Organiser: K. Umut Araz

    >>> base16_encode(b'Hello World!')
    '48656C6C6F20576F726C6421'
    >>> base16_encode(b'HELLO WORLD!')
    '48454C4C4F20574F524C4421'
    >>> base16_encode(b'')
    ''
    """
    # Veriyi bir tam sayı listesine (her tam sayı bir bayt) dönüştür,
    # Ardından her baytı onaltılık temsilini al, büyük harf yap ve
    # hepsini birleştirip geri döndür.
    return "".join([hex(byte)[2:].zfill(2).upper() for byte in data])


def base16_decode(data: str) -> bytes:
    """
    Verilen base16 kodlu veriyi baytlara çözer.

    >>> base16_decode('48656C6C6F20576F726C6421')
    b'Hello World!'
    >>> base16_decode('48454C4C4F20574F524C4421')
    b'HELLO WORLD!'
    >>> base16_decode('')
    b''
    >>> base16_decode('486')
    Traceback (most recent call last):
      ...
    ValueError: Base16 kodlu veri geçersiz:
    Veri, çift sayıda onaltılık basamağa sahip değil.
    >>> base16_decode('48656c6c6f20576f726c6421')
    Traceback (most recent call last):
      ...
    ValueError: Base16 kodlu veri geçersiz:
    Veri büyük harf onaltılık değil veya geçersiz karakterler içeriyor.
    >>> base16_decode('This is not base64 encoded data.')
    Traceback (most recent call last):
      ...
    ValueError: Base16 kodlu veri geçersiz:
    Veri büyük harf onaltılık değil veya geçersiz karakterler içeriyor.
    """
    # Veri geçerliliğini kontrol et, RFC3548'e göre
    # https://www.ietf.org/rfc/rfc3548.txt
    if (len(data) % 2) != 0:
        raise ValueError(
            """Base16 kodlu veri geçersiz:
Veri, çift sayıda onaltılık basamağa sahip değil."""
        )
    # Karakter setini kontrol et - standart base16 alfabesi
    # RFC3548 bölüm 6'ya göre büyük harf olmalıdır.
    if not set(data) <= set("0123456789ABCDEF"):
        raise ValueError(
            """Base16 kodlu veri geçersiz:
Veri büyük harf onaltılık değil veya geçersiz karakterler içeriyor."""
        )
    # Her iki onaltılık basamağı (= bir bayt) bir tam sayıya dönüştür.
    # Ardından, sonucu baytlara birleştirip geri döndür.
    return bytes(int(data[i] + data[i + 1], 16) for i in range(0, len(data), 2))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
