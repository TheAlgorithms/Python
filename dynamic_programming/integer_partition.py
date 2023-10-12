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
        >>> partition(5)
        2
        >>> partition(6)
        3
    """
    # ... (the existing code of the function)

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
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                print("Number of ways to partition:", partition(n))
        except ValueError:
            print("Please enter a valid positive integer.")
    else:
        try:
            n = int(sys.argv[1])
            if n <= 0:
                print("Please pass a positive integer.")
            else:
                print("Number of ways to partition:", partition(n))
        except ValueError:
            print("Please pass a valid positive integer.")
