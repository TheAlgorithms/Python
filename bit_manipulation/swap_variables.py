def swap_variables(first_variable: int, second_variable: int) -> list:
    """
    Swap two variables using bit manipulations

    ---
    type first_variable: int
    type second_variable: int
    type return: list

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
    first_variable = first_variable ^ second_variable
    second_variable = first_variable ^ second_variable
    first_variable = first_variable ^ second_variable
    return [first_variable, second_variable]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
