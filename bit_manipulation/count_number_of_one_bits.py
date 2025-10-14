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
    ValueError: the value of input must not be negative
    """
    if number < 0:
        raise ValueError("the value of input must not be negative")
    result = 0
    while number:
        number &= number - 1
        result += 1
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
    ValueError: the value of input must not be negative
    """
    if number < 0:
        raise ValueError("the value of input must not be negative")
    result = 0
    while number:
        if number % 2 == 1:
            result += 1
        number >>= 1
    return result


def get_set_bits_count_using_lookup_table(number: int) -> int:
    """
    Count the number of set bits in a 32-bit integer using a precomputed lookup table.

    Note: I see similar approach in GeeksforGeeks, but the implementation is little different.
    Link to Code:
    https://www.geeksforgeeks.org/dsa/count-set-bits-integer-using-lookup-table/

    >>> get_set_bits_count_using_lookup_table(25)
    3
    >>> get_set_bits_count_using_lookup_table(37)
    3
    >>> get_set_bits_count_using_lookup_table(21)
    3
    >>> get_set_bits_count_using_lookup_table(58)
    4
    >>> get_set_bits_count_using_lookup_table(0)
    0
    >>> get_set_bits_count_using_lookup_table(256)
    1
    >>> get_set_bits_count_using_lookup_table(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must not be negative
    """
    _lookup_table = [bin(i).count("1") for i in range(256)]

    if number < 0:
        raise ValueError("the value of input must not be negative")

    # Split 32-bit number into four 8-bit chunks and use lookup table
    return (
        _lookup_table[number & 0xFF]
        + _lookup_table[(number >> 8) & 0xFF]
        + _lookup_table[(number >> 16) & 0xFF]
        + _lookup_table[(number >> 24) & 0xFF]
    )



def benchmark() -> None:
    """
    Benchmark code for comparing 3 functions, with different length int values.
    Brian Kernighan's algorithm is consistently faster than using modulo_operator,
    and the lookup table method is often the fastest for repeated calls.
    """

    def do_benchmark(number: int) -> None:
        setup = "import __main__ as z"
        print(f"Benchmark when {number = }:")

        print(f"{get_set_bits_count_using_modulo_operator(number) = }")
        timing = timeit(
            f"z.get_set_bits_count_using_modulo_operator({number})", setup=setup
        )
        print(f"timeit() runs in {timing} seconds")

        print(f"{get_set_bits_count_using_brian_kernighans_algorithm(number) = }")
        timing = timeit(
            f"z.get_set_bits_count_using_brian_kernighans_algorithm({number})",
            setup=setup,
        )
        print(f"timeit() runs in {timing} seconds")

        print(f"{get_set_bits_count_using_lookup_table(number) = }")
        timing = timeit(
            f"z.get_set_bits_count_using_lookup_table({number})",
            setup=setup,
        )
        print(f"timeit() runs in {timing} seconds")

    for number in (25, 37, 58, 0):
        do_benchmark(number)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
