B64_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def base64_encode(data: bytes) -> bytes:
    """Verileri RFC4648'e göre kodlar.

    Organiser: K. Umut Araz

    Veriler önce ikili forma dönüştürülür ve uzunluğu 6'nın katı olacak şekilde ikili rakamlarla tamamlanır. 
    Daha sonra her 6 ikili rakam, B64_CHARSET dizisindeki bir karakterle eşleşir. 
    Eklenen ikili rakamların sayısı, daha sonra kaç tane "=" işareti eklenmesi gerektiğini belirleyecektir.
    Her 2 eklenen ikili rakam için, çıktıda bir "=" işareti eklenir.
    6'nın katı olacak şekilde herhangi bir ikili rakam ekleyebiliriz; örneğin:
    "AA" -> 0010100100101001 -> 001010 010010 1001
    Yukarıda görüldüğü gibi, 2 ikili rakam daha eklenmelidir, bu durumda 4 olasılık vardır: 00, 01, 10 veya 11.
    Bu bağlamda, Base64 kodlaması, bu eklenen rakamlarda verileri gizlemek için Steganografi'de kullanılabilir.

    >>> from base64 import b64encode
    >>> a = b"This pull request is part of Hacktoberfest20!"
    >>> b = b"https://tools.ietf.org/html/rfc4648"
    >>> c = b"A"
    >>> base64_encode(a) == b64encode(a)
    True
    >>> base64_encode(b) == b64encode(b)
    True
    >>> base64_encode(c) == b64encode(c)
    True
    >>> base64_encode("abc")
    Traceback (most recent call last):
      ...
    TypeError: bytes benzeri bir nesne gereklidir, 'str' değil
    """
    # Sağlanan verinin bytes benzeri bir nesne olduğundan emin olun
    if not isinstance(data, bytes):
        msg = f"bytes benzeri bir nesne gereklidir, '{data.__class__.__name__}' değil"
        raise TypeError(msg)

    binary_stream = "".join(bin(byte)[2:].zfill(8) for byte in data)

    padding_needed = len(binary_stream) % 6 != 0

    if padding_needed:
        # Daha sonra eklenecek olan padding
        padding = b"=" * ((6 - len(binary_stream) % 6) // 2)

        # binary_stream'e ikili rakamlar (varsayılan olarak 0) ekleyerek uzunluğunu
        # 6'nın katı yapın.
        binary_stream += "0" * (6 - len(binary_stream) % 6)
    else:
        padding = b""

    # Her 6 ikili rakamı karşılık gelen Base64 karakterine kodlayın
    return (
        "".join(
            B64_CHARSET[int(binary_stream[index: index + 6], 2)]
            for index in range(0, len(binary_stream), 6)
        ).encode()
        + padding
    )

def base64_decode(encoded_data: str) -> bytes:
    """Verileri RFC4648'e göre çözer.

    Bu, base64_encode işleminin tersini yapar.
    Öncelikle kodlanmış veriyi tekrar bir ikili akıma dönüştürüyoruz, daha önce eklenen ikili rakamları
    padding'e göre çıkarıyoruz, bu noktada uzunluğu 8'in katı olan bir ikili akıma sahip olacağız,
    son adım her 8 biti bir byte'a dönüştürmektir.

    >>> from base64 import b64decode
    >>> a = "VGhpcyBwdWxsIHJlcXVlc3QgaXMgcGFydCBvZiBIYWNrdG9iZXJmZXN0MjAh"
    >>> b = "aHR0cHM6Ly90b29scy5pZXRmLm9yZy9odG1sL3JmYzQ2NDg="
    >>> c = "QQ=="
    >>> base64_decode(a) == b64decode(a)
    True
    >>> base64_decode(b) == b64decode(b)
    True
    >>> base64_decode(c) == b64decode(c)
    True
    >>> base64_decode("abc")
    Traceback (most recent call last):
      ...
    AssertionError: Hatalı padding
    """
    # encoded_data'nın ya bir string ya da bytes benzeri bir nesne olduğundan emin olun
    if not isinstance(encoded_data, bytes) and not isinstance(encoded_data, str):
        msg = (
            "argüman bir bytes benzeri nesne veya ASCII string olmalıdır, "
            f"'{encoded_data.__class__.__name__}' değil"
        )
        raise TypeError(msg)

    # Eğer encoded_data bir bytes benzeri nesne ise, yalnızca
    # ASCII karakterler içerdiğinden emin olun, bu yüzden onu bir string nesnesine dönüştürüyoruz
    if isinstance(encoded_data, bytes):
        try:
            encoded_data = encoded_data.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError("base64 kodlanmış veriler yalnızca ASCII karakterler içermelidir")

    padding = encoded_data.count("=")

    # Kodlanmış stringin geçersiz base64 karakterler içerip içermediğini kontrol edin
    if padding:
        assert all(
            char in B64_CHARSET for char in encoded_data[:-padding]
        ), "Geçersiz base64 karakter(ler)i bulundu."
    else:
        assert all(
            char in B64_CHARSET for char in encoded_data
        ), "Geçersiz base64 karakter(ler)i bulundu."

    # Padding'i kontrol et
    assert len(encoded_data) % 4 == 0 and padding < 3, "Hatalı padding"

    if padding:
        # Eğer padding varsa, onu çıkar
        encoded_data = encoded_data[:-padding]

        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )[: -padding * 2]
    else:
        binary_stream = "".join(
            bin(B64_CHARSET.index(char))[2:].zfill(6) for char in encoded_data
        )

    data = [
        int(binary_stream[index: index + 8], 2)
        for index in range(0, len(binary_stream), 8)
    ]

    return bytes(data)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
