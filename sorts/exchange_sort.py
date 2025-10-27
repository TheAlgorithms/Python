def exchange_sort(data: list) -> list:
    """
    Sorts a list of elements using the Exchange Sort algorithm.

    Exchange Sort is a variant of Bubble Sort, swapping elements if they
    are found to be out of order.

    Examples:
    >>> exchange_sort([5, 2, 9, 1, 5])
    [1, 2, 5, 5, 9]
    >>> exchange_sort([10, 5, 3, 2])
    [2, 3, 5, 10]
    """
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data

if __name__ == '__main__':
    import doctest
    doctest.testmod()
