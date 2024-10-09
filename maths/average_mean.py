from __future__ import annotations


def ortalama(sayılar: list[int]) -> float:
    """
    Bir sayı listesinin ortalamasını bulur.
    Wiki: https://en.wikipedia.org/wiki/Mean

    >>> ortalama([3, 6, 9, 12, 15, 18, 21])
    12.0
    >>> ortalama([5, 10, 15, 20, 25, 30, 35])
    20.0
    >>> ortalama([1, 2, 3, 4, 5, 6, 7, 8])
    4.5
    >>> ortalama([])
    Traceback (most recent call last):
        ...
    ValueError: Liste boş
    """
    if not sayılar:
        raise ValueError("Liste boş")
    return sum(sayılar) / len(sayılar)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
