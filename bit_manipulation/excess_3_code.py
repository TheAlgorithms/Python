def eksik_3_kodu(sayi: int) -> str:
    """
    On tabanında bir tam sayının eksik-3 kodunu bulun.
    Ondalık bir sayının tüm basamaklarına 3 ekleyin, ardından ikili kodlanmış ondalık sayıya dönüştürün.
    https://en.wikipedia.org/wiki/Excess-3

    >>> eksik_3_kodu(0)
    '0b0011'
    >>> eksik_3_kodu(3)
    '0b0110'
    >>> eksik_3_kodu(2)
    '0b0101'
    >>> eksik_3_kodu(20)
    '0b01010011'
    >>> eksik_3_kodu(120)
    '0b010001010011'
    """
    num = ""
    for basamak in str(max(0, sayi)):
        num += str(bin(int(basamak) + 3))[2:].zfill(4)
    return "0b" + num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
