#!/usr/bin/env python3


def merdiven_cikma(basamak_sayisi: int) -> int:
    """
    LeetCode No.70: Climbing Stairs
    Her seferinde 1 veya 2 basamak çıkabileceğiniz bir merdivende basamak_sayisi kadar
    basamağı çıkmanın farklı yolları.

    Args:
        basamak_sayisi: merdivendeki basamak sayısı

    Returns:
        basamak_sayisi kadar basamağı çıkmanın farklı yolları

    Raises:
        AssertionError: basamak_sayisi pozitif bir tam sayı değilse

    >>> merdiven_cikma(3)
    3
    >>> merdiven_cikma(1)
    1
    >>> merdiven_cikma(-7)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    AssertionError: basamak_sayisi pozitif bir tam sayı olmalı, girdiniz -7
    """
    assert (
        isinstance(basamak_sayisi, int) and basamak_sayisi > 0
    ), f"basamak_sayisi pozitif bir tam sayı olmalı, girdiniz {basamak_sayisi}"
    if basamak_sayisi == 1:
        return 1
    onceki, simdiki = 1, 1
    for _ in range(basamak_sayisi - 1):
        simdiki, onceki = simdiki + onceki, simdiki
    return simdiki


if __name__ == "__main__":
    import doctest

    doctest.testmod()
