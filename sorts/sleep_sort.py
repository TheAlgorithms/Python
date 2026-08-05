"""
An implementation of Sleep Sort.

Description
-----------
Sleep Sort is a highly unconventional algorithm that leverages timing delays
to produce a sorted sequence. Each element in the array is assigned to a thread
that sleeps for a duration proportional to its value. As threads "wake up,"
they output numbers in increasing order.

This algorithm only works for non-negative integers and is non-deterministic
in real systems due to thread scheduling and timing inaccuracies.

Time complexity: O(n) expected (but unreliable in practice)
Space complexity: O(n) for thread management
"""

import threading
import time
from typing import List


def sleep_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of non-negative integers using the Sleep Sort algorithm.

    Parameters
    ----------
    arr : List[int]
        A list of non-negative integers to be sorted.

    Returns
    -------
    List[int]
        A new list containing the elements in sorted order.

    Example
    -------
    >>> sleep_sort([3, 1, 2])
    [1, 2, 3]
    """
    if not arr:
        return []

    result: List[int] = []
    threads = []

    def _sleep_and_append(n: int) -> None:
        """Sleeps for n * 0.01 seconds and appends n to the result."""
        time.sleep(n * 0.01)
        result.append(n)

    for num in arr:
        if num < 0:
            raise ValueError("Sleep Sort only supports non-negative integers.")
        thread = threading.Thread(target=_sleep_and_append, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


def _test() -> None:
    """Basic test cases for sleep_sort."""
    test_cases = [
        [],
        [1],
        [3, 1, 2],
        [0, 0, 1],
        [5, 3, 9, 1, 4],
    ]

    for case in test_cases:
        sorted_case = sorted(case)
        assert sleep_sort(case) == sorted_case, f"Failed on {case}"
    print("All tests passed.")


if __name__ == "__main__":
    _test()
