# run using python fibonacci_search.py -v

"""
@params
arr: input array
val: the value to be searched
output: the index of element in the array or -1 if not found
return 0 if input array is empty
"""


def fibonacci_search(arr, val):

    """
    >>> fibonacci_search([1,6,7,0,0,0], 6)
    1
    >>> fibonacci_search([1,-1, 5, 2, 9], 10)
    -1
    >>> fibonacci_search([], 9)
    0
    """
    fib_N_2 = 0
    fib_N_1 = 1
    fibNext = fib_N_1 + fib_N_2
    length = len(arr)
    if length == 0:
        return 0
    while fibNext < len(arr):
        fib_N_2 = fib_N_1
        fib_N_1 = fibNext
        fibNext = fib_N_1 + fib_N_2
    index = -1
    while fibNext > 1:
        i = min(index + fib_N_2, (length - 1))
        if arr[i] < val:
            fibNext = fib_N_1
            fib_N_1 = fib_N_2
            fib_N_2 = fibNext - fib_N_1
            index = i
        elif arr[i] > val:
            fibNext = fib_N_2
            fib_N_1 = fib_N_1 - fib_N_2
            fib_N_2 = fibNext - fib_N_1
        else:
            return i
    if (fib_N_1 and index < length - 1) and (arr[index + 1] == val):
        return index + 1
    return -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
