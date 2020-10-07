"""
This is a pure Python implementation of the sleepsort algorithm.
Sleepsort launches a new thread for each element, which sleeps for
as many seconds as the number, and then appends that number to a common
list.

More info: www.geeksforgeeks.org/sleep-sort-king-laziness-sorting-sleeping

For doctests run following command:
python -m doctest -v sleep_sort.py
or
python3 -m doctest -v sleep_sort.py
For manual testing run:
python sleep_sort.py
"""

import threading
from time import sleep

def sleep_sort(collection):
    """Pure implementation of the sleepsort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> sleep_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> sleep_sort([])
    []
    >>> sleep_sort([-2, -5, -1])
    [-5, -2, -1]
    """

    displacement_coefficient = min(collection) if (min(collection) < 0) else 0
    # modification to deal with negative values 
    # by increasing every value by the smallest value
    # if negative values exist

    sorted_collection = []
    threads = []

    def sleep_sort_helper(i):
        sleep(i - displacement_coefficient)
        sorted_collection.append(i)

    for i in collection:
        args = (i,)
        thread = threading.Thread(target=sleep_sort_helper, args=args)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return sorted_collection

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(sleep_sort(unsorted))
