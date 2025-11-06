import math
from timeit import timeit
from typing import Callable


def num_digits(n: int) -> int:
    """
    Find the number of digits in an integer.

    >>> num_digits(12345)
    5
    >>> num_digits(123)
    3
    >>> num_digits(0)
    1
    >>> num_digits(-1)
    1
    >>> num_digits(-123456)
    6
    >>> num_digits('123')  # Raises a TypeError for non-integer input
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    digits = 0
    n = abs(n)
    while True:
        n = n // 10
        digits += 1
        if n == 0:
            break
    return digits


def num_digits_fast(n: int) -> int:
    """
    Find the number of digits using logarithm.

    >>> num_digits_fast(12345)
    5
    >>> num_digits_fast(123)
    3
    >>> num_digits_fast(0)
    1
    >>> num_digits_fast(-1)
    1
    >>> num_digits_fast(-123456)
    6
    >>> num_digits_fast('123')  # Raises a TypeError for non-integer input
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return 1 if n == 0 else math.floor(math.log10(abs(n)) + 1)


def num_digits_faster(n: int) -> int:
    """
    Find the number of digits using string conversion.

    >>> num_digits_faster(12345)
    5
    >>> num_digits_faster(123)
    3
    >>> num_digits_faster(0)
    1
    >>> num_digits_faster(-1)
    1
    >>> num_digits_faster(-123456)
    6
    >>> num_digits_faster('123')  # Raises a TypeError for non-integer input
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return len(str(abs(n)))


def benchmark() -> None:
    """
    Benchmark multiple functions with three different length integers.
    """
    def benchmark_a_function(func: Callable, value: int) -> None:
        call = f"{func.__name__}({value})"
        timing = timeit(f"__main__.{call}", setup="import __main__", number=10000)
        print(f"{call}: Result={func(value)}, Time={timing:.6f} sec")

    test_values = [
        262144,
        1125899906842624,
        1267650600228229401496703205376,
    ]

    for value in test_values:
        for func in (num_digits, num_digits_fast, num_digits_faster):
            benchmark_a_function(func, value)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()

