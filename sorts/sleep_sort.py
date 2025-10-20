"""
Sleep Sort Algorithm Implementation
"""

import threading
import time
from typing import List


def sleep_sort(arr: List[int]) -> List[int]:
    """
    Sort list using sleep sort algorithm.

    Args:
        arr: List of non-negative integers

    Returns:
        Sorted list in ascending order
    """
    if not arr:
        return []

    result = []
    lock = threading.Lock()

    def worker(value):
        time.sleep(value / 10)
        with lock:
            result.append(value)

    threads = []
    for value in arr:
        if value < 0:
            raise ValueError("No negative numbers allowed")
        thread = threading.Thread(target=worker, args=(value,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result


class SleepSort:
    """Class-based sleep sort implementation."""

    def _init_(self, speed_factor=10.0):
        self.speed_factor = speed_factor

    def sort(self, arr):
        """
        Sort array using sleep sort.

        Args:
            arr: List of non-negative integers

        Returns:
            Sorted list
        """
        if not arr:
            return []

        result = []
        lock = threading.Lock()

        def worker(value):
            time.sleep(value / self.speed_factor)
            with lock:
                result.append(value)

        threads = []
        for value in arr:
            if value < 0:
                raise ValueError("No negative numbers allowed")
            thread = threading.Thread(target=worker, args=(value,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return result


if __name__ == "_main_":
    # Test the algorithms
    test_data = [3, 1, 4, 1, 5, 9, 2, 6]

    print("Original array:", test_data)

    # Test basic sleep sort
    try:
        sorted1 = sleep_sort(test_data)
        print("Basic sleep sort:", sorted1)
    except Exception as e:
        print("Basic sleep sort error:", e)

    # Test class-based sleep sort
    try:
        sorter = SleepSort(speed_factor=20.0)
        sorted2 = sorter.sort(test_data)
        print("Class sleep sort:", sorted2)
    except Exception as e:
        print("Class sleep sort error:", e)

    print("Algorithm completed successfully!")
