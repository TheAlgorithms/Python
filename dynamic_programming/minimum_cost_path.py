# Youtube Açıklaması: https://www.youtube.com/watch?v=lBRtnuxg-gU

from __future__ import annotations


def minimum_maliyet_yolu(matris: list[list[int]]) -> int:
    """
    Verilen bir matriste sol üstten sağ alta kadar olan tüm olası yolların izlediği minimum maliyeti bulun

    >>> minimum_maliyet_yolu([[2, 1], [3, 1], [4, 2]])
    6

    >>> minimum_maliyet_yolu([[2, 1, 4], [2, 1, 3], [3, 2, 1]])
    7
    """

    # ilk satırı ön işleme tabi tutma
    for i in range(1, len(matris[0])):
        matris[0][i] += matris[0][i - 1]

    # ilk sütunu ön işleme tabi tutma
    for i in range(1, len(matris)):
        matris[i][0] += matris[i - 1][0]

    # mevcut pozisyon için yol maliyetini güncelleme
    for i in range(1, len(matris)):
        for j in range(1, len(matris[0])):
            matris[i][j] += min(matris[i - 1][j], matris[i][j - 1])

    return matris[-1][-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
