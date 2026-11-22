# Tribonacci sequence using Dynamic Programming


def tribonacci(num: int) -> list[int]:
    """
    Given a number, return first n Tribonacci Numbers.
    >>> tribonacci(5)
    [0, 0, 1, 1, 2]
    >>> tribonacci(8)
    [0, 0, 1, 1, 2, 4, 7, 13]
    >>> tribonacci(0)
    []
    >>> tribonacci(1)
    [0]
    >>> tribonacci(2)
    [0, 0]
    """
    dp = [0] * num
    if num > 2:
        dp[2] = 1

    for i in range(3, num):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp


if __name__ == "__main__":
    import doctest

    doctest.testmod()
