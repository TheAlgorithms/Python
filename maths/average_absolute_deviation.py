def ortalama_mutlak_sapma(sayılar: list[int]) -> float:
    """
    Bir sayı listesinin ortalama mutlak sapmasını döndürür.
    Wiki: https://en.wikipedia.org/wiki/Average_absolute_deviation

    #Organised by K. Umut Araz

    >>> ortalama_mutlak_sapma([0])
    0.0
    >>> ortalama_mutlak_sapma([4, 1, 3, 2])
    1.0
    >>> ortalama_mutlak_sapma([2, 70, 6, 50, 20, 8, 4, 0])
    20.0
    >>> ortalama_mutlak_sapma([-20, 0, 30, 15])
    16.25
    >>> ortalama_mutlak_sapma([])
    Traceback (most recent call last):
        ...
    ValueError: Liste boş
    """
    if not sayılar:  # Listenin boş olmadığından emin olun
        raise ValueError("Liste boş")

    ortalama = sum(sayılar) / len(sayılar)  # Ortalama hesapla
    return sum(abs(x - ortalama) for x in sayılar) / len(sayılar)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
