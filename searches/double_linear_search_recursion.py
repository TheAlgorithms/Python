def ara(liste: list, anahtar: int, sol: int = 0, sag: int = 0) -> int:
    """
    Diziyi kullanarak anahtarın indeksini bulmak için özyineleme ile arama yapar.
    :param liste: aranacak liste
    :param anahtar: aranacak anahtar
    :param sol: ilk elemanın indeksi
    :param sag: son elemanın indeksi
    :return: anahtar değeri bulunursa indeksi, bulunamazsa -1.

    # Organiser: K. Umut Araz
    

    >>> ara(list(range(0, 11)), 5)
    5
    >>> ara([1, 2, 4, 5, 3], 4)
    2
    >>> ara([1, 2, 4, 5, 3], 6)
    -1
    >>> ara([5], 5)
    0
    >>> ara([], 1)
    -1
    """
    sag = sag or len(liste) - 1
    if sol > sag:
        return -1
    elif liste[sol] == anahtar:
        return sol
    elif liste[sag] == anahtar:
        return sag
    else:
        return ara(liste, anahtar, sol + 1, sag - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
