"""
This is a pure Python implementation of the three partition quick sort algorithm

This algorithm splits at each iteration a mutable ordered collection in 3 parts
1 : elements smaller than the pivot
2 : elements equal to the pivot (not happening in 'simple' quick sort)
3 : elements greater than the pivot

For doctests run following command:
python -m doctest -v quick_sort_3partition.py
or
python3 -m doctest -v quick_sort_3partition.py

For manual testing run:
python quick_sort_3partition.py
"""


def quick_sort_3partition(my_list: list, left: int = 0, right: int = None) -> list:
    """
    Implementation of quick sort algorithm, 3-Way variation.

    Examples:
    >>> quick_sort_3partition([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]

    >>> quick_sort_3partition([])
    []

    >>> quick_sort_3partition([-2, -5, -45])
    [-45, -5, -2]
    """
    if right is None:
        right = len(my_list) - 1
    if right <= left:
        return my_list
    i: int = left
    temp_left: int = left
    temp_right: int = right
    # Use the first element as pivot
    pivot: int = my_list[left]
    while i <= temp_right:
        if my_list[i] < pivot:
            # Permute current element with leftmost element of the current sublist
            my_list[temp_left], my_list[i] = my_list[i], my_list[temp_left]
            temp_left += 1
            i += 1
        elif my_list[i] > pivot:
            # Permute current element with rightmost element of the current sublist
            my_list[temp_right], my_list[i] = my_list[i], my_list[temp_right]
            temp_right -= 1
        else:
            # Current element is equal to the pivot
            i += 1
    quick_sort_3partition(my_list, left, temp_left - 1)
    quick_sort_3partition(my_list, temp_right + 1, right)
    return my_list


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort_3partition(unsorted))
