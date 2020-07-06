from bisect import bisect
from itertools import accumulate


def fracKnapsack(vl, wt, W, n):
    """
    >>> fracKnapsack([60, 100, 120], [10, 20, 30], 50, 3)
    240.0
    """

    r = list(sorted(zip(vl, wt), key=lambda x: x[0] / x[1], reverse=True))
    vl, wt = [i[0] for i in r], [i[1] for i in r]
    acc = list(accumulate(wt))
    k = bisect(acc, W)
    return (
        0
        if k == 0
        else sum(vl[:k]) + (W - acc[k - 1]) * (vl[k]) / (wt[k])
        if k != n
        else sum(vl[:k])
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
