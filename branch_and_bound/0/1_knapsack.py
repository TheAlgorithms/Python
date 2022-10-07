"""
The 0/1 knapsack problem means that the items are either completely or no items are filled in a knapsack.
>>> knapSack([60,100,120],[10,20,30],50)
'220'
>>> knapSack("")
Traceback (most recent call last):
...
ValueError:Please Enter Value Not Equal to 0

"""


def knapSack(W, wt, val):
    n = len(val)
    if n == 0 or W == 0 or len(wt) == 0:
        raise ValueError("Please Enter Value Not Equal to 0")
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
