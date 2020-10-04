def bubble_sort(list_data: list, length: int = 0) -> list:
    """
    It is similar is bubble sort but recursive.
    :param list_data: mutable ordered sequence of elements
    :param length: length of list data
    :return: the same list in ascending order

    >>> bubble_sort([0, 5, 2, 3, 2], 5)
    [0, 2, 2, 3, 5]

    >>> bubble_sort([], 0)
    []

    >>> bubble_sort([-2, -45, -5], 3)
    [-45, -5, -2]

    >>> bubble_sort([-23, 0, 6, -4, 34], 5)
    [-23, -4, 0, 6, 34]

    >>> bubble_sort([-23, 0, 6, -4, 34], 5) == sorted([-23, 0, 6, -4, 34])
    True

    >>> bubble_sort(['z','a','y','b','x','c'], 6)
    ['a', 'b', 'c', 'x', 'y', 'z']

    >>> bubble_sort([1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6])
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    """
    length = length or len(list_data)
    swapped = False
    for i in range(length - 1):
        if list_data[i] > list_data[i + 1]:
            list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
            swapped = True

    return list_data if not swapped else bubble_sort(list_data, length - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
