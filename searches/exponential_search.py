"""
Python program to find an element x
in a sorted array using Exponential Search

A recursive binary search function returns
location  of x in given array arr[l..r] is
present, otherwise -1
https://en.wikipedia.org/wiki/Exponential_search
"""


def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)

        return binary_search(arr, mid + 1, r, x)
    return -1


def exponential_search(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return binary_search(arr, i // 2, min(i, n - 1), x)


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    n = len(arr)
    x = 10
    result = exponential_search(arr, n, x)
    if result == -1:
        print("Element not found in the array")
    else:
        print("Element is present at index %d" % (result))
