"""
This is a python implementation of the exponential search algorithm.
This algorithm is an improved version of binary search
Here instead of applying binary search on whole input we find
    an interval using exponentiation and apply binary search on it.
It is useful for unbounded/infinite lists

https://en.wikipedia.org/wiki/Exponential_search
"""


def binary_search(sequence: list, left: int, right:int, key:int) -> int:
    """
    This is a python implementation of recursive binary search algorithm.

    :param sequence: An ascending sorted list of numbers
    :param left: Start of the interval where our element is predicted to be present.
    :param right: End of the interval where our element is predicted to be present.
    :param key: Value to search

    Examples:
    >>> binary_search([0, 5, 7, 10, 15, 21, 29, 35], 0, 7, 5)
    1

    >>> binary_search([0, 5, 7, 10, 15, 21, 29, 35], 4, 7, 21)
    5

    >>> binary_search([0, 5, 7, 10, 15, 21, 29, 35], 4, 7, 23)
    -1

    >>> binary_search([0, 5, 7, 10, 15, 21, 29, 35], 4, 7, 29)
    6

    """
    if right >= left:
        mid = left + (right-left) // 2
        if sequence[mid] == key:
            return mid
        elif sequence[mid] > key:
            return binary_search(sequence, left, mid-1, key)
        elif sequence[mid] < key:
            return binary_search(sequence, mid+1, right, key)
    
    # Element is not present in the sequence
    return -1


def exp_search(sequence: list, key:int) -> int:
    """
    This is the exponential search method used to find the interval.
    We start with 1 and then each time multiplies it by 2 till the time
        we are in the range of our sequence and element present at start 
        of interval is less than or equal to our key.

    Be careful that the sequence must be a collection of sorted numbers, otherwise
    the algorithm will give incorrect outputs.

    :param sequence: An ascending sorted list of numbers
    :param key: Value to search
    :return: Index of the found value or -1 if value is not present in the sequence

    Examples:
    >>> exp_search([0, 5, 7, 10, 15, 21, 29, 35], 5)
    1

    >>> exp_search([0, 5, 7, 10, 15, 21, 29, 35], 21)
    5

    >>> exp_search([0, 5, 7, 10, 15, 21, 29, 35], 23)
    -1

    >>> exp_search([0, 5, 7, 10, 15, 21, 29, 35], 29)
    6
    """
    if sequence[0] == key:
        return 0
    
    start_interval = 1
    n = len(sequence)
    
    while start_interval < n and sequence[start_interval] <= key:
        start_interval *= 2
    
    result = binary_search(sequence, start_interval // 2, min(start_interval, n-1), key)

    return result


if __name__ == '__main__':
    user_input = input("Enter numbers separated by a comma in an ascending order:\n").strip()
    sequence = [int(item) for item in user_input.split(",")]
    key = int(input("Enter the value to be searched:\n"))
    result = exp_search(sequence, key)
    if result == -1:
        print("Value not found!")
    else:
        print(f"Value {key} is at index {result}")