def bitleri_goster(oncesi: int, sonrasi: int) -> str:
    """
    Organiser: K. Umut Araz 
    
    >>> print(bitleri_goster(0, 0xFFFF))
        0: 00000000
    65535: 1111111111111111
    """
    return f"{oncesi:>5}: {oncesi:08b}\n{sonrasi:>5}: {sonrasi:08b}"


def tek_cift_bitleri_degistir(sayi: int) -> int:
    """
    1. Bit düzeyinde VE işlemleri kullanarak giriş sayısındaki çift bitleri (0, 2, 4, 6, vb.)
       ve tek bitleri (1, 3, 5, 7, vb.) ayırırız.
    2. Daha sonra çift bitleri 1 pozisyon sağa kaydırır ve tek bitleri 1 pozisyon sola kaydırarak
       onları değiştiririz.
    3. Son olarak, değiştirilen çift ve tek bitleri bit düzeyinde VEYA işlemi kullanarak birleştiririz
       ve nihai sonucu elde ederiz.
    >>> print(bitleri_goster(0, tek_cift_bitleri_degistir(0)))
        0: 00000000
        0: 00000000
    >>> print(bitleri_goster(1, tek_cift_bitleri_degistir(1)))
        1: 00000001
        2: 00000010
    >>> print(bitleri_goster(2, tek_cift_bitleri_degistir(2)))
        2: 00000010
        1: 00000001
    >>> print(bitleri_goster(3, tek_cift_bitleri_degistir(3)))
        3: 00000011
        3: 00000011
    >>> print(bitleri_goster(4, tek_cift_bitleri_degistir(4)))
        4: 00000100
        8: 00001000
    >>> print(bitleri_goster(5, tek_cift_bitleri_degistir(5)))
        5: 00000101
       10: 00001010
    >>> print(bitleri_goster(6, tek_cift_bitleri_degistir(6)))
        6: 00000110
        9: 00001001
    >>> print(bitleri_goster(23, tek_cift_bitleri_degistir(23)))
       23: 00010111
       43: 00101011
    """
    # Tüm çift bitleri al - 0xAAAAAAAA, tüm çift bitleri 1 olan 32 bitlik bir sayıdır
    cift_bitler = sayi & 0xAAAAAAAA

    # Tüm tek bitleri al - 0x55555555, tüm tek bitleri 1 olan 32 bitlik bir sayıdır
    tek_bitler = sayi & 0x55555555

    # Çift bitleri sağa kaydır ve tek bitleri sola kaydır ve değiştir
    return cift_bitler >> 1 | tek_bitler << 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    for i in (-1, 0, 1, 2, 3, 4, 23, 24):
        print(bitleri_goster(i, tek_cift_bitleri_degistir(i)), "\n")
