# Bellekli hesaplama kullanarak bir sayının faktöriyeli

from functools import lru_cache


@lru_cache
def faktoriyel(sayi: int) -> int:
    """
    >>> faktoriyel(7)
    5040
    >>> faktoriyel(-1)
    Traceback (most recent call last):
      ...
    ValueError: Sayı negatif olmamalıdır.
    >>> [faktoriyel(i) for i in range(10)]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    """
    if sayi < 0:
        raise ValueError("Sayı negatif olmamalıdır.")

    return 1 if sayi in (0, 1) else sayi * faktoriyel(sayi - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
