"""
https://en.wikipedia.org/wiki/Computus#Gauss'_Easter_algorithm
"""
from datetime import datetime, timedelta


def gauss_easter(year: int) -> datetime:
    """
    Calculation Gregorian easter date for given year

    >>> gauss_easter(2007)
    datetime.datetime(2007, 4, 8, 0, 0)

    >>> gauss_easter(2008)
    datetime.datetime(2008, 3, 23, 0, 0)

    >>> gauss_easter(2020)
    datetime.datetime(2020, 4, 12, 0, 0)

    >>> gauss_easter(2021)
    datetime.datetime(2021, 4, 4, 0, 0)
    """
    a = year % 19
    b = year % 4
    c = year % 7
    k = year // 100
    p = (13 + 8 * k) / 25
    q = k / 4
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7
    d = (19 * a + M) % 30
    e = (2 * b + 4 * c + 6 * d + N) % 7

    if d == 29 and e == 6:
        return datetime(year, 4, 19)
    elif d == 28 and e == 6:
        return datetime(year, 4, 18)
    else:
        print(22, 22 + d + e, d + e)
        return datetime(year, 3, 22) + timedelta(days=int(d + e))

if __name__ == '__main__':
    print(gauss_easter(2021))