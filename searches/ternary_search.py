"""
This is a type of divide and conquer algorithm which divides the search space into
3 parts and finds the target value based on the property of the array or list
(usually monotonic property).

Time Complexity  : O(log3 N)
Space Complexity : O(1)
"""
from typing import List

# This is the precision for this function which can be altered.
# It is recommended for users to keep this number greater than or equal to 10.
precision = 10


# This is the linear search that will occur after the search space has become smaller.

def lin_search(left: int, right: int, A: List[int], target: int) -> int:
    """Perform linear search in list. Returns -1 if element is not found.

    Parameters
    ----------
    left : int
        left index bound.
    right : int
        right index bound.
    A : List[int]
        List of elements to be searched on
    target : int
        Element that is searched

    Returns
    -------
    int
        index of element that is looked for.

    Examples
    --------
    >>> print(lin_search(0, 4, [4, 5, 6, 7], 7))
    3
    >>> print(lin_search(0, 3, [4, 5, 6, 7], 7))
    -1
    >>> print(lin_search(0, 2, [-18, 2], -18))
    0
    >>> print(lin_search(0, 1, [5], 5))
    0
    >>> print(lin_search(0, 3, ['a', 'c', 'd'], 'c'))
    1
    >>> print(lin_search(0, 3, [.1, .4 , -.1], .1))
    0
    >>> print(lin_search(0, 3, [.1, .4 , -.1], -.1))
    2
    """
    for i in range(left, right):
        if A[i] == target:
            return i
    return -1


def ite_ternary_search(A: List[int], target: int) -> int:
    """Iterative method of the ternary search algorithm.
    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> print(ite_ternary_search(test_list, 3))
    -1
    >>> print(ite_ternary_search(test_list, 13))
    4
    >>> print(ite_ternary_search([4, 5, 6, 7], 4))
    0
    >>> print(ite_ternary_search([4, 5, 6, 7], -10))
    -1
    >>> print(ite_ternary_search([-18, 2], -18))
    0
    >>> print(ite_ternary_search([5], 5))
    0
    >>> print(ite_ternary_search(['a', 'c', 'd'], 'c'))
    1
    >>> print(ite_ternary_search(['a', 'c', 'd'], 'f'))
    -1
    >>> print(ite_ternary_search([], 1))
    -1
    >>> print(ite_ternary_search([.1, .4 , -.1], .1))
    0
    """

    left = 0
    right = len(A)
    while left <= right:
        if right - left < precision:
            return lin_search(left, right, A, target)

        oneThird = (left + right) / 3 + 1
        twoThird = 2 * (left + right) / 3 + 1

        if A[oneThird] == target:
            return oneThird
        elif A[twoThird] == target:
            return twoThird

        elif target < A[oneThird]:
            right = oneThird - 1
        elif A[twoThird] < target:
            left = twoThird + 1

        else:

            left = oneThird + 1
            right = twoThird - 1
    else:
        return -1


def rec_ternary_search(left: int, right: int, A: List[int], target: int) -> int:
    """Recursive method of the ternary search algorithm.

    >>> test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    >>> print(rec_ternary_search(0, len(test_list), test_list, 3))
    -1
    >>> print(rec_ternary_search(4, len(test_list), test_list, 42))
    8
    >>> print(rec_ternary_search(0, 2, [4, 5, 6, 7], 4))
    0
    >>> print(rec_ternary_search(0, 3, [4, 5, 6, 7], -10))
    -1
    >>> print(rec_ternary_search(0, 1, [-18, 2], -18))
    0
    >>> print(rec_ternary_search(0, 1, [5], 5))
    0
    >>> print(rec_ternary_search(0, 2, ['a', 'c', 'd'], 'c'))
    1
    >>> print(rec_ternary_search(0, 2, ['a', 'c', 'd'], 'f'))
    -1
    >>> print(rec_ternary_search(0, 0, [], 1))
    -1
    >>> print(rec_ternary_search(0, 3, [.1, .4 , -.1], .1))
    0
    """
    if left < right:
        if right - left < precision:
            return lin_search(left, right, A, target)
        oneThird = (left + right) / 3 + 1
        twoThird = 2 * (left + right) / 3 + 1

        if A[oneThird] == target:
            return oneThird
        elif A[twoThird] == target:
            return twoThird

        elif target < A[oneThird]:
            return rec_ternary_search(left, oneThird - 1, A, target)
        elif A[twoThird] < target:
            return rec_ternary_search(twoThird + 1, right, A, target)
        else:
            return rec_ternary_search(oneThird + 1, twoThird - 1, A, target)
    else:
        return -1



if __name__ == "__main__":
    user_input = input("Enter numbers separated by comma:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]
    assert collection == sorted(collection), f"List must be ordered.\n{collection}."
    target = int(input("Enter the number to be found in the list:\n").strip())
    result1 = ite_ternary_search(collection, target)
    result2 = rec_ternary_search(0, len(collection) - 1, collection, target)
    if result2 != -1:
        print(f"Iterative search: {target} found at positions: {result1}")
        print(f"Recursive search: {target} found at positions: {result2}")
    else:
        print("Not found")
