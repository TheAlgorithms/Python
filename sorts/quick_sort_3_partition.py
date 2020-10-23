def quick_sort_3partition(sorting: list, left: int, right: int) -> None:
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
