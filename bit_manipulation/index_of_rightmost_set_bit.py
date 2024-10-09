# Referans: https://www.geeksforgeeks.org/position-of-rightmost-set-bit/


def en_sagdaki_ayarlanmis_bit_indeksi(sayi: int) -> int:
    """
    Pozitif bir tamsayı 'sayi' alır.
    Bu 'sayi'daki sağdan ilk ayarlanmış bitin sıfır tabanlı indeksini döndürür.
    Ayarlanmış bit bulunamazsa -1 döndürür.

    >>> en_sagdaki_ayarlanmis_bit_indeksi(0)
    -1
    >>> en_sagdaki_ayarlanmis_bit_indeksi(5)
    0
    >>> en_sagdaki_ayarlanmis_bit_indeksi(36)
    2
    >>> en_sagdaki_ayarlanmis_bit_indeksi(8)
    3
    >>> en_sagdaki_ayarlanmis_bit_indeksi(-18)
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmayan bir tamsayı olmalıdır
    >>> en_sagdaki_ayarlanmis_bit_indeksi('test')
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmayan bir tamsayı olmalıdır
    >>> en_sagdaki_ayarlanmis_bit_indeksi(1.25)
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmayan bir tamsayı olmalıdır
    """

    if not isinstance(sayi, int) or sayi < 0:
        raise ValueError("Girdi negatif olmayan bir tamsayı olmalıdır")

    ara_deger = sayi & ~(sayi - 1)
    indeks = 0
    while ara_deger:
        ara_deger >>= 1
        indeks += 1
    return indeks - 1


if __name__ == "__main__":
    """
    En sağdaki ayarlanmış bitin indeksini bulmak, özellikle pozitif tamsayılar
    listesindeki eksik veya/veya tekrarlayan sayıları bulmada çok özel kullanım
    durumlarına sahiptir.
    """
    import doctest

    doctest.testmod(verbose=True)
