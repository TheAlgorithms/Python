# Sleep sort (novelty) implementation
# This provides a fast simulated mode (default) plus an optional real threaded mode.

from typing import List
import threading
import time


def sleep_sort(a: List[int], simulate: bool = True, scale: float = 0.01) -> None:
    """
    Sort the list a in-place using the sleep sort idea.

    Behavior:
    - Destructive: modifies list a.
    - Only accepts integers (positive, zero, or negative).
    - Default simulate=True runs instantly by simulating timed wake-ups (safe for tests/CI).
    - If simulate=False the function spawns one thread per element and uses time.sleep;
      use that mode only for small inputs (and beware of real waiting).
    - scale (seconds per unit) applies only when simulate=False.

    >>> a = [3, 1, 2]
    >>> b = sorted(a)
    >>> sleep_sort(a)  # simulated, fast
    >>> a == b
    True

    >>> a = [0, 0, 1]
    >>> sleep_sort(a)
    >>> a
    [0, 0, 1]

    >>> a = [-2, 1, 0]
    >>> sleep_sort(a)
    >>> a == sorted([-2, 1, 0])
    True

    >>> sleep_sort([1.5, 2])  # non-integers not allowed
    Traceback (most recent call last)
    ...
    TypeError: integers only please
    """
    # quick no-op for empty
    if not a:
        return

    # type checks
    if any(not isinstance(x, int) for x in a):
        raise TypeError("integers only please")

    # handle negatives by offsetting so all "sleep times" are non-negative
    min_val = min(a)
    offset = -min_val if min_val < 0 else 0

    if simulate:
        # Simulated wake-up: bucket by wake time (value + offset), preserve original order
        buckets = {}
        for idx, val in enumerate(a):
            wake = val + offset
            buckets.setdefault(wake, []).append((idx, val))
        result: List[int] = []
        for wake in sorted(buckets.keys()):
            # append in original order to make stable when values equal
            for _, val in buckets[wake]:
                result.append(val)
        a[:] = result
        return

    # Real threaded mode (be careful: this actually sleeps)
    results: List[int] = []
    lock = threading.Lock()

    def worker(value: int) -> None:
        # sleep proportional to value (after offset), then append to results
        time.sleep((value + offset) * scale)
        with lock:
            results.append(value)

    threads: List[threading.Thread] = []
    for val in a:
        t = threading.Thread(target=worker, args=(val,))
        t.daemon = True
        t.start()
        threads.append(t)

    # wait for threads to finish
    for t in threads:
        t.join()

    # results is in the order threads woke up
    a[:] = results


def main() -> None:
    a = [8, 3, 2, 7, 4, 6, 8]
    sleep_sort(a)  # simulated (fast)
    print("Sorted order is:", " ".join(map(str, a)))


if __name__ == "__main__":
    main()
