# Tribonacci sequence using Dynamic Programming


def tribonacci(num: int) -> list:
    """
    Given a number, return first n Tribonacci Numbers.
    >>> tribonacci(5)
    [0, 0, 1, 1, 2]
    >>> tribonacci(8)
    [0, 0, 1, 1, 2, 4, 7, 13]
    """
    dp = [0 for i in range(num)]
    dp[0] = dp[1] = 0
    dp[2] = 1

    for i in range(3, num):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp


if __name__ == "__main__":
    import doctest

    doctest.testmod()
