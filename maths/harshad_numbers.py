"""
A Harshad number is divisible by the sum of its digits in any base n.
Reference: https://en.wikipedia.org/wiki/Harshad_number
"""


def int_to_base(number: int, base_of_interest: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while number > 0:
        number, remainder = divmod(number, base_of_interest)
        result = digits[remainder] + result

    if result == "":
        result = "0"

    return result


def sum_of_digits(num: int, base_of_interest: int) -> str:
    """
    Calculate the sum of digit values in a positive integer
    converted to the given 'base_of_interest'.
    Where 'base_of_interest' ranges from 2 to 36.

    Examples:
    >>> sum_of_digits(103, 12)
    '13'
    >>> sum_of_digits(1275, 4)
    '30'
    >>> sum_of_digits(6645, 2)
    '1001'
    >>> # bases beyond 36 and below 2 will error
    >>> sum_of_digits(543, 1)
    Traceback (most recent call last):
        ...
    ValueError: 'base_of_interest' must be between 36 and 2 inclusive
    >>> sum_of_digits(543, 37)
    Traceback (most recent call last):
        ...
    ValueError: 'base_of_interest' must be between 36 and 2 inclusive
    """

    if (base_of_interest > 36) or (base_of_interest < 2):
        raise ValueError("'base_of_interest' must be between 36 and 2 inclusive")

    num_str = int_to_base(num, base_of_interest)
    res = 0
    for char in num_str:
        res += int(char, base_of_interest)
    res = int_to_base(res, base_of_interest)
    return res


def all_harshad_numbers(num: int, base_of_interest: int) -> tuple[int, list[str]]:
    """
    Finds all Harshad numbers smaller than num in base 'base_of_interest'.
    Where 'base_of_interest' ranges from 2 to 36.

    Examples:
    >>> all_harshad_numbers(15, 2)
    (7, ['1', '10', '100', '110', '1000', '1010', '1100'])
    >>> all_harshad_numbers(12, 34)
    (11, ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B'])
    >>> all_harshad_numbers(12, 4)
    (7, ['1', '2', '3', '10', '12', '20', '21'])
    >>> # bases beyond 36 and below 2 will error
    >>> all_harshad_numbers(234, 37)
    Traceback (most recent call last):
        ...
    ValueError: 'base_of_interest' must be between 36 and 2 inclusive
    >>> all_harshad_numbers(234, 1)
    Traceback (most recent call last):
        ...
    ValueError: 'base_of_interest' must be between 36 and 2 inclusive
    """

    if (base_of_interest > 36) or (base_of_interest < 2):
        raise ValueError("'base_of_interest' must be between 36 and 2 inclusive")

    result = 0
    numbers = []
    if num >= 0:
        for i in range(1, num):
            y = sum_of_digits(i, base_of_interest)
            if i % int(y, base_of_interest) == 0:
                result += 1
                numbers.append(int_to_base(i, base_of_interest))

    return result, numbers


def is_harshad_number(num: int, base_of_interest: int) -> bool:
    """
    Determines whether n in base 'base_of_interest' is a harshad number.
    Where 'base_of_interest' ranges from 2 to 36.

    Examples:
    >>> is_harshad_number(18, 10)
    True
    >>> is_harshad_number(21, 10)
    True
    >>> is_harshad_number(-21, 5)
    False
    >>> # bases beyond 36 and below 2 will error
    >>> is_harshad_number(45, 37)
    Traceback (most recent call last):
        ...
    ValueError: 'base_of_interest' must be between 36 and 2 inclusive
    >>> is_harshad_number(45, 1)
    Traceback (most recent call last):
        ...
    ValueError: 'base_of_interest' must be between 36 and 2 inclusive
    """

    if (base_of_interest > 36) or (base_of_interest < 2):
        raise ValueError("'base_of_interest' must be between 36 and 2 inclusive")

    if num >= 0:
        n = int_to_base(num, base_of_interest)
        d = sum_of_digits(num, base_of_interest)
        if int(n, base_of_interest) % int(d, base_of_interest) == 0:
            return True

    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
