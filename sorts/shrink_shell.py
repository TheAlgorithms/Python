"""
This function implements the shell sort algorithm.

Shell sort is a sorting algorithm that works by first sorting
elements that are far apart from each other, and then sorting
elements that are closer together. This reduces the amount of
swapping that needs to be done, and makes the algorithm more
efficient.

The algorithm works by first choosing a 'gap' value. This value
determines how far apart the elements will be that are sorted
first. The gap is then decreased, and the elements are sorted
again. This process is repeated until the gap is 1, at which
point the elements are sorted using insertion sort.

Shell sort is an efficient algorithm that is easy to implement.
It is a good choice for sorting large arrays of data.

"""

def shell_sort(collection: list) -> list:
    """Implementation of shell sort algorithm in Python
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending
    
    >>> shell_sort([3, 2, 1])
    [1, 2, 3]
    >>> shell_sort([])
    []
    >>> shell_sort([1])
    [1]
    """

    # Choose an initial gap value
    gap = len(collection)

    # Set the gap value to be decreased by a factor of 1.3
    # after each iteration
    shrink = 1.3

    # Continue sorting until the gap is 1
    while gap > 1:

        # Decrease the gap value
        gap = int(gap / shrink)

        # Sort the elements using insertion sort
        for i in range(gap, len(collection)):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
            collection[j] = temp

    return collection


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    collection = [int(item) for item in user_input.split(",")]
    print(shell_sort(collection))