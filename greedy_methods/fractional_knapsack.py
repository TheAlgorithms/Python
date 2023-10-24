from bisect import bisect
from itertools import accumulate

# Reference Link: https://en.wikipedia.org/wiki/Continuous_knapsack_problem


def frac_knapsack(vl: list, wt: list, w: int, n: int) -> float:
    """
    This function implements fractional knapsack problem.

    Args:
        vl: List of values of items.
        wt: List of weights of items.
        w: Capacity of the knapsack.
        n: Number of items.

    Returns:
        Maximum value of items that can be put into the knapsack.

    >>> frac_knapsack([60, 100, 120], [10, 20, 30], 50, 3)
    240.0
    """

    # sort in descending order of value/weight ratio
    r = sorted(zip(vl, wt), key=lambda x: x[0] / x[1], reverse=True)

    vl, wt = [i[0] for i in r], [i[1] for i in r]  # unzip the list
    acc = list(accumulate(wt))  # cumulative sum of weights
    k = bisect(acc, w)  # find the index of the weight just greater than w

    if k == 0:  # no item can be put into the knapsack
        return 0
    elif k != n:  # fractional part of the kth item can be put into the knapsack
        return sum(vl[:k]) + (w - acc[k - 1]) * (vl[k]) / (wt[k])
    return sum(vl[:k])  # all items can be put into the knapsack


if __name__ == "__main__":
    import doctest

    doctest.testmod()
