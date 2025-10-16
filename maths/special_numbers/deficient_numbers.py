"""
A number n is said to be a Deficient number if
the sum of its proper divisors is less than the number itself.

Examples of Deficient Numbers: 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, ...
"""


def is_deficient_number(number: int) -> bool:
    """
    This function takes an integer number as input.
    Returns True if the number is a deficient number.

    >>> is_deficient_number(-1)
    False
    >>> is_deficient_number(0)
    False
    >>> is_deficient_number(1)
    True
    >>> is_deficient_number(2)
    True
    >>> is_deficient_number(6)
    False
    >>> is_deficient_number(12)
    False
    >>> is_deficient_number(7)
    True
    >>> is_deficient_number(28)
    False
    >>> is_deficient_number(15)
    True
    >>> is_deficient_number(8.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=8.0] must be an integer
    """

    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        return False

    divisor_sum = 1
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisor_sum += i
            if i != number // i:
                divisor_sum += number // i
    return divisor_sum < number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
