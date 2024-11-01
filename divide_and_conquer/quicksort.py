def quicksort(arr: list) -> list:
    """Quicksort function implementation in Python.

    https://en.wikipedia.org/wiki/Quicksort
    >>> quicksort([])
    []
    >>> quicksort([5])
    [5]
    >>> quicksort([3, 6, 8, 10, 1, 2, 1, 3, 2, 8])
    [1, 1, 2, 2, 3, 3, 6, 8, 8, 10]
    """

    # If the length of the array is less than or equal to 1, then there's
    # nothing to sort, so return the given array
    if len(arr) <= 1:
        return arr

    # In quicksort a element needs to be selected as pivot, it can be anywhere
    # In this case let the pivot be the first element
    pivot = arr[0]

    # Using list comprehension creating three list object: smaller_elemnts,
    # pivot_elements & larger_elements
    # based on the comparison with the pivot element
    smaller_elements = [x for x in arr if x < pivot]
    pivot_elements = [x for x in arr if x == pivot]
    larger_elements = [x for x in arr if x > pivot]

    # Recursively splitting the list object to determine the correct
    # position of the element
    return quicksort(smaller_elements) + pivot_elements + quicksort(larger_elements)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
