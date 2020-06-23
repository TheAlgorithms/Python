"""
Sleep sort is probably the wierdest of all sorting functions with time-complexity of
O(max(input)+n) which is quite different from almost all other sorting techniques.
If the number of inputs is small then the complexity can be approximated to be
O(max(input)) which is a constant

If the number of inputs is large, the complexity is approximately O(n).

This function uses multithreading a kind of higher order programming and calls n
functions, each with a sleep time equal to its number. Hence each of function wakes
in sorted time.

This function is not stable for very large values.

https://rosettacode.org/wiki/Sorting_algorithms/Sleep_sort
"""
from threading import Timer
from time import sleep
from typing import List


def sleep_sort(values: List[int]) -> List[int]:
    """
    Sort the list using sleepsort.
    >>> sleep_sort([3, 2, 4, 7, 3, 6, 9, 1])
    [1, 2, 3, 3, 4, 6, 7, 9]
    >>> sleep_sort([3, 2, 1, 9, 8, 4, 2])
    [1, 2, 2, 3, 4, 8, 9]
    """
    sleep_sort.result = []

    def append_to_result(x):
        sleep_sort.result.append(x)

    mx = values[0]
    for value in values:
        if mx < value:
            mx = value
        Timer(value, append_to_result, [value]).start()
    sleep(mx + 1)
    return sleep_sort.result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(sleep_sort([3, 2, 4, 7, 3, 6, 9, 1]))
