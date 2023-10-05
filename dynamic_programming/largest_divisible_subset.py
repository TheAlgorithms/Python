from __future__ import annotations


def largest_divisible_subset(array):
    """
    Algorithm to find the biggest subset 
    in the given array such that for any 
    2 elements x and y in the subset,
    either x divides y or y divides x
    >>> largest_divisible_subset([1,16,7,8,4])
    [16, 8, 4, 1]
    >>> largest_divisible_subset([1,2,3])
    [2, 1]
    >>> largest_divisible_subset([1, 2, 4, 8])
    [8, 4, 2, 1]
    """
    n = len(array)

    # Sort the array in ascending order
    # as the sequence does not matter 
    # we only have to pick up a subset
    array.sort()

    # Initialize dp and hash arrays with 1s
    dp = [1] * n
    hash_arr = list(range(n))

    # Iterate through the array
    for i in range(n):
        for prev_index in range(i):
            if array[i] % array[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                dp[i] = 1 + dp[prev_index]
                hash_arr[i] = prev_index

    ans = -1
    last_index = -1

    # Find the maximum length and its corresponding index
    for i in range(n):
        if dp[i] > ans:
            ans = dp[i]
            last_index = i

    # Reconstruct the divisible subset
    result = [array[last_index]]
    while hash_arr[last_index] != last_index:
        last_index = hash_arr[last_index]
        result.append(array[last_index])

    return result

if __name__ == "__main__":
    from doctest import testmod

    testmod()

    array = [1, 16, 7, 8, 4]

    ans = largest_divisible_subset(array)

    print("The longest divisible subset elements are:", ans)