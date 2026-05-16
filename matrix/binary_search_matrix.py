def binary_search(array: list, lower_bound: int, upper_bound: int, value: int) -> int:
    """
    This function carries out Binary search on a 1d array and
    return -1 if it do not exist
    array: A 1d sorted array
    value : the value meant to be searched
    >>> matrix = [1, 4, 7, 11, 15]
    >>> binary_search(matrix, 0, len(matrix) - 1, 1)
    0
    >>> binary_search(matrix, 0, len(matrix) - 1, 23)
    -1
    """

    r = int((lower_bound + upper_bound) // 2)
    if array[r] == value:
        return r
    if lower_bound >= upper_bound:
        return -1
    if array[r] < value:
        return binary_search(array, r + 1, upper_bound, value)
    else:
        return binary_search(array, lower_bound, r - 1, value)


def mat_bin_search(value: int, matrix: list) -> list:
    """
    This function loops over a 2d matrix and calls binarySearch on
    the selected 1d array and returns [-1, -1] is it do not exist
    value : value meant to be searched
    matrix = a sorted 2d matrix
    >>> matrix = [[1, 4, 7, 11, 15],
    ...           [2, 5, 8, 12, 19],
    ...           [3, 6, 9, 16, 22],
    ...           [10, 13, 14, 17, 24],
    ...           [18, 21, 23, 26, 30]]
    >>> target = 1
    >>> mat_bin_search(target, matrix)
    [0, 0]
    >>> target = 34
    >>> mat_bin_search(target, matrix)
    [-1, -1]
    """
    index = 0
    if matrix[index][0] == value:
        return [index, 0]
    while index < len(matrix) and matrix[index][0] < value:
        r = binary_search(matrix[index], 0, len(matrix[index]) - 1, value)
        if r != -1:
            return [index, r]
        index += 1
    return [-1, -1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
