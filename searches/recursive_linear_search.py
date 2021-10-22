"""
    In this solution , we want to use a recursive approach to obtain the
    index of a target element in an array
    For doctests run following command:
    python -m doctest -v recursive_linear_search.py
    or
    python3 -m doctest -v recursive_linear_search.py

    For manual testing run:
    python recursive_linear_search.py
"""


def recursive_linear_search(arr, target, i=0):
    """
    params: `arr` -> array to search from
    params: `target` -> element to look for
    returns: index position of target
    for example:
    >>>  recursive_linear_search([3,2,5,6,7,8,1,9],9)
    7
    >>> recursive_linear_search([3,2,5,6,7,8,1,9],3)
    0
    """
    if len(arr) == 0:
        return -1
    if i == len(arr):
        return -1
    if arr[i] == target:
        return i
    return recursive_linear_search(arr, target, i + 1)


if __name__ == "___main__":
    print(recursive_linear_search([3, 2, 5, 6, 7, 8, 1, 9], 9))
