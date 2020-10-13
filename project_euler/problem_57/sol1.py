"""
Problem 57: Square root convergents
It is possible to show that the square root of two can be expressed as an infinite
continued fraction.

sqrt(2) = 1 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))

By expanding this for the first four iterations, we get:
1 + 1 / 2 = 3 / 2 = 1.5
1 + 1 / (2 + 1 / 2} = 7 / 5 = 1.4
1 + 1 / (2 + 1 / (2 + 1 / 2)) = 17 / 12 = 1.41666...
1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / 2))) = 41/ 29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion,
1393/985, is the first example where the number of digits in the numerator exceeds
the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with
more digits than the denominator?
"""


def solution(n: int = 1000) -> int:
    """
    returns number of fractions containing a numerator with more digits than
    the denominator in the first n expansions.
    >>> solution(14)
    2
    >>> solution(100)
    15
    >>> solution(10000)
    1508
    """
    a, b = 1, 1
    res = []
    for i in range(1, n + 1):
        numerator = a + 2 * b
        denominator = a + b
        if len(str(numerator)) > len(str(denominator)):
            res.append(i)
        a = numerator
        b = denominator

    return len(res)


if __name__ == "__main__":
    print(f"{solution(10000) = }")
