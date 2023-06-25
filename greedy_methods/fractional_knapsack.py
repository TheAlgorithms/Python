from bisect import bisect
from itertools import accumulate


def frac_knapsack(vl, wt, w, n):
    """
    >>> frac_knapsack([60, 100, 120], [10, 20, 30], 50, 3)
    240.0
    """

    r = sorted(zip(vl, wt), key=lambda x: x[0] / x[1], reverse=True)
    vl, wt = [i[0] for i in r], [i[1] for i in r]
    acc = list(accumulate(wt))
    k = bisect(acc, w)
    return (
        0
        if k == 0
        else sum(vl[:k]) + (w - acc[k - 1]) * (vl[k]) / (wt[k])
        if k != n
        else sum(vl[:k])
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
