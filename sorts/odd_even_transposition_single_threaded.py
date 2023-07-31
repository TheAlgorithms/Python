"""
Source: https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort

This is a non-parallelized implementation of odd-even transposition sort.

Normally the swaps in each set happen simultaneously, without that the algorithm
is no better than bubble sort.
"""


def odd_even_transposition(arr: list) -> list:
    """
    >>> odd_even_transposition([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> odd_even_transposition([13, 11, 18, 0, -1])
    [-1, 0, 11, 13, 18]

    >>> odd_even_transposition([-.1, 1.1, .1, -2.9])
    [-2.9, -0.1, 0.1, 1.1]
    """
    arr_size = len(arr)
    for _ in range(arr_size):
        for i in range(_ % 2, arr_size - 1, 2):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


if __name__ == "__main__":
    arr = list(range(10, 0, -1))
    print(f"Original: {arr}. Sorted: {odd_even_transposition(arr)}")
