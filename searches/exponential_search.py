"""
Python program to find an element x
in a sorted array using Exponential Search

A recursive binary search function returns
location  of x in given array arr[l..r] is
present, otherwise -1
https://en.wikipedia.org/wiki/Exponential_search
"""


def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        return binarySearch(arr, mid + 1, r, x)
    return -1


def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0

    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return binarySearch(arr, i // 2, min(i, n - 1), x)
