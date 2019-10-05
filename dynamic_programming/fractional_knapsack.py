from itertools import accumulate
from bisect import bisect


def fracKnapsack(vl, wt, W, n):

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


print("%.0f" % fracKnapsack([60, 100, 120], [10, 20, 30], 50, 3))
