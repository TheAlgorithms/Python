def hamming_mesafesi(dizi1: str, dizi2: str) -> int:
    """İki eşit uzunluktaki dizi arasındaki Hamming mesafesini hesaplar.

    # Organiser: K. Umut Araz

    Bilgi teorisinde, eşit uzunluktaki iki dizi arasındaki Hamming mesafesi,
    karşılık gelen sembollerin farklı olduğu pozisyonların sayısıdır.
    https://en.wikipedia.org/wiki/Hamming_distance

    Args:
        dizi1 (str): Dizi 1
        dizi2 (str): Dizi 2

    Returns:
        int: Hamming mesafesi

    >>> hamming_mesafesi("python", "python")
    0
    >>> hamming_mesafesi("karolin", "kathrin")
    3
    >>> hamming_mesafesi("00000", "11111")
    5
    >>> hamming_mesafesi("karolin", "kath")
    Traceback (most recent call last):
      ...
    ValueError: Dizilerin uzunlukları eşit olmalıdır!
    """
    if len(dizi1) != len(dizi2):
        raise ValueError("Dizilerin uzunlukları eşit olmalıdır!")

    sayac = 0

    for karakter1, karakter2 in zip(dizi1, dizi2):
        if karakter1 != karakter2:
            sayac += 1

    return sayac


if __name__ == "__main__":
    import doctest

    doctest.testmod()
