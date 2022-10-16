# Author:- Arnab Nath
# Python program to find an element x
# in a sorted array using Exponential Search

# A recursive binary search function returns
# location of x in given array arr[l..r] is
# present, otherwise -1
arr = [4, 7, 10, 34, 44, 70]
n = len(arr)
x = 44
if arr[0] == x:
    print("0")
i = 1
# Finding range for binarySearch
while i < n and arr[i] <= x:
    i = i * 2
min1 = min(i, len(arr))


def binarysearch(arr: list, le: int, r: int, x: int) -> int:
    """Pure implementation of binary search algorithm in Python by recursion

    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    First recursion should be started with le=0 and r=(len(arr)-1)
    :param le:left
    :param r:right
    :param arr: some ascending sorted collection with comparable items
    :param x: item value to search
    :return: index of found item or None if item is not found

    Examples:
    >>> binarysearch([0, 5, 7, 10, 15], 0, 4, 0)
    0

    >>> binarysearch([0, 5, 7, 10, 15], 0, 4, 15)
    4

    >>> binarysearch([0, 5, 7, 10, 15], 0, 4, 5)
    1

    """

    if r >= le:
        mid = int(le + (r - le) // 2)

        # If the element is present at
        # the middle itself
        if arr[mid] == x:
            return mid

        # If the element is smaller than mid,
        # then it can only be present in the
        # left subarray
        if arr[mid] > x:
            return binarysearch(arr, le, mid - 1, x)
        # Else he element can only be
        # present in the right
        else:
            return binarysearch(arr, mid + 1, r, x)

    # We reach here if the element is not present
    if r <= le:
        return -1


# Returns the position of first
# occurrence of x in array
index = binarysearch(arr, i // 2, min(i, n), x)
if index == -1:
    print("Element not found")
else:
    print(f"Element found at index {index}")

if __name__ == "__main__":
    import doctest

    doctest.testmod(name="binarysearch", verbose=True)

# URL:- https://www.tutorialspoint.com/Exponential-Search
