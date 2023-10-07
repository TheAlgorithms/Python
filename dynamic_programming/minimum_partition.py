"""
Partition a set into two subsets such that the difference of subset sums is minimum
"""


def find_min(arr):
    """

    >>> find_min([1,2,3,4])
    0
    >>> find_min([0,0,0,0])
    0
    >>> find_min([-1,-5,5,1])
    0
    >>> find_min([0,0,0,1,2,-4])
    -1
    >>> find_min([9,9,9,9,9])
    9
    >>> find_min([])
    0
    >>> find_min([0,0,0,0])
    0
    >>> find_min([-1,-5,-10,-3])
    -1
    >>> find_min([1,5,10,3])
    1
    >>> find_min([-1,0,1])
    0

    """
    n = len(arr)
    s = sum(arr)

    dp = [[False for x in range(s + 1)] for y in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = True

    for i in range(1, s + 1):
        dp[0][i] = False

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            dp[i][j] = dp[i][j - 1]

            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    for j in range(int(s / 2), -1, -1):
        if dp[n][j] is True:
            diff = s - 2 * j
            break

    return diff
