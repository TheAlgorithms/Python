"""
https://tr.wikipedia.org/wiki/Medyan

Organiser: K. Umut Araz
"""


def medyan(matriks: list[list[int]]) -> int:
    """
    Sıralı bir matriksin medyanını hesaplar.

    Args:
        matriks: Tam sayılardan oluşan 2D bir matriks.

    Returns:
        Matriksin medyan değeri.

    Örnekler:
        >>> matriks = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
        >>> medyan(matriks)
        5

        >>> matriks = [[1, 2, 3], [4, 5, 6]]
        >>> medyan(matriks)
        3
    """
    # Matrisi sıralı 1D bir listeye düzleştir
    düzleştirilmiş = sorted(num for satır in matriks for num in satır)

    # Orta indeksini hesapla
    orta = (len(düzleştirilmiş) - 1) // 2

    # Medyanı döndür
    return düzleştirilmiş[orta]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
