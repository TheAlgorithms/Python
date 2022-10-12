def is_sum_subset(arr, arr_len, required_sum):
    """
    >>> is_sum_subset([2, 4, 6, 8], 4, 5)
    False
    >>> is_sum_subset([2, 4, 6, 8], 4, 14)
    True
    """
    # a subset value says 1 if that subset sum can be formed else 0
    # initially no subsets can be formed hence False/0
    subset = [[False for i in range(required_sum + 1)] for i in range(arr_len + 1)]

    # for each arr value, a sum of zero(0) can be formed by not taking any element
    # hence True/1
    for i in range(arr_len + 1):
        subset[i][0] = True

    # sum is not zero and set is empty then false
    for i in range(1, required_sum + 1):
        subset[0][i] = False

    for i in range(1, arr_len + 1):
        for j in range(1, required_sum + 1):
            if arr[i - 1] > j:
                subset[i][j] = subset[i - 1][j]
            if arr[i - 1] <= j:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - arr[i - 1]]

    # uncomment to print the subset
    # for i in range(arrLen+1):
    #     print(subset[i])
    print(subset[arr_len][required_sum])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
