from typing import List
import threading
import time


def sleep_sort(numbers: List[int], simulate: bool = True, scale: float = 0.01) -> None:
    """
    Perform Sleep Sort on the given list of integers.

    Sorts the list numbers in place using the Sleep Sort algorithm.

    Behavior:
    - Destructive: modifies the list numbers.
    - Only accepts integers (positive, zero, or negative).
    - Default simulate=True runs instantly by simulating timed wake-ups (safe for tests/CI).
    - If simulate=False, the function spawns one thread per element and uses time.sleep;
      this mode causes real waiting time proportional to element values.
    - scale (seconds per unit) applies only when simulate=False.

    Examples
    --------
    >>> nums = [3, 1, 2]
    >>> sleep_sort(nums)
    >>> nums
    [1, 2, 3]

    >>> nums = [0, 0, 1]
    >>> sleep_sort(nums)
    >>> nums
    [0, 0, 1]

    >>> nums = [-2, 1, 0]
    >>> sleep_sort(nums)
    >>> nums
    [-2, 0, 1]

    >>> sleep_sort([1.5, 2])
    Traceback (most recent call last):
    ...
    TypeError: integers only please
    """
    if not numbers:
        return

    if any(not isinstance(x, int) for x in numbers):
        raise TypeError("integers only please")

    min_val = min(numbers)
    offset = -min_val if min_val < 0 else 0

    if simulate:
        # Simulated wake-up: bucket by wake time (value + offset), preserve order
        buckets = {}
        for idx, val in enumerate(numbers):
            wake = val + offset
            buckets.setdefault(wake, []).append((idx, val))
        result: List[int] = []
        for wake in sorted(buckets.keys()):
            for _, val in buckets[wake]:
                result.append(val)
        numbers[:] = result
        return

    # Real threaded mode: causes actual delays proportional to element values
    results: List[int] = []
    lock = threading.Lock()

    def worker(value: int) -> None:
        time.sleep((value + offset) * scale)
        with lock:
            results.append(value)

    threads: List[threading.Thread] = []
    for val in numbers:
        t = threading.Thread(target=worker, args=(val,))
        t.daemon = True
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    numbers[:] = results
