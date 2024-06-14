"""
https://en.wikipedia.org/wiki/Natural_sort_order

In computing, natural sort order (or natural sorting) is the ordering
of strings in alphabetical order, except that multi-digit numbers are
treated atomically, i.e., as if they were a single character.
Natural sort order has been promoted as being more human-friendly
("natural") than machine-oriented, pure alphabetical sort order.

For example, in alphabetical sorting, "z11" would be sorted before
"z2" because the "1" in the first string is sorted as smaller
than "2", while in natural sorting "z2" is sorted before "z11"
because "2" is treated as smaller than "11".

Alphabetical sorting:
1.z11
2.z2

Natural sorting:
1. z2
2. z11
"""

from collections.abc import Iterable


def alpha_numerical_sort(unsorted: Iterable) -> Iterable:
    """
    This function is used to alpha numerical sort an unsorted
    iterable as a list or a set
    Args:
        unsorted: Iterable object
    Returns:
        Iterable object alpha numerical sorted
    Examples:
    >>> alpha_numerical_sort(['k', 5, 'e', 3, 'g', 7, 0, 't'])
    [0, 3, 5, 7, 'e', 'g', 'k', 't']
    >>> alpha_numerical_sort(['z2', 'z11'])
    ['z11', 'z2']
    """

    # separate into two lists one for Numbers only and other of Strings only
    num_list = []
    str_list = []

    # fill each list
    for i in unsorted:
        if isinstance(i, str):
            str_list.append(i)
        else:
            num_list.append(i)

    # sort, separately, each list
    num_list = sorted(num_list)
    str_list = sorted(str_list)

    # combine those two together and return
    return num_list + str_list


if __name__ == "__main__":
    user_input = input("Enter alphanumeric elements separated by a comma:\n").strip()
    unsorted = user_input.split(",")
    print(alpha_numerical_sort(unsorted))
