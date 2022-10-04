"""Iterative approach of binary search.
   Ref : https://en.wikipedia.org/wiki/Binary_search_algorithm

   Time Complexity : O(log n)
   Space Complexity : O(1)
"""


def binary_search(nums: list, k: int, n: int) -> int:
    """This function uses divide & conquer paradigm to find the number in a sorted list and return its index.

    Args:
        nums (list): list of numbers
        k (int): number to be find from the list
        n (int): size of list

    Returns:
        int: index of k or -1 if k is not present in list

    Examples
    --------
    >>> binary_search([1,4,5,6,7],7,5)
    4
    >>> binary_search([1,4,5,6,7],2,5)
    -1
    """

    # Assign left and right pointers with 0 and size of array respectively
    left = 0
    right = n

    # Iterate over the list until left is less than right or k is find
    while left < right:
        # Find the middle within left and right
        mid = (left + right) // 2

        # Base Case
        if nums[mid] == k:
            return mid

        # Update right to mid as element at middle is greater than k
        elif nums[mid] > k:
            right = mid

        # Update left to mid + 1 as element at middle is less than k
        else:
            left = mid + 1

    # Return -1 if k is not present in the list
    return -1


print(binary_search([1, 4, 5, 6, 7], 7, 5))
