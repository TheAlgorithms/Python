"""
This is a pure Python implementation of the sleep algorithm,
In general, sleep sort works by starting a separate task for 
each item to be sorted, where each task sleeps for an interval 
corresponding to the item's sort key, then emits the item. 
Items are then collected sequentially in time. 

More info on: https://rosettacode.org/wiki/Sorting_algorithms/Sleep_sort

For doctests run following command:
python -m doctest -v sleep_sort.py
or
python3 -m doctest -v sleep_sort.py
For manual testing run:
python sleep_sort.py
"""

from time import sleep
from threading import Timer

def sleep_sort(collection):
    """Pure implementation of sleep sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> sleep_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> sleep_sort([0, 5, 2, 3, 2]) == sorted([0, 5, 2, 3, 2])
    True
    >>> sleep_sort([]) == sorted([])
    True
    >>> sleep_sort([2, 15, 5]) == sorted([2, 15, 5])
    True
    >>> sleep_sort([23, 0, 6, 4, 34]) == sorted([23, 0, 6, 4, 34])
    True
    """
    result = []
    
    def append_result(x):
        result.append(x)

    if len(collection) > 0:
        mx = collection[0]
        for v in collection:
            if mx < v: 
                mx = v
            Timer(v, append_result, [v]).start()

        sleep(mx+1)

    return result

if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*sleep_sort(unsorted), sep=",")
    print(f"Processing time: {time.process_time() - start}")