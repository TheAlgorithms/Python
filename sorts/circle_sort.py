"""
This is a Python implementation of the circle sort algorithm

For doctests run following command:
python3 -m doctest -v circle_sort.py

For manual testing run:
python3 circle_sort.py
"""


def circle_sort(collection: list) -> list:
    """A pure Python implementation of circle sort algorithm

    :param collection: a mutable collection of comparable items in any order
    :return: the same collection in ascending order

    Examples:
    >>> circle_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> circle_sort([])
    []
    >>> circle_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    >>> collections = ([], [0, 5, 3, 2, 2], [-2, 5, 0, -45])
    >>> all(sorted(collection) == circle_sort(collection) for collection in collections)
    True
    """

    if len(collection) < 2:
        return collection

    def circle_sort_util(collection: list, low: int, high: int) -> bool:
        """
        >>> arr = [5,4,3,2,1]
        >>> circle_sort_util(lst, 0, 2)
        True
        >>> arr
        [3, 4, 5, 2, 1]
        """

        swapped = False

        if low == high:
            return swapped

        left = low
        right = high

        while left < right:
            if collection[left] > collection[right]:
                collection[left], collection[right] = (
                    collection[right],
                    collection[left],
                )
                swapped = True

            left += 1
            right -= 1

        if left == right and collection[left] > collection[right + 1]:
            collection[left], collection[right + 1] = (
                collection[right + 1],
                collection[left],
            )

            swapped = True

        mid = low + int((high - low) / 2)
        left_swap = circle_sort_util(collection, low, mid)
        right_swap = circle_sort_util(collection, mid + 1, high)

        return swapped or left_swap or right_swap

    is_not_sorted = True

    while is_not_sorted is True:
        is_not_sorted = circle_sort_util(collection, 0, len(collection) - 1)

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(circle_sort(unsorted))
