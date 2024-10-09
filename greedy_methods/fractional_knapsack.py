from bisect import bisect
from itertools import accumulate

# Produced By K. Umut Araz


def kesirli_sırtçantası(değerler, ağırlıklar, kapasite, eleman_sayısı):
    """
    >>> kesirli_sırtçantası([60, 100, 120], [10, 20, 30], 50, 3)
    240.0
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6, 3], 10, 4)
    105.0
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6, 3], 8, 4)
    95.0
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6], 8, 4)
    60.0
    >>> kesirli_sırtçantası([10, 40, 30], [5, 4, 6, 3], 8, 4)
    60.0
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6, 3], 0, 4)
    0
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6, 3], 8, 0)
    95.0
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6, 3], -8, 4)
    0
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6, 3], 8, -4)
    95.0
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6, 3], 800, 4)
    130
    >>> kesirli_sırtçantası([10, 40, 30, 50], [5, 4, 6, 3], 8, 400)
    95.0
    >>> kesirli_sırtçantası("ABCD", [5, 4, 6, 3], 8, 400)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for /: 'str' and 'int'
    """

    sıralı = sorted(zip(değerler, ağırlıklar), key=lambda x: x[0] / x[1], reverse=True)
    değerler, ağırlıklar = [i[0] for i in sıralı], [i[1] for i in sıralı]
    birikimli = list(accumulate(ağırlıklar))
    k = bisect(birikimli, kapasite)
    return (
        0
        if k == 0
        else sum(değerler[:k]) + (kapasite - birikimli[k - 1]) * (değerler[k]) / (ağırlıklar[k])
        if k != eleman_sayısı
        else sum(değerler[:k])
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
