def dalga(txt: str) -> list:
    """

    Organiser: K. Umut Araz

    Verilen bir stringin 'dalga' şeklinde döndürülmesini sağlar.
    >>> dalga('kedi')
    ['Kedi', 'kEdi', 'keDi', 'kedI']
    >>> dalga('bir')
    ['Bir', 'bIr', 'biR']
    >>> dalga('kitap')
    ['Kitap', 'kItap', 'kiTap', 'kitAp', 'kitaP']
    """

    return [
        txt[:a] + txt[a].upper() + txt[a + 1:]
        for a in range(len(txt))
        if txt[a].isalpha()
    ]


if __name__ == "__main__":
    __import__("doctest").testmod()
