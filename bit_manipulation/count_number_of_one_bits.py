from timeit import timeit
def get_set_bits_count_using_brian_kernighans_algorithm(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer
    >>> get_set_bits_count_using_brian_kernighans_algorithm(25)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(37)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(21)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(58)
    4
    >>> get_set_bits_count_using_brian_kernighans_algorithm(0)
    0
    >>> get_set_bits_count_using_brian_kernighans_algorithm(256)
    1
    >>> get_set_bits_count_using_brian_kernighans_algorithm(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive
    """
    if number < 0:
        raise ValueError("the value of input must be positive")
    result = 0
    while number:
        number &= (number-1)
        result+= 1
    return result

def get_set_bits_count_using_modulo_operator(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer
    >>> get_set_bits_count_using_modulo_operator(25)
    3
    >>> get_set_bits_count_using_modulo_operator(37)
    3
    >>> get_set_bits_count_using_modulo_operator(21)
    3
    >>> get_set_bits_count_using_modulo_operator(58)
    4
    >>> get_set_bits_count_using_modulo_operator(0)
    0
    >>> get_set_bits_count_using_modulo_operator(256)
    1
    >>> get_set_bits_count_using_modulo_operator(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be positive
    """
    if number < 0:
        raise ValueError("the value of input must be positive")
    result = 0
    while number:
        if number % 2 == 1:
            result += 1
        number = number >> 1
    return result

def benchmark() -> None:
    """
    Benchmark code for comparing 2 functions,
    with 3 different length int values.
    """
    print("\nFor 25 = :")
    print(
        "> get_set_bits_count_using_modulo_operator()",
        "\t\tans =",
        get_set_bits_count_using_modulo_operator(25),
        "\ttime =",
        timeit("z.get_set_bits_count_using_modulo_operator(25)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> get_set_bits_count_using_brian_kernighans_algorithm()",
        "\tans =",
        get_set_bits_count_using_brian_kernighans_algorithm(25),
        "\ttime =",
        timeit("z.get_set_bits_count_using_brian_kernighans_algorithm(25)", setup="import __main__ as z"),
        "seconds",
    )

    print("\nFor 37 = :")
    print(
        "> get_set_bits_count_using_modulo_operator()",
        "\t\tans =",
        get_set_bits_count_using_modulo_operator(37),
        "\ttime =",
        timeit("z.get_set_bits_count_using_modulo_operator(37)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> get_set_bits_count_using_brian_kernighans_algorithm()",
        "\tans =",
        get_set_bits_count_using_brian_kernighans_algorithm(37),
        "\ttime =",
        timeit("z.get_set_bits_count_using_brian_kernighans_algorithm(37)", setup="import __main__ as z"),
        "seconds",
    )

    print("\nFor 58 = :")
    print(
        "> get_set_bits_count_using_modulo_operator()",
        "\t\tans =",
        get_set_bits_count_using_modulo_operator(58),
        "\ttime =",
        timeit("z.get_set_bits_count_using_modulo_operator(58)", setup="import __main__ as z"),
        "seconds",
    )
    print(
        "> get_set_bits_count_using_brian_kernighans_algorithm()",
        "\tans =",
        get_set_bits_count_using_brian_kernighans_algorithm(58),
        "\ttime =",
        timeit("z.get_set_bits_count_using_brian_kernighans_algorithm(58)", setup="import __main__ as z"),
        "seconds",
    )


if __name__ == "__main__":
    import doctest

    benchmark()
    doctest.testmod()
