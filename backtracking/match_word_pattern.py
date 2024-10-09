def kelime_deseni_eşleştir(desen: str, giriş_dizesi: str) -> bool:
    """
    Geri izleme kullanarak verilen bir desenin bir dizeyle eşleşip eşleşmediğini belirleyin.

    desen: Eşleştirilecek desen.
    giriş_dizesi: Desene karşı eşleştirilecek dize.
    dönüş: Desen dizeyle eşleşirse True, aksi takdirde False döner.

    >>> kelime_deseni_eşleştir("aba", "GraphTreesGraph")
    True

    >>> kelime_deseni_eşleştir("xyx", "PythonRubyPython")
    True

    >>> kelime_deseni_eşleştir("GG", "PythonJavaPython")
    False
    """

    def geri_izleme(desen_indeksi: int, dize_indeksi: int) -> bool:
        """
        >>> geri_izleme(0, 0)
        True

        >>> geri_izleme(0, 1)
        True

        >>> geri_izleme(0, 4)
        False
        """
        if desen_indeksi == len(desen) and dize_indeksi == len(giriş_dizesi):
            return True
        if desen_indeksi == len(desen) or dize_indeksi == len(giriş_dizesi):
            return False
        karakter = desen[desen_indeksi]
        if karakter in desen_haritası:
            eşleşen_dize = desen_haritası[karakter]
            if giriş_dizesi.startswith(eşleşen_dize, dize_indeksi):
                return geri_izleme(desen_indeksi + 1, dize_indeksi + len(eşleşen_dize))
            else:
                return False
        for son in range(dize_indeksi + 1, len(giriş_dizesi) + 1):
            alt_dize = giriş_dizesi[dize_indeksi:son]
            if alt_dize in dize_haritası:
                continue
            desen_haritası[karakter] = alt_dize
            dize_haritası[alt_dize] = karakter
            if geri_izleme(desen_indeksi + 1, son):
                return True
            del desen_haritası[karakter]
            del dize_haritası[alt_dize]
        return False

    desen_haritası: dict[str, str] = {}
    dize_haritası: dict[str, str] = {}
    return geri_izleme(0, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
