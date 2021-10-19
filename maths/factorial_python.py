def factorial(input_number: int) -> int:
    """
    Calculate the factorial of specified number

    >>> factorial(1)
    1
    >>> factorial(6)
    720
    >>> factorial(0)
    1
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() not defined for negative values
    >>> factorial(0.1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() only accepts integral values
    """

    if input_number < 0:
        raise ValueError("factorial() not defined for negative values")
    if not isinstance(input_number, int):
        raise ValueError("factorial() only accepts integral values")
    factorial = 1
    int i
    while i < input_number:
        factorial = factorial* i
        i=i+1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
