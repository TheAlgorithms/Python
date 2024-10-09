def ikili_arama(dizi: list, alt_sınır: int, üst_sınır: int, değer: int) -> int:
    """
    Bu fonksiyon, 1 boyutlu bir dizide ikili arama yapar ve
    değer mevcut değilse -1 döner.
    dizi: Sıralı 1 boyutlu dizi
    değer: Aranacak değer
    >>> matris = [1, 4, 7, 11, 15]
    >>> ikili_arama(matris, 0, len(matris) - 1, 1)
    0
    >>> ikili_arama(matris, 0, len(matris) - 1, 23)
    -1
    """

    r = (alt_sınır + üst_sınır) // 2
    if dizi[r] == değer:
        return r
    if alt_sınır >= üst_sınır:
        return -1
    if dizi[r] < değer:
        return ikili_arama(dizi, r + 1, üst_sınır, değer)
    else:
        return ikili_arama(dizi, alt_sınır, r - 1, değer)


def matris_ikili_arama(değer: int, matris: list) -> list:
    """
    Bu fonksiyon, 2 boyutlu bir matris üzerinde döngü yapar ve
    seçilen 1 boyutlu dizi üzerinde ikili arama yapar.
    Değer mevcut değilse [-1, -1] döner.
    değer: Aranacak değer
    matris: Sıralı 2 boyutlu matris
    >>> matris = [[1, 4, 7, 11, 15],
    ...           [2, 5, 8, 12, 19],
    ...           [3, 6, 9, 16, 22],
    ...           [10, 13, 14, 17, 24],
    ...           [18, 21, 23, 26, 30]]
    >>> hedef = 1
    >>> matris_ikili_arama(hedef, matris)
    [0, 0]
    >>> hedef = 34
    >>> matris_ikili_arama(hedef, matris)
    [-1, -1]
    """
    index = 0
    if matris[index][0] == değer:
        return [index, 0]
    while index < len(matris) and matris[index][0] < değer:
        r = ikili_arama(matris[index], 0, len(matris[index]) - 1, değer)
        if r != -1:
            return [index, r]
        index += 1
    return [-1, -1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
