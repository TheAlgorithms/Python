import random
from typing import List


def randomized_quicksort(arr: List[int]) -> List[int]:
    """
    Sorts a list of integers using randomized QuickSort algorithm.

    Args:
        arr (List[int]): List of integers to sort.

    Returns:
        List[int]: Sorted list of integers.

    Examples:
    >>> randomized_quicksort([3, 6, 1, 8, 4])
    [1, 3, 4, 6, 8]
    >>> randomized_quicksort([])
    []
    """
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
