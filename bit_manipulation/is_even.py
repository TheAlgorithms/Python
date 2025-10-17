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


if __name__ == "__main__":
    import doctest

    doctest.testmod()
