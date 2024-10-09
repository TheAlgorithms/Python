#!/usr/bin/env python3

"""Tek bir biti manipüle etme işlevselliği sağlayın."""


def bit_ayarla(sayi: int, konum: int) -> int:
    """
    Konumdaki biti 1 olarak ayarla.

    Detaylar: verilen sayı ve X için bit düzeyinde veya işlemi gerçekleştirin.
    X, tüm bitleri sıfır olan ve verilen konumdaki biti bir olan bir sayıdır.

    >>> bit_ayarla(0b1101, 1) # 0b1111
    15
    >>> bit_ayarla(0b0, 5) # 0b100000
    32
    >>> bit_ayarla(0b1111, 1) # 0b1111
    15
    """
    return sayi | (1 << konum)


def bit_temizle(sayi: int, konum: int) -> int:
    """
    Konumdaki biti 0 olarak ayarla.

    Detaylar: verilen sayı ve X için bit düzeyinde ve işlemi gerçekleştirin.
    X, tüm bitleri bir olan ve verilen konumdaki biti sıfır olan bir sayıdır.

    >>> bit_temizle(0b10010, 1) # 0b10000
    16
    >>> bit_temizle(0b0, 5) # 0b0
    0
    """
    return sayi & ~(1 << konum)


def bit_degistir(sayi: int, konum: int) -> int:
    """
    Konumdaki biti değiştir.

    Detaylar: verilen sayı ve X için bit düzeyinde xor işlemi gerçekleştirin.
    X, tüm bitleri sıfır olan ve verilen konumdaki biti bir olan bir sayıdır.

    >>> bit_degistir(0b101, 1) # 0b111
    7
    >>> bit_degistir(0b101, 0) # 0b100
    4
    """
    return sayi ^ (1 << konum)


def bit_ayarlimi(sayi: int, konum: int) -> bool:
    """
    Konumdaki bit ayarlı mı?

    Detaylar: Konumdaki biti en küçük bit olacak şekilde kaydırın.
    Ardından kaydırılan sayıyı 1 ile anding yaparak ilk bitin ayarlı olup olmadığını kontrol edin.

    >>> bit_ayarlimi(0b1010, 0)
    False
    >>> bit_ayarlimi(0b1010, 1)
    True
    >>> bit_ayarlimi(0b1010, 2)
    False
    >>> bit_ayarlimi(0b1010, 3)
    True
    >>> bit_ayarlimi(0b0, 17)
    False
    """
    return ((sayi >> konum) & 1) == 1


def bit_al(sayi: int, konum: int) -> int:
    """
    Verilen konumdaki biti al

    Detaylar: verilen sayı ve X için bit düzeyinde ve işlemi gerçekleştirin,
    X, tüm bitleri sıfır olan ve verilen konumdaki biti bir olan bir sayıdır.
    Sonuç sıfıra eşit değilse, verilen konumdaki bit 1'dir, aksi takdirde 0'dır.

    >>> bit_al(0b1010, 0)
    0
    >>> bit_al(0b1010, 1)
    1
    >>> bit_al(0b1010, 2)
    0
    >>> bit_al(0b1010, 3)
    1
    """
    return int((sayi & (1 << konum)) != 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
