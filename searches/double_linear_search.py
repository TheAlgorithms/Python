from __future__ import annotations


def double_linear_search(array: list[int], search_item: int) -> int:
    """
    Iterate through the array from both sides to find the index of search_item.

    This algorithm searches for a target value from both the start and end of the
    array simultaneously, converging toward the middle. It returns the index of the
    first match found (prioritizing from the start when both ends match simultaneously).

    :param array: the array to be searched
    :param search_item: the item to be searched
    :return the index of search_item, if search_item is in array, else -1

    Examples:
    >>> double_linear_search([1, 5, 5, 10], 1)
    0
    >>> double_linear_search([1, 5, 5, 10], 5)
    1
    >>> double_linear_search([1, 5, 5, 10], 100)
    -1
    >>> double_linear_search([1, 5, 5, 10], 10)
    3

    >>> double_linear_search([], 1)
    -1

    >>> double_linear_search([42], 42)
    0

    >>> double_linear_search([42], 99)
    -1

    >>> double_linear_search([1, 2, 3, 4, 5], 3)
    2

    >>> double_linear_search([1, 2, 3, 4, 5], 1)
    0

    >>> double_linear_search([1, 2, 3, 4, 5], 5)
    4

    >>> double_linear_search([10, 10, 10, 10], 10)
    0

    >>> double_linear_search([-5, -2, 0, 3, 7], -5)
    0

    >>> double_linear_search([-5, -2, 0, 3, 7], 0)
    2

    >>> double_linear_search([-5, -2, 0, 3, 7], 7)
    4

    >>> double_linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    4

    >>> double_linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    8

    >>> double_linear_search([100, 200, 300, 400], 250)
    -1
    """
    # define the start and end index of the given array
    start_ind, end_ind = 0, len(array) - 1
    while start_ind <= end_ind:
        if array[start_ind] == search_item:
            return start_ind
        elif array[end_ind] == search_item:
            return end_ind
        else:
            start_ind += 1
            end_ind -= 1
    # returns -1 if search_item is not found in array
    return -1


if __name__ == "__main__":
    print(double_linear_search(list(range(100)), 40))
