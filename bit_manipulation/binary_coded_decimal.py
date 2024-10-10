def ikili_kodlu_onluk(sayi: int) -> str:
    """

    Organiser: K. Umut Araz
    
    On tabanında bir tamsayının ikili kodlu onluk (bcd) değerini bulun.
    Sayının her basamağı 4 bitlik ikili olarak temsil edilir.
    Örnek:
    >>> ikili_kodlu_onluk(-2)
    '0b0000'
    >>> ikili_kodlu_onluk(-1)
    '0b0000'
    >>> ikili_kodlu_onluk(0)
    '0b0000'
    >>> ikili_kodlu_onluk(3)
    '0b0011'
    >>> ikili_kodlu_onluk(2)
    '0b0010'
    >>> ikili_kodlu_onluk(12)
    '0b00010010'
    >>> ikili_kodlu_onluk(987)
    '0b100110000111'
    """
    return "0b" + "".join(
        str(bin(int(rakam)))[2:].zfill(4) for rakam in str(max(0, sayi))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
