def digit_sum(n: int) -> int:
    """
    Find the sum of digits of a number.

    >>> digit_sum(12345)
    15
    >>> digit_sum(123)
    6
    """
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res


if __name__ == "__main__":
    print(digit_sum(12345))   # ===> 15
