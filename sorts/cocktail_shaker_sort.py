""" https://en.wikipedia.org/wiki/Cocktail_shaker_sort """


def cocktail_shaker_sort(unsorted: list) -> list:
    """
    Pure implementation of the cocktail shaker sort algorithm in Python.
    >>> cocktail_shaker_sort([4, 5, 2, 1, 2])
    [1, 2, 2, 4, 5]

    >>> cocktail_shaker_sort([-4, 5, 0, 1, 2, 11])
    [-4, 0, 1, 2, 5, 11]

    >>> cocktail_shaker_sort([0.1, -2.4, 4.4, 2.2])
    [-2.4, 0.1, 2.2, 4.4]

    >>> cocktail_shaker_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    >>> cocktail_shaker_sort([-4, -5, -24, -7, -11])
    [-24, -11, -7, -5, -4]
    """
    for i in range(len(unsorted) - 1, 0, -1):
        swapped = False

        for j in range(i, 0, -1):
            if unsorted[j] < unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                swapped = True

        for j in range(i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swapped = True

        if not swapped:
            break
    return unsorted


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{cocktail_shaker_sort(unsorted) = }")
