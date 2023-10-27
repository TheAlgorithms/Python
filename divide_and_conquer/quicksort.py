def quick_sort(array):
    """Pure implementation of quick sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> quick_sort([])
    []

    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    array_length = len(array)
    if( array_length <= 1):
        return array
    else:
        pivot = ARRAY[0]
        greater = [ element for element in array[1:] if element > pivot ]
        lesser = [ element for element in array[1:] if element <= pivot ]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == '__main__':

    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user_input.split(',') ]
    print( quick_sort(unsorted) )
