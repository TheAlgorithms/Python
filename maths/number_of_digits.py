import math


def num_digits(n: int) -> int:
    """
    Find the number of digits in a number.
    Time Complexity: O(n)

    >>> num_digits(12345)
    5
    >>> num_digits(123)
    3
    """
    digits = 0
    while n > 0:
        n = n // 10
        digits += 1
    return digits


def num_digits2(n: int) -> int:
    """
    Find the number of digits in a number.
    Time Complexity: O(n)
    abs() is used for negative numbers

    >>> num_digits2(12345)
    5
    >>> num_digits2(123)
    3
    """
    return (len(str(abs(n))))


def num_digits_fast(n: int) -> int:
    """
    Find the number of digits in a number.
    Time Complexity: O(1)
    abs() is used as logarithm for negative numbers is not defined.

    >>> num_digits_fast(12345)
    5
    >>> num_digits_fast(123)
    3
    """
    return (math.floor(math.log(abs(n), 10) + 1))


if __name__ == "__main__":
    print(num_digits(12345))        # ===> 5 in O(n)
    print(num_digits2(12345))       # ===> 5 in O(n)
    print(num_digits_fast(12345))   # ===> 5 in O(1)
