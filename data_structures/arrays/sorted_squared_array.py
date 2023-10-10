def sorted_squared_array(arr: list[int]) -> list:
    """
    Returns the square of the initial sorted array in ascending order
    >>> sorted_squared_array( [-5, -4, -3, 2, 5])
    [4, 9, 16, 25, 25]
    >>> sorted_squared_array( [-1, 0, 1, 2])
    [0, 1, 1, 4]
    >>> sorted_squared_array( [-15, -4, -1, 12, 15, 17])
    [1, 16, 144, 225, 225, 289]
    """
    left = 0
    i = right = len(arr) - 1
    res = [0] * len(arr)

    while left <= right:
        if abs(arr[right]) > abs(arr[left]):
            res[i] = arr[right] ** 2
            right -= 1
        else:
            res[i] = arr[left] ** 2
            left += 1
        i -= 1
    return res
