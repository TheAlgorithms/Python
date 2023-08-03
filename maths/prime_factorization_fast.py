from math import ceil, sqrt
from __future__ import annotations


def primeproduct(n: int, x: list = []):
    """
    >>> primeproduct(868)
    [2, 2, 7, 31]
    >>> primeproduct(9039423423423743)
    [2, 2, 7, 31, 719, 12572216166097]
    >>> primeproduct(0.02)
    []
    """
    if n < 1:
        return []

    if n > 1:
        if len(x) >= 1 and x[-1] % n == 0:  # check in already factorised
            x.append(x[-1])
            n = n // x[-1]

        else:
            sq = ceil(sqrt(n))
            flag = 0

            if x != []:
                for i in range(x[-1], sq + 1, 2):
                    if n % i == 0:
                        n = n // i
                        x.append(i)
                        flag = 1
                        break

            else:
                # Handle factor 2 separately
                while n % 2 == 0:  # only 2 is even prime
                    n = n // 2
                    x.append(2)

                # Start loop from 3 and increment by 2
                for i in range(3, sq + 1, 2):  # skip even numbers
                    if n % i == 0:
                        n = n // i
                        x.append(i)
                        flag = 1
                        break

            if not flag:
                x.append(n)
                n = 1

        return primeproduct(n, x)

    return x


# faster than https://github.com/sourabhkv/Python/blob/master/maths/prime_factors.py approx 2x
if __name__ == "__main__":
    import doctest

    doctest.testmod()
