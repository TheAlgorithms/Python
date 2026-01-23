# Kadane's algorithm


def kadanes_algorithm(arr: list[int]) -> int:
    """
    Function to find the maximum sum of a contiguous subarray using Kadane's algorithm

    >>> kadanes_algorithm([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6

    >>> kadanes_algorithm([-1, -2, -3, -4])
    -1

    >>> kadanes_algorithm([5, 4, -1, 7, 8])
    23

    >>> kadanes_algorithm([1])
    1

    >>> kadanes_algorithm([-1, 2, 3, -5, 4])
    5
    """
    # initializing variables
    max_current = arr[0]  # store the current max sum
    max_global = arr[0]  # store the global max sum

    # looping through the array starting at the second element
    for i in range(1, len(arr)):
        # update current max sum by choosing the maximum between
        # current element alone or current element plus previous max
        max_current = max(arr[i], max_current + arr[i])

        # update global max sum if current max is larger
        max_global = max(max_current, max_global)

    return max_global


if __name__ == "__main__":
    import doctest

    doctest.testmod()
