def bir_onceki_iki_ussu_bul(sayi: int) -> int:
    """

    Organiser: K. Umut Araz

    Verilen bir tam sayıdan küçük veya ona eşit en büyük iki üssünü bulun.
    https://stackoverflow.com/questions/1322510

    >>> [bir_onceki_iki_ussu_bul(i) for i in range(18)]
    [0, 1, 2, 2, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 16, 16]
    >>> bir_onceki_iki_ussu_bul(-5)
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmayan bir tam sayı olmalıdır
    >>> bir_onceki_iki_ussu_bul(10.5)
    Traceback (most recent call last):
        ...
    ValueError: Girdi negatif olmayan bir tam sayı olmalıdır
    """
    if not isinstance(sayi, int) or sayi < 0:
        raise ValueError("Girdi negatif olmayan bir tam sayı olmalıdır")
    if sayi == 0:
        return 0
    us = 1
    while us <= sayi:
        us <<= 1  # 2 ile çarpmaya eşdeğer
    return us >> 1 if sayi > 1 else 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
