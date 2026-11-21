"""
Woodall Number

In number theory, a Woodall number (also known as a Cullen number of the second
kind) is any natural number of the form:

    W_n = n * 2^n - 1

for any integer n >= 1.

The first few Woodall numbers are:
    1, 7, 23, 63, 159, 383, 895, 2047, 4607, 10239, ...

They also satisfy the recurrence relation:
    W_1 = 1
    W_(n + 1) = 2 * W_n + 2^(n + 1) + 1

Woodall numbers were first studied by Allan J. C. Cullen in 1905 and later
investigated in detail by Herbert J. Woodall in 1917.

References:
    https://en.wikipedia.org/wiki/Woodall_number
    https://oeis.org/A003261
"""


def woodall_number(index: int) -> int:
    """
    Return the index-th Woodall number: index * 2^index - 1.

    :param index: index of the Woodall number, must be a positive integer (index >= 1)
    :return: the index-th Woodall number

    >>> woodall_number(1)
    1
    >>> woodall_number(2)
    7
    >>> woodall_number(3)
    23
    >>> woodall_number(4)
    63
    >>> woodall_number(5)
    159
    >>> woodall_number(10)
    10239
    >>> woodall_number(20)
    20971519
    >>> all(
    ...     woodall_number(i) == i * (1 << i) - 1 for i in range(1, 100)
    ... )
    True
    >>> all(
    ...     woodall_number(i + 1) == 2 * woodall_number(i) + (1 << (i + 1)) + 1
    ...     for i in range(1, 50)
    ... )
    True
    >>> woodall_number(0)
    Traceback (most recent call last):
        ...
    ValueError: index must be a positive integer (index >= 1), got 0
    >>> woodall_number(-5)
    Traceback (most recent call last):
        ...
    ValueError: index must be a positive integer (index >= 1), got -5
    >>> woodall_number(2.5)
    Traceback (most recent call last):
        ...
    TypeError: index must be an integer, got 2.5
    >>> woodall_number("3")
    Traceback (most recent call last):
        ...
    TypeError: index must be an integer, got '3'
    >>> woodall_number(True)
    Traceback (most recent call last):
        ...
    TypeError: index must be an integer, got True
    """
    if not isinstance(index, int) or isinstance(index, bool):
        msg = f"index must be an integer, got {index!r}"
        raise TypeError(msg)
    if index < 1:
        msg = f"index must be a positive integer (index >= 1), got {index!r}"
        raise ValueError(msg)

    return (index << index) - 1


def is_woodall_number(number: int) -> bool:
    """
    Check whether a given integer is a Woodall number.

    :param number: integer to test
    :return: True if number is a Woodall number, False otherwise

    >>> is_woodall_number(1)
    True
    >>> is_woodall_number(7)
    True
    >>> is_woodall_number(23)
    True
    >>> is_woodall_number(63)
    True
    >>> is_woodall_number(159)
    True
    >>> is_woodall_number(10239)
    True
    >>> is_woodall_number(0)
    False
    >>> is_woodall_number(-7)
    False
    >>> is_woodall_number(10)
    False
    >>> is_woodall_number(100)
    False
    >>> is_woodall_number(6.5)
    Traceback (most recent call last):
        ...
    TypeError: number must be an integer, got 6.5
    >>> is_woodall_number("7")
    Traceback (most recent call last):
        ...
    TypeError: number must be an integer, got '7'
    >>> is_woodall_number(True)
    Traceback (most recent call last):
        ...
    TypeError: number must be an integer, got True
    """
    if not isinstance(number, int) or isinstance(number, bool):
        msg = f"number must be an integer, got {number!r}"
        raise TypeError(msg)
    if number < 1:
        return False

    k = 1
    while True:
        woodall = woodall_number(k)
        if woodall == number:
            return True
        if woodall > number:
            return False
        k += 1


def woodall_sequence(length: int) -> list[int]:
    """
    Return the first `length` Woodall numbers as a list.

    :param length: how many terms to return, must be a non-negative integer
    :return: list of the first `length` Woodall numbers

    >>> woodall_sequence(0)
    []
    >>> woodall_sequence(1)
    [1]
    >>> woodall_sequence(5)
    [1, 7, 23, 63, 159]
    >>> woodall_sequence(10)
    [1, 7, 23, 63, 159, 383, 895, 2047, 4607, 10239]
    >>> woodall_sequence(-1)
    Traceback (most recent call last):
        ...
    ValueError: length must be a non-negative integer, got -1
    >>> woodall_sequence(3.5)
    Traceback (most recent call last):
        ...
    TypeError: length must be an integer, got 3.5
    >>> woodall_sequence(True)
    Traceback (most recent call last):
        ...
    TypeError: length must be an integer, got True
    """
    if not isinstance(length, int) or isinstance(length, bool):
        msg = f"length must be an integer, got {length!r}"
        raise TypeError(msg)
    if length < 0:
        msg = f"length must be a non-negative integer, got {length!r}"
        raise ValueError(msg)

    return [woodall_number(i) for i in range(1, length + 1)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
