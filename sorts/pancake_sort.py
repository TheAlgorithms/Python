"""
This is a pure python implementation of the pancake sort algorithm
For doctests run following command:
python3 -m doctest -v pancake_sort.py
or
python -m doctest -v pancake_sort.py
For manual testing run:
python pancake_sort.py
"""

def pancake_sort(arr):
    """Sort Array with Pancake Sort.
    :param arr: Collection containing comparable items
    :return: Collection ordered in ascending order of items
    Examples:
    >>> pancake_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> pancake_sort([])
    []
    >>> pancake_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    cur = len(arr)
    while cur > 1:
        # Find the maximum number in arr
        mi = arr.index(max(arr[0:cur]))
        # Reverse from 0 to mi
        arr = arr[mi::-1] + arr[mi + 1:len(arr)]
        # Reverse whole list
        arr = arr[cur - 1::-1] + arr[cur:len(arr)]
        cur -= 1
    return arr


if __name__ == '__main__':
    user_input = input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(pancake_sort(unsorted))
