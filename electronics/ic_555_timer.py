from __future__ import annotations

"""
    Kararsız 555 zamanlayıcısının frekansını ve/veya görev döngüsünü hesaplayın.
    * https://en.wikipedia.org/wiki/555_timer_IC#Astable

    Bu fonksiyonlar, harici dirençlerin (ohm cinsinden) ve kapasitansın (mikrofarad cinsinden) değerini alır ve aşağıdakileri hesaplar:

    -------------------------------------
    | Frekans = 1.44 /[( R1+ 2 x R2) x C1] |               ... Hz cinsinden
    -------------------------------------
    burada Frekans frekansı,
          R1 birinci direnç ohm cinsinden,
          R2 ikinci direnç ohm cinsinden,
          C1 kapasitans mikrofarad cinsindendir.

    ------------------------------------------------
    | Görev Döngüsü = (R1 + R2) / (R1 + 2 x R2) x 100 |    ... % cinsinden
    ------------------------------------------------
    burada R1 birinci direnç ohm cinsinden,
          R2 ikinci direnç ohm cinsindendir.
"""


def kararsız_frekans(
    direnç_1: float, direnç_2: float, kapasitans: float
) -> float:
    """
    Kullanım örnekleri:
    >>> kararsız_frekans(direnç_1=45, direnç_2=45, kapasitans=7)
    1523.8095238095239
    >>> kararsız_frekans(direnç_1=356, direnç_2=234, kapasitans=976)
    1.7905459175553078
    >>> kararsız_frekans(direnç_1=2, direnç_2=-1, kapasitans=2)
    Traceback (most recent call last):
        ...
    ValueError: Tüm değerler pozitif olmalıdır
    >>> kararsız_frekans(direnç_1=45, direnç_2=45, kapasitans=0)
    Traceback (most recent call last):
        ...
    ValueError: Tüm değerler pozitif olmalıdır
    """

    if direnç_1 <= 0 or direnç_2 <= 0 or kapasitans <= 0:
        raise ValueError("Tüm değerler pozitif olmalıdır")
    return (1.44 / ((direnç_1 + 2 * direnç_2) * kapasitans)) * 10**6


def kararsız_görev_döngüsü(direnç_1: float, direnç_2: float) -> float:
    """
    Kullanım örnekleri:
    >>> kararsız_görev_döngüsü(direnç_1=45, direnç_2=45)
    66.66666666666666
    >>> kararsız_görev_döngüsü(direnç_1=356, direnç_2=234)
    71.60194174757282
    >>> kararsız_görev_döngüsü(direnç_1=2, direnç_2=-1)
    Traceback (most recent call last):
        ...
    ValueError: Tüm değerler pozitif olmalıdır
    >>> kararsız_görev_döngüsü(direnç_1=0, direnç_2=0)
    Traceback (most recent call last):
        ...
    ValueError: Tüm değerler pozitif olmalıdır
    """

    if direnç_1 <= 0 or direnç_2 <= 0:
        raise ValueError("Tüm değerler pozitif olmalıdır")
    return (direnç_1 + direnç_2) / (direnç_1 + 2 * direnç_2) * 100


if __name__ == "__main__":
    import doctest

    doctest.testmod()
