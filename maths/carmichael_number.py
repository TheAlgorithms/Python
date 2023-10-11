"""
== Carmichael Numbers ==
A number n is said to be a Carmichael number if it
satisfies the following modular arithmetic condition:

    power(b, n-1) MOD n = 1,
    for all b ranging from 1 to n such that b and
    n are relatively prime, i.e, gcd(b, n) = 1

Examples of Carmichael Numbers: 561, 1105, ...
https://en.wikipedia.org/wiki/Carmichael_number
"""

from maths.greatest_common_divisor import greatest_common_divisor


def power(x: int, y: int, mod: int) -> int:
    """

    Examples:
    >>> power(2, 15, 3)
    2

    >>> power(5, 1, 30)
    5
    """

    if y == 0:
        return 1
    temp = power(x, y // 2, mod) % mod
    temp = (temp * temp) % mod
    if y % 2 == 1:
        temp = (temp * x) % mod
    return temp


def is_carmichael_number(n: int) -> bool:
    """

    Examples:
    >>> is_carmichael_number(562)
    False

    >>> is_carmichael_number(561)
    True

    >>> is_carmichael_number(5.1)
    Traceback (most recent call last):
         ...
    ValueError: Number 5.1 must instead be a positive integer

    >>> is_carmichael_number(-7)
    Traceback (most recent call last):
         ...
    ValueError: Number -7 must instead be a positive integer

    >>> is_carmichael_number(0)
    Traceback (most recent call last):
         ...
    ValueError: Number 0 must instead be a positive integer
    """

    if n <= 0 or not isinstance(n, int):
        msg = f"Number {n} must instead be a positive integer"
        raise ValueError(msg)

    return all(
        power(b, n - 1, n) == 1
        for b in range(2, n)
        if greatest_common_divisor(b, n) == 1
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    number = int(input("Enter number: ").strip())
    if is_carmichael_number(number):
        print(f"{number} is a Carmichael Number.")
    else:
        print(f"{number} is not a Carmichael Number.")
