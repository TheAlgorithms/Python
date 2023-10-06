def swap(collection, i, j):
    """Swap elements at indices i and j in the collection."""
    collection[i], collection[j] = collection[j], collection[i]

def double_sort(collection):
    """
    This sorting algorithm sorts an array using the principle of bubble sort,
    but does it both from left to right and right to left.
    Hence, it's called "Double sort"

    :param collection: mutable ordered sequence of elements
    :return: the same collection in ascending order

    Examples:
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6 ,-7])
    [-7, -6, -5, -4, -3, -2, -1]
    >>> double_sort([])
    []
    >>> double_sort([-1 ,-2 ,-3 ,-4 ,-5 ,-6])
    [-6, -5, -4, -3, -2, -1]
    >>> double_sort([-3, 10, 16, -42, 29]) == sorted([-3, 10, 16, -42, 29])
    True
    """
    n = len(collection)
    for i in range(n // 2):
        swapped = False

        # Bubble sort from left to right
        for j in range(i, n - i - 1):
            if collection[j] > collection[j + 1]:
                swap(collection, j, j + 1)
                swapped = True

        # Bubble sort from right to left
        for j in range(n - i - 2, i, -1):
            if collection[j] < collection[j - 1]:
                swap(collection, j, j - 1)
                swapped = True

        if not swapped:
            break


if __name__ == "__main__":
    print("Enter the list to be sorted (space-separated integers):")
    input_list = [int(x) for x in input().split()]
    double_sort(input_list)
    print("The sorted list is:")
    print(input_list)