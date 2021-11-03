import doctest
from collections import Counter


def sock_merchant(ar: list[int]) -> int:
    """
    >>> sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    >>> sock_merchant([1, 1, 3, 3])
    2
    """

    i = 0
    occur = Counter(ar)

    for x in occur.values():
        i += x // 2
    return i


if __name__ == "__main__":

    array = list(map(int, input().rstrip().split()))

    result = sock_merchant(array)
    print(result)
    doctest.testmod()
