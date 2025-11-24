import heapq
from typing import List, Union


def kth_largest_element(
    arr: List[Union[int, float, str]], k: int
) -> Union[int, float, str]:
    """
    Finds the kth largest element in an array using a heap.

    Args:
        arr: List of numbers or strings.
        k: The position of the desired kth largest element.

    Returns:
        The kth largest element.

    Raises:
        ValueError: If k is invalid or not an integer.

    Examples:
        >>> kth_largest_element([3, 1, 4, 1, 5, 9], 2)
        5
        >>> kth_largest_element([9, 7, 5, 3, 1], 1)
        9
        >>> kth_largest_element([1, 2, 3], 3)
        1
        >>> kth_largest_element([], 1)
        Traceback (most recent call last):
        ...
        ValueError: Invalid value of 'k'
        >>> kth_largest_element([1, 2, 3], -2)
        Traceback (most recent call last):
        ...
        ValueError: Invalid value of 'k'
    """
    if not isinstance(k, int):
        raise ValueError("The position should be an integer")
    if not 1 <= k <= len(arr):
        raise ValueError("Invalid value of 'k'")

    # Use heapq.nlargest to directly get k largest, then pick the last
    return heapq.nlargest(k, arr)[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
