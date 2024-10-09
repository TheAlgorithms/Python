# https://farside.ph.utexas.edu/teaching/316/lectures/node46.html

from __future__ import annotations


def paralel_kondansator(kondansatorler: list[float]) -> float:
    """
    Ceq = C1 + C2 + ... + Cn
    Herhangi bir sayıda paralel bağlı kondansatörlerin eşdeğer kapasitesini hesaplayın.
    >>> paralel_kondansator([5.71389, 12, 3])
    20.71389
    >>> paralel_kondansator([5.71389, 12, -3])
    Traceback (most recent call last):
        ...
    ValueError: 2. indeksteki kondansatör negatif bir değere sahip!
    """
    toplam_c = 0.0
    for indeks, kondansator in enumerate(kondansatorler):
        if kondansator < 0:
            msg = f"{indeks}. indeksteki kondansatör negatif bir değere sahip!"
            raise ValueError(msg)
        toplam_c += kondansator
    return toplam_c


def seri_kondansator(kondansatorler: list[float]) -> float:
    """
    Ceq = 1/ (1/C1 + 1/C2 + ... + 1/Cn)
    >>> seri_kondansator([5.71389, 12, 3])
    1.6901062252507735
    >>> seri_kondansator([5.71389, 12, -3])
    Traceback (most recent call last):
        ...
    ValueError: 2. indeksteki kondansatör negatif veya sıfır değere sahip!
    >>> seri_kondansator([5.71389, 12, 0.000])
    Traceback (most recent call last):
        ...
    ValueError: 2. indeksteki kondansatör negatif veya sıfır değere sahip!
    """

    ilk_toplam = 0.0
    for indeks, kondansator in enumerate(kondansatorler):
        if kondansator <= 0:
            msg = f"{indeks}. indeksteki kondansatör negatif veya sıfır değere sahip!"
            raise ValueError(msg)
        ilk_toplam += 1 / kondansator
    return 1 / ilk_toplam


if __name__ == "__main__":
    import doctest

    doctest.testmod()
