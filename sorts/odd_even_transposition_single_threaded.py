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


# creates a list and sorts it
def main():
    list = []

    for i in range(10, 0, -1):
        list.append(i)
    print("Initial List")
    print(*list)

    list = OddEvenTransposition(list)

    print("Sorted List\n")
    print(*list)


if __name__ == "__main__":
    main()
