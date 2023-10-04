"""
This function implements the shell sort algorithm
which is slightly faster than its pure implementation.

This shell sort is implemented using a gap, which
shrinks by a certain factor each iteration. In this
implementation, the gap is initially set to the
length of the collection. The gap is then reduced by
a certain factor (1.3) each iteration.

For each iteration, the algorithm compares elements
that are a certain number of positions apart
(determined by the gap). If the element at the higher
position is greater than the element at the lower
position, the two elements are swapped. The process
is repeated until the gap is equal to 1.

The reason this is more efficient is that it reduces
the number of comparisons that need to be made. By
using a smaller gap, the list is sorted more quickly.
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
