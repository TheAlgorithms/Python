"""Sleepsort is probably the wierdest of all sorting functions
with time-complexity of O(max(input)+n) which is
quite different from almost all other sorting techniques.
If the number of inputs is small then the complexity
can be approximated to be O(max(input)) which is a constant

If the number of inputs is large, the complexity is
approximately O(n).

This function uses multithreading a kind of higher order programming
and calls n functions, each with a sleep time equal to its number.
Hence each of the functions wake in sorted form.

This function is not stable for very large values.

https://rosettacode.org/wiki/Sorting_algorithms/Sleep_sort
"""

from time import sleep
from threading import Timer
from typing import List


def sleepsort(values: List[int]) -> List[int]:
    """
    Sort the list using sleepsort.
    >>> sleepsort([3, 2, 4, 7, 3, 6, 9, 1])
    [1, 2, 3, 3, 4, 6, 7, 9]
    >>> sleepsort([3, 2, 1, 9, 8, 4, 2])
    [1, 2, 2, 3, 4, 8, 9]
    """
    sleepsort.result = []
    def append_to_result(x):
        sleepsort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v:
            mx = v
        Timer(v, append_to_result, [v]).start()
    sleep(mx+1)
    return sleepsort.result
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    x = [3, 2, 4, 7, 3, 6, 9, 1]
    sorted_x = sleepsort(x)
    print(sorted_x)
