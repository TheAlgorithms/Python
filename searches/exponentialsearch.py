# Author:- Arnab Nath
# Python program to find an element x
# in a sorted array using Exponential Search

# A recursive binary search function returns
# location of x in given array arr[l..r] is
# present, otherwise -1
def binarysearch(arr: list, x: int, l: int, r: int) -> int:
    """Pure implementation of binary search algorithm in Python by recursion

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    First recursion should be started with l=0 and r=(len(arr)-1)
    :param l:
    :param arr: some ascending sorted collection with comparable items
    :param x: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binarysearch([0, 5, 7, 10, 15], 0, 0, 4)
    0

    >>> binarysearch([0, 5, 7, 10, 15], 15, 0, 4)
    4

    >>> binarysearch([0, 5, 7, 10, 15], 5, 0, 4)
    1

    """

    if r >= l:
        mid = l + (r - l) // 2

        # If the element is present at
        # the middle itself
        if arr[mid] == x:
            return mid

        # If the element is smaller than mid,
        # then it can only be present in the
        # left subarray
        if arr[mid] > x:
            return binarysearch(arr, x, l, mid - 1)

        # Else he element can only be
        # present in the right
        return binarysearch(arr, x, mid + 1, r)

    # We reach here if the element is not present
    return -1


# Returns the position of first
# occurrence of x in array


def exponentialsearch(arr: list, n: int, x: int):
    # IF x is present at first
    # location itself
    if arr[0] == x:
        return 0

    # Find range for binary search
    # j by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # Call binary search for the found range
    return binarysearch(arr, x, i // 2, min(i, n - 1))


# Driver Code
arr = [4, 7, 10, 34, 44, 70]
n = len(arr)
x = 44
result = exponentialsearch(arr, n, x)
if result == -1:
    print("Element not found in the array")
else:
    print("Element is present at index %d" % (result))


if __name__ == "__main__":
    import doctest

    doctest.testmod(name="binarysearch", verbose=True)

# URL:- https://www.tutorialspoint.com/Exponential-Search
