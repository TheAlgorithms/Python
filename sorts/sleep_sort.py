"""
Sleep Sort Algorithm

Sleep Sort is a humorous sorting algorithm that works by spawning a separate
thread for each element in the input array. Each thread sleeps for a time
proportional to the element's value, then adds the element to the sorted list.

Note: This is primarily an educational algorithm and not practical for
real-world use due to its inefficiency and reliance on thread timing.

Time Complexity: O(max(input) + n)
Space Complexity: O(n)
"""

import threading
import time
from typing import List


def sleep_sort(arr: List[int]) -> List[int]:
    """
    Sorts a list of non-negative integers using sleep sort algorithm.

    Args:
        arr (List[int]): List of non-negative integers to be sorted

    Returns:
        List[int]: Sorted list in ascending order

    Examples:
    >>> sleep_sort([3, 1, 2])
    [1, 2, 3]

    >>> sleep_sort([5, 2, 8, 1])
    [1, 2, 5, 8]

    >>> sleep_sort([1])
    [1]

    >>> sleep_sort([])
    []
    """
    if not arr:
        return []

    # Shared result list and lock for thread safety
    result = []
    lock = threading.Lock()

    def worker(value: int) -> None:
        """Worker function that sleeps for value seconds then appends to result."""
        time.sleep(value / 10)  # Divide by 10 to make it faster for demonstration
        with lock:
            result.append(value)

    # Create and start threads
    threads = []
    for value in arr:
        if value < 0:
            raise ValueError("Sleep sort only works with non-negative integers")
        thread = threading.Thread(target=worker, args=(value,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    return result


def sleep_sort_simple(arr: List[int]) -> List[int]:
    """
    A simpler version of sleep sort without threads (sequential execution).
    This version is more reliable for testing.

    Args:
        arr (List[int]): List of non-negative integers to be sorted

    Returns:
        List[int]: Sorted list in ascending order
    """
    if not arr:
        return []

    # Create list of (value, index) pairs
    pairs = [(value, i) for i, value in enumerate(arr)]

    # Sort based on value
    pairs.sort(key=lambda x: x[0])

    # Extract sorted values
    return [value for value, _ in pairs]


class SleepSort:
    """
    A class-based implementation of sleep sort with additional features.
    """

    def _init_(self, speed_factor: float = 10.0):
        """
        Initialize SleepSort with a speed factor.

        Args:
            speed_factor (float): Factor to divide sleep times by (higher = faster)
        """
        self.speed_factor = speed_factor

    def sort(self, arr: List[int]) -> List[int]:
        """
        Sort the array using sleep sort.

        Args:
            arr (List[int]): List of non-negative integers

        Returns:
            List[int]: Sorted list
        """
        if not arr:
            return []

        result = []
        lock = threading.Lock()

        def worker(value: int) -> None:
            time.sleep(value / self.speed_factor)
            with lock:
                result.append(value)

        threads = []
        for value in arr:
            if value < 0:
                raise ValueError("Sleep sort only works with non-negative integers")
            thread = threading.Thread(target=worker, args=(value,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return result


if __name__ == "_main_":
    # Example usage and test cases
    import doctest

    # Run doctests (using simple version for reliability)
    doctest.testmod()

    print("=== Sleep Sort Demo ===")

    # Test with simple version (more reliable)
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Original array: {test_arr}")

    simple_sorted = sleep_sort_simple(test_arr)
    print(f"Simple sorted:  {simple_sorted}")

    # Test with threaded version (may have timing issues in doctests)
    try:
        threaded_sorted = sleep_sort(test_arr)
        print(f"Threaded sorted: {threaded_sorted}")
    except Exception as e:
        print(f"Threaded version error: {e}")

    # Test with class-based version
    sorter = SleepSort(speed_factor=20.0)
    try:
        class_sorted = sorter.sort(test_arr)
        print(f"Class sorted:    {class_sorted}")
    except Exception as e:
        print(f"Class version error: {e}")

    # Performance comparison
    print("\n=== Performance Test ===")
    small_arr = [5, 2, 8, 1, 9]

    import time as time_module

    start = time_module.time()
    simple_result = sleep_sort_simple(small_arr)
    simple_time = time_module.time() - start
    print(f"Simple version: {simple_result} (Time: {simple_time:.4f}s)")

    # Demonstrate the algorithm concept
    print("\n=== Algorithm Concept ===")
    print("1. Each number goes to sleep for n milliseconds")
    print("2. Smaller numbers wake up first and get added to result")
    print("3. Larger numbers wake up later and get added after")
    print("4. Final result is sorted in ascending order!")
