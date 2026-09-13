def is_even(number: int) -> bool:
    """Return True if the input integer is even using a bitwise check.

    Explanation:
    In binary, even numbers always have the least significant bit cleared (0),
    while odd numbers have it set (1). Therefore, ``n & 1 == 0`` implies even.

    >>> is_even(1)
    False
    >>> is_even(4)
    True
    >>> is_even(9)
    False
    >>> is_even(15)
    False
    >>> is_even(40)
    True
    >>> is_even(100)
    True
    >>> is_even(101)
    False
    >>> is_even(True)
    Traceback (most recent call last):
        ...
    TypeError: input must be an integer
    >>> is_even(3.14)
    Traceback (most recent call last):
        ...
    TypeError: input must be an integer
    """
    if not isinstance(number, int) or isinstance(number, bool):
        # bool is a subclass of int; explicitly disallow it as a number here.
        raise TypeError("input must be an integer")
    return (number & 1) == 0


def is_even_using_shift_operator(number: int) -> bool:
    """
    Returns True if the input integer is even.

    Explanation:
    In binary, even numbers end with 0, odd numbers end with 1.
    Examples:
    2  -> 10
    3  -> 11
    4  -> 100
    5  -> 101

    For odd numbers, the last bit is always 1.
    Using shift:
    (n >> 1) << 1 removes the last bit.
    If result equals n, n is even.

    >>> is_even_using_shift_operator(1)
    False
    >>> is_even_using_shift_operator(4)
    True
    >>> is_even_using_shift_operator(9)
    False
    >>> is_even_using_shift_operator(15)
    False
    >>> is_even_using_shift_operator(40)
    True
    >>> is_even_using_shift_operator(100)
    True
    >>> is_even_using_shift_operator(101)
    False
    """
    return (number >> 1) << 1 == number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
