def sum_of_digits(n: int) -> int:
    """
    Find the sum of digits of a number.

    >>> sum_of_digits(12345)
    15
    >>> sum_of_digits(123)
    6
    """
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res


if __name__ == "__main__":
    print(sum_of_digits(12345))  # ===> 15
