def min_yol_toplamı(ızgara: list) -> int:
    """
    Bir dizi sayının sol üst köşesinden sağ alt köşesine kadar olan yolda
    en düşük olası toplamı bul ve bu yoldaki toplamı döndür.
    >>> min_yol_toplamı([
    ...     [1, 3, 1],
    ...     [1, 5, 1],
    ...     [4, 2, 1],
    ... ])
    7

    >>> min_yol_toplamı([
    ...     [1, 0, 5, 6, 7],
    ...     [8, 9, 0, 4, 2],
    ...     [4, 4, 4, 5, 1],
    ...     [9, 6, 3, 1, 0],
    ...     [8, 4, 3, 2, 7],
    ... ])
    20



    >>> min_yol_toplamı(None)
    Traceback (most recent call last):
        ...
    TypeError: Izgara uygun bilgileri içermiyor

    >>> min_yol_toplamı([[]])
    Traceback (most recent call last):
        ...
    TypeError: Izgara uygun bilgileri içermiyor
    """

    if not ızgara or not ızgara[0]:
        raise TypeError("Izgara uygun bilgileri içermiyor")

    for hücre_n in range(1, len(ızgara[0])):
        ızgara[0][hücre_n] += ızgara[0][hücre_n - 1]
    üst_satır = ızgara[0]

    for satır_n in range(1, len(ızgara)):
        mevcut_satır = ızgara[satır_n]
        ızgara[satır_n] = satırı_doldur(mevcut_satır, üst_satır)
        üst_satır = ızgara[satır_n]

    return ızgara[-1][-1]

#Produced By K. Umut Araz


def satırı_doldur(mevcut_satır: list, üst_satır: list) -> list:
    """
    >>> satırı_doldur([2, 2, 2], [1, 2, 3])
    [3, 4, 5]
    """

    mevcut_satır[0] += üst_satır[0]
    for hücre_n in range(1, len(mevcut_satır)):
        mevcut_satır[hücre_n] += min(mevcut_satır[hücre_n - 1], üst_satır[hücre_n])

    return mevcut_satır


if __name__ == "__main__":
    import doctest

    doctest.testmod()
