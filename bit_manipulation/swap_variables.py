def swap_variables(a: int, b: int) -> list:
    """swap variables a and b using bit manipulations
    variables a and b are integers
    function returns a list of two swapped integers [a,b]
    >>> swap_variables(1, 2)
    [2, 1]
    >>> swap_variables(2, 1)
    [1, 2]
    >>> swap_variables(1, 1)
    [1, 1]
    >>> swap_variables(10000, 10)
    [10, 10000]
    >>> swap_variables(10, -10)
    [-10, 10]
    >>> swap_variables(-91, -10)
    [-10, -91]
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return [a, b]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
