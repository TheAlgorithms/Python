# sorts/sleep_sort.py
from __future__ import annotations

import threading
import time
from typing import List


def sleep_sort(arr: List[int]) -> List[int]:
    """
    "Sorts" a list by sleeping for each value's duration.
    Fun demo – **not** for production!

    >>> import random; random.seed(42)
    >>> sleep_sort([3, 1, 4, 1, 5])
    [1, 1, 3, 4, 5]
    >>> sleep_sort([])
    []
    >>> sleep_sort([42])
    [42]
    """
    if not arr:
        return []

    result: List[int] = []

    def sleeper(value: int) -> None:
        time.sleep(value / 1000.0)  # scale down for fast tests
        result.append(value)

    threads = [threading.Thread(target=sleeper, args=(x,)) for x in arr]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
