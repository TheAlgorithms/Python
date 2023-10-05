from __future__ import annotations


def largest_divisible_subset(array: list[int]) -> list[int]:
    """
    Algorithm to find the biggest subset
    in the given array such that for any
    2 elements x and y in the subset,
    either x divides y or y divides x
    >>> largest_divisible_subset([1, 16, 7, 8, 4])
    [16, 8, 4, 1]
    >>> largest_divisible_subset([1, 2, 3])
    [2, 1]
    >>> largest_divisible_subset([-1, -2, -3])
    [-3]
    >>> largest_divisible_subset([1, 2, 4, 8])
    [8, 4, 2, 1]
    >>> largest_divisible_subset((1, 2, 4, 8))
    [8, 4, 2, 1]
    >>> largest_divisible_subset([1, 1, 1])
    [1, 1, 1]
    >>> largest_divisible_subset([0, 0, 0])
    [0, 0, 0]
    >>> largest_divisible_subset([-1, -1, -1])
    [-1, -1, -1]
    >>> largest_divisible_subset([])
    []
    """
    array_size = len(array)

    # Sort the array in ascending order
    # as the sequence does not matter
    # we only have to pick up a subset
    array.sort()

    # Initialize memo and hash arrays with 1s
    memo = [1] * array_size
    hash_array = list(range(array_size))

    # Iterate through the array
    for i, item in enumerate(array):
        for prev_index in range(i):
            if item % array[prev_index] == 0 and 1 + memo[prev_index] > memo[i]:
                memo[i] = 1 + memo[prev_index]
                hash_array[i] = prev_index

    ans = -1
    last_index = -1

    # Find the maximum length and its corresponding index
    for i in range(array_size):
        if memo[i] > ans:
            ans = memo[i]
            last_index = i

    # Reconstruct the divisible subset
    result = [array[last_index]]
    while hash_array[last_index] != last_index:
        last_index = hash_array[last_index]
        result.append(array[last_index])

    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    array = [1, 16, 7, 8, 4]

    answer = largest_divisible_subset(array)

    print("The longest divisible subset elements are:", answer)
