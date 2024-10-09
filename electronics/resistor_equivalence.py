# https://byjus.com/equivalent-resistance-formula/

from __future__ import annotations


def paralel_direnç(dirençler: list[float]) -> float:
    """
    Req = 1/ (1/R1 + 1/R2 + ... + 1/Rn)

    >>> paralel_direnç([3.21389, 2, 3])
    0.8737571620498019
    >>> paralel_direnç([3.21389, 2, -3])
    Traceback (most recent call last):
        ...
    ValueError: 2. sıradaki direnç negatif veya sıfır değere sahip!
    >>> paralel_direnç([3.21389, 2, 0.000])
    Traceback (most recent call last):
        ...
    ValueError: 2. sıradaki direnç negatif veya sıfır değere sahip!
    """

    ilk_toplam = 0.00
    for index, direnç in enumerate(dirençler):
        if direnç <= 0:
            msg = f"{index}. sıradaki direnç negatif veya sıfır değere sahip!"
            raise ValueError(msg)
        ilk_toplam += 1 / float(direnç)
    return 1 / ilk_toplam


def seri_direnç(dirençler: list[float]) -> float:
    """
    Req = R1 + R2 + ... + Rn

    Herhangi bir sayıda seri bağlı direnç için eşdeğer direnci hesaplayın.

    >>> seri_direnç([3.21389, 2, 3])
    8.21389
    >>> seri_direnç([3.21389, 2, -3])
    Traceback (most recent call last):
        ...
    ValueError: 2. sıradaki direnç negatif değere sahip!
    """
    toplam_r = 0.00
    for index, direnç in enumerate(dirençler):
        toplam_r += direnç
        if direnç < 0:
            msg = f"{index}. sıradaki direnç negatif değere sahip!"
            raise ValueError(msg)
    return toplam_r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
