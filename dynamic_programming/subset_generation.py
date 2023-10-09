# Print all subset combinations of n element in given set of r element.


def combinations(arr, n, r, index=0, data=None, i=0):
    """
    Generate and print all combinations of 'r' elements from the input list 'arr'.
    Args:
    arr (list): The input list from which combinations are generated.
    n (int): The total number of elements in the input list 'arr'.
    r (int): The size of the combinations to be generated.
    index (int, optional): The current index in the 'data' array. Defaults to 0.
    data (list, optional): Temporary array to store the current combination.
    i (int, optional): The current index in the input list 'arr'. Defaults to 0.
    Returns:
    None: This function prints the combinations but does not return a value.
    Examples:
    >>> arr = [1, 2, 3, 4]
    >>> n = len(arr)
    >>> r = 2
    >>> combinations(arr, n, r)
    1 2
    1 3
    1 4
    2 3
    2 4
    3 4
    """
    if data is None:
        data = [0] * r

    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print(" ")
        return
    if i >= n:
        return
    data[index] = arr[i]
    combinations(arr, n, r, index + 1, data, i + 1)
    combinations(arr, n, r, index, data, i + 1)


if __name__ == "__main__":
      import doctest

    doctest.testmod()
