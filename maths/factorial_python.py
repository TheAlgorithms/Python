def factorial(input_number: int) -> int:
    """
        Non-recursive algorithm of finding factorial of the
        input number.
        >>> factorial(1)
        1
        >>> factorial(6)
        720
        >>> factorial(0)
        1
    """

    if input_number < 0:
        raise ValueError("Input input_number should be non-negative")
    result = 1
    for i in range(1, input_number):
        result = result * (i + 1)
    return result


if __name__ == '__main__':
    import doctest

    doctest.testmod()