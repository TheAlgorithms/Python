def stooge_sort(arr):
    """
    Examples:
    >>> stooge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> stooge_sort([])
    []

    >>> stooge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    stooge(arr, 0, len(arr) - 1)
    return arr


def stooge(arr, i, h):

    if i >= h:
        return

    # If first element is smaller than the last then swap them
    if arr[i] > arr[h]:
        arr[i], arr[h] = arr[h], arr[i]

    # If there are more than 2 elements in the array
    if h - i + 1 > 2:
        t = (int)((h - i + 1) / 3)

        # Recursively sort first 2/3 elements
        stooge(arr, i, (h - t))

        # Recursively sort last 2/3 elements
        stooge(arr, i + t, (h))

        # Recursively sort first 2/3 elements
        stooge(arr, i, (h - t))

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(stooge_sort(unsorted))
