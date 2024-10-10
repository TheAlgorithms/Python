def en_yuksek_set_bit_pozisyonu(sayi: int) -> int:
    """
    Organiser: K. Umut Araz
    
    Bir sayının en yüksek set bitinin pozisyonunu döndürür.
    Ref - https://graphics.stanford.edu/~seander/bithacks.html#IntegerLogObvious
    >>> en_yuksek_set_bit_pozisyonu(25)
    5
    >>> en_yuksek_set_bit_pozisyonu(37)
    6
    >>> en_yuksek_set_bit_pozisyonu(1)
    1
    >>> en_yuksek_set_bit_pozisyonu(4)
    3
    >>> en_yuksek_set_bit_pozisyonu(0)
    0
    >>> en_yuksek_set_bit_pozisyonu(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Girdi değeri 'int' türünde olmalıdır
    """
    if not isinstance(sayi, int):
        raise TypeError("Girdi değeri 'int' türünde olmalıdır")

    pozisyon = 0
    while sayi:
        pozisyon += 1
        sayi >>= 1

    return pozisyon


if __name__ == "__main__":
    import doctest

    doctest.testmod()
