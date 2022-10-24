# Find Transition Point
# Given a sorted array containing only 0s and 1s, find the transition point.
# Example
# N = 5
# arr[] = {0,0,0,1,1}
# Output: 3
# Explanation: index 3 is the transition point where 1 begins.

# If in case no trasistion point is found, then we return -1

# Below are Three different Implementations.


def transitionPoint(arr, n):
    # Code here
    # Method1 O(n)
    try:
        return arr.index(1)
    except:
        return -1

    # Method2 O(n)
    for i in range(len(arr)):
        if arr[i] == 1:
            return i
    return -1

    # Method3 O(logn)
    # Binary Search Algo
    if arr[0] == 1:
        return 0
    if arr[-1] == 0:
        return -1
    start = 0
    end = n - 1

    while not start > end:
        mid = (start + end) // 2

        if arr[mid] == 1 and arr[mid - 1] == 0:
            return mid
        if arr[mid] == 0:
            start = mid + 1
        if arr[mid] == 1:
            end = mid - 1
