from collections import defaultdict


def min_cost(basket1: list[int], basket2: list[int]) -> int:
    """
    Compute the minimum cost to make two baskets identical by swapping fruits.

    Each fruit is represented by an integer value. The goal is to make both baskets
    have the same multiset of elements with the minimum swap cost. Each swap cost
    is defined as the minimum of the swapped fruit's value and twice the smallest
    fruit value in both baskets.

    If it's impossible to make the baskets identical, return -1.

    Args:
        basket1 (list[int]): The first basket of fruits.
        basket2 (list[int]): The second basket of fruits.

    Returns:
        int: The minimum total cost, or -1 if impossible.

    Examples:
        >>> min_cost([4, 2, 2, 2], [1, 4, 1, 2])
        1
        >>> min_cost([1, 2, 3, 4], [2, 3, 4, 1])
        0
        >>> min_cost([1, 1, 1, 1], [1, 1, 1, 1])
        0
        >>> min_cost([1, 2, 2], [2, 1, 1])
        -1
        >>> min_cost([5, 3, 3, 2], [2, 5, 5, 3])
        -1
    """
    n = len(basket1)
    freq: defaultdict[int, int] = defaultdict(int)
    mn: float = float("inf")

    for i in range(n):
        freq[basket1[i]] += 1
        freq[basket2[i]] -= 1
        mn = min(mn, basket1[i], basket2[i])

    to_swap: list[int] = []
    for j, k in freq.items():
        if k % 2 != 0:
            return -1
        to_swap += [j] * (abs(k) // 2)

    to_swap.sort()
    res: int = 0
    for i in range(len(to_swap) // 2):
        res += min(to_swap[i], 2 * int(mn))

    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("All doctests passed.")
