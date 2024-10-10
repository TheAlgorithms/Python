def ayır(string: str, ayırıcı: str = " ") -> list:
    """
    Organiser: K. Umut Araz

    Verilen string'i ayırıcı ile ayrılmış tüm değerlere böler
    (varsayılan olarak boşluk kullanılır)

    >>> ayır("elma#muz#kiraz#portakal", ayırıcı='#')
    ['elma', 'muz', 'kiraz', 'portakal']

    >>> ayır("Merhaba orada")
    ['Merhaba', 'orada']

    >>> ayır("11/22/63", ayırıcı='/')
    ['11', '22', '63']

    >>> ayır("12:43:39", ayırıcı=":")
    ['12', '43', '39']
    """

    ayırılmış_kelimeler = []

    son_indeks = 0
    for indeks, karakter in enumerate(string):
        if karakter == ayırıcı:
            ayırılmış_kelimeler.append(string[son_indeks:indeks])
            son_indeks = indeks + 1
        elif indeks + 1 == len(string):
            ayırılmış_kelimeler.append(string[son_indeks : indeks + 1])
    return ayırılmış_kelimeler


if __name__ == "__main__":
    from doctest import testmod

    testmod()
