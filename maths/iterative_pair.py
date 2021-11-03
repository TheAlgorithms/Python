import doctest
from collections import Counter


def sockMerchant(n, ar):
    """
    >>> sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    >>> sockMerchant(4, [1, 1, 3, 3])
    2

    """

    i = 0
    occur = Counter(ar)

    for x in occur.values():
        i += x // 2
    return i


if __name__ == "__main__":

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
    doctest.testmod()
