def bubble_sort(list1):
    """
    It is similar is bubble sort but recursive.
    :param list1: mutable ordered sequence of elements
    :return: the same list in ascending order

    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -45, -5])
    [-45, -5, -2]

    >>> bubble_sort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]

    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True

    >>> bubble_sort(['z','a','y','b','x','c'])
    ['a', 'b', 'c', 'x', 'y', 'z']
    
    """

    for i, num in enumerate(list1):
        try:
            if list1[i + 1] < num:
                list1[i] = list1[i + 1]
                list1[i + 1] = num
                bubble_sort(list1)
        except IndexError:
            pass
    return list1


if __name__ == "__main__":
    list1 = [33, 99, 22, 11, 66]
    bubble_sort(list1)
    print(list1)
