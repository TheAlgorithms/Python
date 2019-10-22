"""
Counting Summations
Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?
"""


def partition(m):
    """Returns the number of different ways one hundred can be written as a sum
    of at least two positive integers.

    >>> partition(100)
    190569291
    >>> partition(50)
    204225
    >>> partition(30)
    5603
    >>> partition(10)
    41
    >>> partition(5)
    6
    >>> partition(3)
    2
    >>> partition(2)
    1
    >>> partition(1)
    0
    """
    memo = [[0 for _ in range(m)] for _ in range(m + 1)]
    for i in range(m + 1):
        memo[i][0] = 1

    for n in range(m + 1):
        for k in range(1, m):
            memo[n][k] += memo[n][k - 1]
            if n > k:
                memo[n][k] += memo[n - k - 1][k]

    return memo[m][m - 1] - 1


if __name__ == "__main__":
    print(partition(int(str(input()).strip())))
