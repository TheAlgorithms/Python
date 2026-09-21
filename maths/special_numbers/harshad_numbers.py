"""
A harshad number (or more specifically an n-harshad number) is a number that's
divisible by the sum of its digits in some given base n.
Reference: https://en.wikipedia.org/wiki/Harshad_number
"""


def int_to_base(number: int, base: int) -> str:
    """
    Convert a given positive decimal integer to base 'base'.
    Where 'base' ranges from 2 to 36.

    Examples:
    >>> int_to_base(0, 21)
    '0'
    >>> int_to_base(23, 2)
    '10111'
    >>> int_to_base(58, 5)
    '213'
    >>> int_to_base(167, 16)
    'A7'
    >>> # bases below 2 and beyond 36 will error
    >>> int_to_base(98, 1)
    Traceback (most recent call last):
        ...
    ValueError: 'base' must be between 2 and 36 inclusive
    >>> int_to_base(98, 37)
    Traceback (most recent call last):
        ...
    ValueError: 'base' must be between 2 and 36 inclusive
    >>> int_to_base(-99, 16)
    Traceback (most recent call last):
        ...
    ValueError: number must be a positive integer
    """

    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36 inclusive")

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    if number < 0:
        raise ValueError("number must be a positive integer")

    while number > 0:
        number, remainder = divmod(number, base)
        result = digits[remainder] + result

    if result == "":
        result = "0"

    return result


def sum_of_digits(num: int, base: int) -> str:
    """
    Calculate the sum of digit values in a positive integer
    converted to the given 'base'.
    Where 'base' ranges from 2 to 36.

    Examples:
    >>> sum_of_digits(103, 12)
    '13'
    >>> sum_of_digits(1275, 4)
    '30'
    >>> sum_of_digits(6645, 2)
    '1001'
    >>> # bases below 2 and beyond 36 will error
    >>> sum_of_digits(543, 1)
    Traceback (most recent call last):
        ...
    ValueError: 'base' must be between 2 and 36 inclusive
    >>> sum_of_digits(543, 37)
    Traceback (most recent call last):
        ...
    ValueError: 'base' must be between 2 and 36 inclusive
    """

    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36 inclusive")

    num_str = int_to_base(num, base)
    res = sum(int(char, base) for char in num_str)
    res_str = int_to_base(res, base)
    return res_str


def harshad_numbers_in_base(limit: int, base: int) -> list[str]:
    """
    Finds all Harshad numbers smaller than num in base 'base'.
    Where 'base' ranges from 2 to 36.

    Examples:
    >>> harshad_numbers_in_base(15, 2)
    ['1', '10', '100', '110', '1000', '1010', '1100']
    >>> harshad_numbers_in_base(12, 34)
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B']
    >>> harshad_numbers_in_base(12, 4)
    ['1', '2', '3', '10', '12', '20', '21']
    >>> # bases below 2 and beyond 36 will error
    >>> harshad_numbers_in_base(234, 37)
    Traceback (most recent call last):
        ...
    ValueError: 'base' must be between 2 and 36 inclusive
    >>> harshad_numbers_in_base(234, 1)
    Traceback (most recent call last):
        ...
    ValueError: 'base' must be between 2 and 36 inclusive
    >>> harshad_numbers_in_base(-12, 6)
    []
    """

    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36 inclusive")

    if limit < 0:
        return []

    numbers = [
        int_to_base(i, base)
        for i in range(1, limit)
        if i % int(sum_of_digits(i, base), base) == 0
    ]

    return numbers


def is_harshad_number_in_base(num: int, base: int) -> bool:
    """
    Determines whether n in base 'base' is a harshad number.
    Where 'base' ranges from 2 to 36.

    Examples:
    >>> is_harshad_number_in_base(18, 10)
    True
    >>> is_harshad_number_in_base(21, 10)
    True
    >>> is_harshad_number_in_base(-21, 5)
    False
    >>> # bases below 2 and beyond 36 will error
    >>> is_harshad_number_in_base(45, 37)
    Traceback (most recent call last):
        ...
    ValueError: 'base' must be between 2 and 36 inclusive
    >>> is_harshad_number_in_base(45, 1)
    Traceback (most recent call last):
        ...
    ValueError: 'base' must be between 2 and 36 inclusive
    """

    if base < 2 or base > 36:
        raise ValueError("'base' must be between 2 and 36 inclusive")

    if num < 0:
        return False

    n = int_to_base(num, base)
    d = sum_of_digits(num, base)
    return int(n, base) % int(d, base) == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
