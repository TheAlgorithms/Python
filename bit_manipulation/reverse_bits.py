def ters_bit_dizisi_al(sayi: int) -> str:
    """
    bir tamsayının bit dizisini döndür

    >>> ters_bit_dizisi_al(9)
    '10010000000000000000000000000000'
    >>> ters_bit_dizisi_al(43)
    '11010100000000000000000000000000'
    >>> ters_bit_dizisi_al(2873)
    '10011100110100000000000000000000'
    >>> ters_bit_dizisi_al("bu bir sayı değil")
    Traceback (most recent call last):
        ...
    TypeError: işlem str türünde bir nesne üzerinde yapılamaz
    """
    if not isinstance(sayi, int):
        msg = (
            "işlem "
            f"{type(sayi).__name__} türünde bir nesne üzerinde yapılamaz"
        )
        raise TypeError(msg)
    bit_dizisi = ""
    for _ in range(32):
        bit_dizisi += str(sayi % 2)
        sayi = sayi >> 1
    return bit_dizisi


def bit_ters_cevir(sayi: int) -> str:
    """
    32 bitlik bir tamsayı al, bitlerini ters çevir,
    ters bitlerin bir dizisini döndür

    sağlanan tamsayı üzerinde bir bit_ters_cevir işleminin sonucu.

    >>> bit_ters_cevir(25)
    '00000000000000000000000000011001'
    >>> bit_ters_cevir(37)
    '00000000000000000000000000100101'
    >>> bit_ters_cevir(21)
    '00000000000000000000000000010101'
    >>> bit_ters_cevir(58)
    '00000000000000000000000000111010'
    >>> bit_ters_cevir(0)
    '00000000000000000000000000000000'
    >>> bit_ters_cevir(256)
    '00000000000000000000000100000000'
    >>> bit_ters_cevir(-1)
    Traceback (most recent call last):
        ...
    ValueError: giriş değeri pozitif olmalıdır

    >>> bit_ters_cevir(1.1)
    Traceback (most recent call last):
        ...
    TypeError: Giriş değeri 'int' türünde olmalıdır

    >>> bit_ters_cevir("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' str ve int türleri arasında desteklenmiyor
    """
    if sayi < 0:
        raise ValueError("giriş değeri pozitif olmalıdır")
    elif isinstance(sayi, float):
        raise TypeError("Giriş değeri 'int' türünde olmalıdır")
    elif isinstance(sayi, str):
        raise TypeError("'<' str ve int türleri arasında desteklenmiyor")
    sonuc = 0
    # 32 bitlik tamsayı ile uğraştığımız için [1'den 32'ye] kadar yineleyici
    for _ in range(1, 33):
        # bitleri bir birim sola kaydır
        sonuc = sonuc << 1
        # son biti al
        son_bit = sayi % 2
        # bitleri bir birim sağa kaydır
        sayi = sayi >> 1
        # bu biti cevaba ekle
        sonuc = sonuc | son_bit
    return ters_bit_dizisi_al(sonuc)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
