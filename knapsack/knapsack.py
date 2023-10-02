""" A naive recursive implementation of 0-1 Knapsack Problem
    https://en.wikipedia.org/wiki/Knapsack_problem
"""


def knapsack(capacity, weights, values, permit_repetition=False):
    """
    #Parameters:
    #capacity - max item weight knapsack can hold
    #weights - list of item weights
    #values -list of item values
    #permit_repetition - boolean restricting repetitve selection of items

    >>> cap = 50
    >>> val = [60, 100, 120]
    >>> w = [10, 20, 30]
    >>> knapsack(cap, w, val, permit_repetition=False)
    220

    >>> knapsack(cap, w, val, permit_repetition=True)
    300
    """

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                if permit_repetition:
                    dp[i][w] = max(
                        dp[i - 1][w], dp[i][w - weights[i - 1]] + values[i - 1]
                    )
                else:
                    dp[i][w] = max(
                        dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]
                    )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
