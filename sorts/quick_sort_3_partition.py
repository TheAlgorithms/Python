import random


def quick_sort_3partition(sorting: list, left: int, right: int) -> None:
    """ "
    Python implementation of quick sort algorithm with 3-way partition.
    The idea of 3-way quick sort is based on "Dutch National Flag algorithm".

    :param sorting: sort list
    :param left: left endpoint of sorting
    :param right: right endpoint of sorting
    :return: None

    Examples:
    >>> array1 = [5, -1, -1, 5, 5, 24, 0]
    >>> quick_sort_3partition(array1, 0, 6)
    >>> array1
    [-1, -1, 0, 5, 5, 5, 24]
    >>> array2 = [9, 0, 2, 6]
    >>> quick_sort_3partition(array2, 0, 3)
    >>> array2
    [0, 2, 6, 9]
    >>> array3 = []
    >>> quick_sort_3partition(array3, 0, 0)
    >>> array3
    []
    """
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)


def quick_sort_lomuto_partition(sorting: list, left: int, right: int) -> None:
    """
    A pure Python implementation of quick sort algorithm(in-place)
    with Lomuto partition scheme:
    https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme

    :param sorting: sort list
    :param left: left endpoint of sorting
    :param right: right endpoint of sorting
    :return: None

    Examples:
    >>> nums1 = [0, 5, 3, 1, 2]
    >>> quick_sort_lomuto_partition(nums1, 0, 4)
    >>> nums1
    [0, 1, 2, 3, 5]
    >>> nums2 = []
    >>> quick_sort_lomuto_partition(nums2, 0, 0)
    >>> nums2
    []
    >>> nums3 = [-2, 5, 0, -4]
    >>> quick_sort_lomuto_partition(nums3, 0, 3)
    >>> nums3
    [-4, -2, 0, 5]
    """
    if left < right:
        pivot_index = lomuto_partition(sorting, left, right)
        quick_sort_lomuto_partition(sorting, left, pivot_index - 1)
        quick_sort_lomuto_partition(sorting, pivot_index + 1, right)


def lomuto_partition(sorting: list, left: int, right: int) -> int:
    """
    Example:
    >>> lomuto_partition([1,5,7,6], 0, 3)
    2
    """
    pivot = sorting[right]
    store_index = left
    for i in range(left, right):
        if sorting[i] < pivot:
            sorting[store_index], sorting[i] = sorting[i], sorting[store_index]
            store_index += 1
    sorting[right], sorting[store_index] = sorting[store_index], sorting[right]
    return store_index


def hoare_partition_by_value(
    array: list, pivot_value: int, start: int = 0, end: int | None = None
) -> int:
    """
    Returns the starting index of the right subarray, which contains the
    elements greater than or equal to `pivot_value`

    >>> list_unsorted = [7, 3, 5, 4, 1, 8, 6]
    >>> array = list_unsorted.copy()
    >>> hoare_partition_by_value(array, 5)
    3
    >>> array
    [1, 3, 4, 5, 7, 8, 6]

    Edge cases:
    >>> hoare_partition_by_value(list_unsorted.copy(), 0)
    0
    >>> hoare_partition_by_value(list_unsorted.copy(), 1)
    0
    >>> hoare_partition_by_value(list_unsorted.copy(), 2)
    1
    >>> hoare_partition_by_value(list_unsorted.copy(), 8)
    6
    >>> hoare_partition_by_value(list_unsorted.copy(), 9)
    7

    """
    if end is None:
        end = len(array) - 1

    left = start
    right = end

    while True:
        """
        In an intermediate iteration, state could look like this:

            lllluuuuuuuuuurrrrr
                ^        ^
                |        |
              left      right

        Where the middle values are [u]nknown, since they are not yet traversed.
        `left-1` points to the end of the left subarray.
        `right+1` points to the start of the right subarray.
        """

        while array[left] < pivot_value:
            left += 1
            if left > end:
                # Right subarray is empty.
                # Signal it by returning an index out of bounds.
                return end + 1
        while array[right] >= pivot_value:
            right -= 1
            if right < start:
                # Left subarray is empty
                return start

        if left > right:
            break

        # Invariants:
        assert all(i < pivot_value for i in array[start:left])
        assert all(i >= pivot_value for i in array[right + 1 : end])
        """
            llllllruuuuulrrrrrr
                  ^     ^
                  |     |
                left   right
        """

        # Swap
        array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1

    return right + 1


def hoare_partition_by_pivot(
    array: list, pivot_index: int, start=0, end: int | None = None
) -> int:
    """
    Returns the new pivot index after partitioning

    >>> array = [7, 3, 5, 4, 1, 8, 6]
    >>> array[3]
    4
    >>> hoare_partition_by_pivot(array, 3)
    2
    >>> array
    [1, 3, 4, 6, 7, 8, 5]
    """
    if end is None:
        end = len(array) - 1

    def swap(i1, i2):
        array[i1], array[i2] = array[i2], array[i1]

    pivot_value = array[pivot_index]
    swap(pivot_index, end)
    greater_or_equal = hoare_partition_by_value(
        array, pivot_value, start=start, end=end - 1
    )
    swap(end, greater_or_equal)
    return greater_or_equal


def quicksort_hoare(array: list, start: int = 0, end: int | None = None):
    """
    Quicksort using the Hoare partition scheme:
    - https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
    - The Art of Computer Programming, Volume 3: Sorting and Searching

    >>> array = [2, 2, 8, 0, 3, 7, 2, 1, 8, 8]
    >>> quicksort_hoare(array)
    >>> array
    [0, 1, 2, 2, 2, 3, 7, 8, 8, 8]
    """
    if end is None:
        end = len(array) - 1

    if end + 1 - start <= 1:
        return

    pivot_index = random.randrange(start, end)
    pivot_index_final = hoare_partition_by_pivot(array, pivot_index, start, end)
    quicksort_hoare(array, start, pivot_index_final - 1)
    quicksort_hoare(array, pivot_index_final + 1, end)


def three_way_radix_quicksort(sorting: list) -> list:
    """
    Three-way radix quicksort:
    https://en.wikipedia.org/wiki/Quicksort#Three-way_radix_quicksort
    First divide the list into three parts.
    Then recursively sort the "less than" and "greater than" partitions.

    >>> three_way_radix_quicksort([])
    []
    >>> three_way_radix_quicksort([1])
    [1]
    >>> three_way_radix_quicksort([-5, -2, 1, -2, 0, 1])
    [-5, -2, -2, 0, 1, 1]
    >>> three_way_radix_quicksort([1, 2, 5, 1, 2, 0, 0, 5, 2, -1])
    [-1, 0, 0, 1, 1, 2, 2, 2, 5, 5]
    """
    if len(sorting) <= 1:
        return sorting
    return (
        three_way_radix_quicksort([i for i in sorting if i < sorting[0]])
        + [i for i in sorting if i == sorting[0]]
        + three_way_radix_quicksort([i for i in sorting if i > sorting[0]])
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    quick_sort_3partition(unsorted, 0, len(unsorted) - 1)
    print(unsorted)
