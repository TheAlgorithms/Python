"""
A pure Python implementation of the insertion sort algorithm

This algorithm sorts a collection by comparing adjacent elements.
When it finds that order is not respected, it moves the element compared
backward until the order is correct.  It then goes back directly to the
element's initial position resuming forward comparison.

For doctests run following command:
python3 -m doctest -v insertion_sort.py

For manual testing run:
python3 insertion_sort.py
"""


def insertion_sort(collection: list) -> list:
    """A pure Python implementation of the insertion sort algorithm

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> insertion_sort([])
    []

    >>> insertion_sort([-2, -5, -45])
    [-45, -5, -2]
    """

    for loop_index in range(1, len(collection)):
        insertion_index = loop_index
        while (
            insertion_index > 0
            and collection[insertion_index - 1] > collection[insertion_index]
        ):
            collection[insertion_index], collection[insertion_index - 1] = (
                collection[insertion_index - 1],
                collection[insertion_index],
            )
            insertion_index -= 1

    return collection


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{insertion_sort(unsorted) = }")
