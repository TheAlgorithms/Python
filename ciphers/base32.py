"""
Base32 kodlama ve çözme

https://en.wikipedia.org/wiki/Base32

Organiser: K. Umut Araz
"""

B32_CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"


def base32_kodla(data: bytes) -> bytes:
    """
    >>> base32_kodla(b"Merhaba Dünya!")
    b'JBSWY3DPEBLW64TMMQQQ===='
    >>> base32_kodla(b"123456")
    b'GEZDGNBVGY======'
    >>> base32_kodla(b"uzun karmaşık bir dize")
    b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY='
    """
    binary_data = "".join(bin(ord(d))[2:].zfill(8) for d in data.decode("utf-8"))
    binary_data = binary_data.ljust(5 * ((len(binary_data) // 5) + 1), "0")
    b32_parçalar = map("".join, zip(*[iter(binary_data)] * 5))
    b32_sonuc = "".join(B32_CHARSET[int(parça, 2)] for parça in b32_parçalar)
    return bytes(b32_sonuc.ljust(8 * ((len(b32_sonuc) // 8) + 1), "="), "utf-8")


def base32_çöz(data: bytes) -> bytes:
    """
    >>> base32_çöz(b'JBSWY3DPEBLW64TMMQQQ====')
    b'Merhaba Dünya!'
    >>> base32_çöz(b'GEZDGNBVGY======')
    b'123456'
    >>> base32_çöz(b'ONXW2ZJANRXW4ZZAMNXW24DMMV4CA43UOJUW4ZY=')
    b'uzun karmaşık bir dize'
    """
    binary_parçalar = "".join(
        bin(B32_CHARSET.index(_d))[2:].zfill(5)
        for _d in data.decode("utf-8").strip("=")
    )
    binary_data = list(map("".join, zip(*[iter(binary_parçalar)] * 8)))
    return bytes("".join([chr(int(_d, 2)) for _d in binary_data]), "utf-8")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
