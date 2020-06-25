"""
This is a non-parallelized implementation of odd-even transpostiion sort.

Normally the swaps in each set happen simultaneously, without that the algorithm
is no better than bubble sort.
"""


def OddEvenTransposition(arr):
    """
    >>> OddEvenTransposition([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> OddEvenTransposition([13, 11, 18, 0, -1])
    [-1, 0, 11, 13, 18]

    >>> OddEvenTransposition([-.1, 1.1, .1, -2.9])
    [-2.9, -0.1, 0.1, 1.1]
    """
    for i in range(0, len(arr)):
        for i in range(i % 2, len(arr) - 1, 2):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


if __name__ == "__main__":
    arr = list(range(10, 0, -1))
    print(f"Original: {arr}. Sorted: {OddEvenTransposition(arr)}")
