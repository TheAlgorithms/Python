"""

This will locate the item desired from a list which has been rotated
around a pivot. So, the array is sorted, but just with two seperate, 
increasing sections, with list[0] > list[len(list)-1]. It finds the 
desired item via binary search. Would be prefered if the sorted_collection
contained no repeats.


Resource w/ psuedocode: https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
Used the psuedocode from the Improved section to write out code.

"""

from __future__ import annotations


def rotated_binary_search(sorted_collection: list[int], item: int, low: int, high: int) -> int:
    """
    :param sorted_collection: the rotated list we would like to find the item within
    :param item: the item to be found within the sorted_collection
    :param low: for the binary search, the lowest index on the current search - initially 0
    :param high: for the binary search, the highest index on the current search - initially the length of sorted_collection - 1
    :return: index i that item appears in sequence

    Examples:
    >>> rotated_binary_search([5, 6, 7, 1, 2, 3], 8, 0, 5)
    -1

    >>> rotated_binary_search([11, 12, 1, 2, 3, 4, 5, 6], 5, 0, 7)
    6

    >>> rotated_binary_search([11, 12, 13, 16, 20, 2], 2, 0, 5)
    5

    >>> rotated_binary_search([20, 21, 1, 2, 3], 20, 0, 4)
    0

    """

    mid = int((high + low) / 2)
    if sorted_collection[mid] == item:  # found the item
        return mid
    if low >= high:  # couldn't find the item
        return -1
    elif sorted_collection[low] < sorted_collection[mid]:
        if (item <= sorted_collection[mid]) and (item >= sorted_collection[low]):
            return rotated_binary_search(sorted_collection, item, low, mid)
        else:
            return rotated_binary_search(sorted_collection, item, mid + 1, high)
    else:
        if (item <= sorted_collection[high]) and (item >= sorted_collection[mid + 1]):
            return rotated_binary_search(sorted_collection, item, mid + 1, high)
        else:
            return rotated_binary_search(sorted_collection, item, low, mid)


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    user_input = input("Enter rotated numbers separated by comma:\n").strip()
    inputs = [int(item.strip()) for item in user_input.split(",")]

    item = int(input("Enter a single number to be found in the list:\n").strip())
    index = rotated_binary_search(inputs, item, 0, len(inputs) - 1)

    if index != -1:
        print(f"{item} was found in {inputs} at position {index}")
    else:
        print(f"{item} was not found in {inputs}")