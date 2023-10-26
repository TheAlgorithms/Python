""" https://en.wikipedia.org/wiki/Cocktail_shaker_sort """
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


def cocktail_shaker_sort(arr):
    """
    Sorts a list using the Cocktail Shaker Sort algorithm.

    :param arr: List of elements to be sorted.
    :return: Sorted list.
    """
    start, end = 0, len(arr) - 1

    while start < end:
        swapped = False

        # Pass from left to right
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        end -= 1  # Decrease the end pointer after each pass

        # Pass from right to left
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

        if not swapped:
            break

        start += 1  # Increase the start pointer after each pass

    return arr


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    sorted_list = cocktail_shaker_sort(unsorted)
    print(f"Sorted list: {sorted_list}")

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{cocktail_shaker_sort(unsorted) = }")
