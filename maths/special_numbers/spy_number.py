"""
== Spy Number ==
 spy number is defined as a positive integer where the
 sum of its digits equals the product of its digits.

Examples of Spy Numbers: 22,123,1124,...
https://www.scribd.com/document/895653665/Interesting-Number-Programs
"""


def is_spy_number(number: int) -> bool:
    """
    This functions takes an integer number as input.
    returns True if the number is spy.
    >>> is_spy_number(-1)
    False
    >>> is_spy_number(0)
    False
    >>> is_spy_number(22)
    True
    >>> is_spy_number(1124)
    True
    >>> is_spy_number(124)
    False
    >>> is_spy_number(5.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=5.0] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number <= 0:
        return False
    digit_sum = 0
    digit_mul = 1
    while number > 0:
        digit = number % 10
        digit_sum += digit
        digit_mul *= digit
        number //= 10
    return digit_sum == digit_mul


if __name__ == "__main__":
    import doctest

    doctest.testmod()
