from __future__ import annotations
from math import ceil, sqrt


def primeproduct(num: int) -> list[int]:
    """
    >>> primeproduct(868)
    [2, 2, 7, 31]
    >>> primeproduct(9039423423423743)
    [2, 2, 7, 31, 719, 12572216166097]
    >>> primeproduct(0.02)
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: '0.02'
    >>> primeproduct(-2342)
    []
    """

    if num <= 1:
        return []

    prime_factors: list[int] = []
    while num > 1:
        if len(prime_factors) >= 1 and prime_factors[-1] % num == 0:
            prime_factors.append(prime_factors[-1])

        else:
            sq = ceil(sqrt(num))
            flag = 0

            if prime_factors != []:
                for i in range(prime_factors[-1], sq + 1, 2):
                    if num % i == 0:
                        num = num // i
                        prime_factors.append(i)
                        flag = 1
                        break

            else:
                while num % 2 == 0:
                    num = num // 2
                    prime_factors.append(2)

                for i in range(3, sq + 1, 2):
                    if num % i == 0:
                        num = num // i
                        prime_factors.append(i)
                        flag = 1
                        break

            if not flag and num > 1:
                prime_factors.append(num)
                num = 1
                break

    return prime_factors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
