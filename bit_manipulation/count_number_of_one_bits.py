from timeit import timeit


def get_set_bits_count_using_brian_kernighans_algorithm(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer
    Uses Brian Kernighan's algorithm: the operation (number & (number - 1)) removes
    the rightmost set bit from the number. By repeating this until the number becomes
    zero, we count exactly how many set bits existed.
    Algorithm (Brian Kernighan's Method):
    1. While number > 0:
       a. Execute: number &= (number - 1)  # Removes the lowest set bit
       b. Increment counter
    2. Return counter
    Why it works: (number - 1) flips all bits after the rightmost set bit.
    So (number & (number - 1)) removes only that one rightmost set bit.
    Example: 25 = 0b11001
    - Iteration 1: 25 & 24 = 0b11001 & 0b11000 = 0b11000 (24)
    - Iteration 2: 24 & 23 = 0b11000 & 0b10111 = 0b10000 (16)
    - Iteration 3: 16 & 15 = 0b10000 & 0b01111 = 0b00000 (0)
    - Count: 3 set bits
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

    Uses the basic approach: repeatedly check if the least significant bit (LSB) is set
    using the modulo operator, then right-shift to check the next bit.

    Algorithm:
    1. While number > 0:
       a. If number % 2 == 1, increment counter (LSB is 1)
       b. Right-shift number by 1 (number >>= 1) to check next bit
    2. Return counter

    Example: 25 = 0b11001
    - Iteration 1: 25 % 2 = 1, count = 1, then 25 >> 1 = 12
    - Iteration 2: 12 % 2 = 0, count = 1, then 12 >> 1 = 6
    - Iteration 3: 6 % 2 = 0, count = 1, then 6 >> 1 = 3
    - Iteration 4: 3 % 2 = 1, count = 2, then 3 >> 1 = 1
    - Iteration 5: 1 % 2 = 1, count = 3, then 1 >> 1 = 0
    - Count: 3 set bits

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


def benchmark() -> None:
    """
    Benchmark code for comparing 2 functions, with different length int values.
    Brian Kernighan's algorithm is consistently faster than using modulo_operator.
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

    for number in (25, 37, 58, 0):
        do_benchmark(number)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
