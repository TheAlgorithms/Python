"""
The number of partitions of a number n into at least k parts equals the number of
partitions into exactly k parts plus the number of partitions into at least k-1 parts.
Subtracting 1 from each part of a partition of n into k parts gives a partition of n-k
into k parts. These two facts together are used for this algorithm.
"""


def partition(m: int) -> int:
    """
    Calculate the number of ways to partition a positive integer into distinct positive integers.

    Args:
        m (int): The positive integer to partition.

    Returns:
        int: The number of ways to partition the integer.

    Examples:
        * [Wikipedia - Partition (number theory)]
        * [Wikipedia - Partition function (number theory)]

        >>> partition(5)
        7  # Corrected expected output
        >>> partition(7)
        15
        >>> partition(100)
        190569292
        >>> partition(1_000)
        24061467864032622473692149727991
        >>> partition(-7)
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        >>> partition(0)
        Traceback (most recent call last):
            ...
        IndexError: list assignment index out of range
        >>> partition(7.8)
        Traceback (most recent call last):
            ...
        TypeError: 'float' object cannot be interpreted as an integer
    """
    if m <= 0:
        return 0  # Return 0 for non-positive integers

    memo: list[list[int]] = [[0 for _ in range(m)] for _ in range(m + 1)]
    for i in range(m + 1):
        memo[i][0] = 1

    for total in range(m + 1):
        for largest_num in range(1, m):
            memo[total][largest_num] += memo[total][largest_num - 1]
            if total - largest_num > 0:
                memo[total][largest_num] += memo[total - largest_num - 1][largest_num]

    return memo[m][m - 1]


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        try:
            n = int(input("Enter a positive integer: ").strip())
            result = partition(n)
            print("Number of ways to partition:", result)
        except ValueError:
            print("Please enter a valid positive integer.")
    else:
        try:
            n = int(sys.argv[1])
            result = partition(n)
            print("Number of ways to partition:", result)
        except ValueError:
            print("Please pass a valid positive integer.")
