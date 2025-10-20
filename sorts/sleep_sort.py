
"""Sleep Sort Algorithm."""

import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """Sort list using sleep sort."""
    if not arr:
        return []
    result: List[int] = []
    lock = threading.Lock()
    
    def worker(value: int) -> None:
        time.sleep(value / 10)
        with lock:
            result.append(value)
    
    threads: List[threading.Thread] = []
    for value in arr:
        if value < 0:
            raise ValueError("No negative numbers")
        thread = threading.Thread(target=worker, args=(value,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    return result

def sleep_sort_simple(arr: List[int]) -> List[int]:
    """Simple non-threaded version."""
    if not arr:
        return []
    return sorted(arr)

class SleepSort:
    """Class-based sleep sort implementation."""
    
    def _init_(self, speed_factor: float = 10.0) -> None:
        self.speed_factor = speed_factor
    
    def sort(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        result: List[int] = []
        lock = threading.Lock()
        
        def worker(value: int) -> None:
            time.sleep(value / self.speed_factor)
            with lock:
                result.append(value)
        
        threads: List[threading.Thread] = []
        for value in arr:
            if value < 0:
                raise ValueError("No negative numbers")
            thread = threading.Thread(target=worker, args=(value,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        return result

if __name__ == "_main_":
    test_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print("Original array:", test_arr)
    print("Simple sorted:", sleep_sort_simple(test_arr))
    
    try:
        threaded = sleep_sort(test_arr)
        print("Threaded sorted:", threaded)
    except Exception as e:
        print("Threaded error:", e)
    
    try:
        sorter = SleepSort(speed_factor=20.0)
        class_sorted = sorter.sort(test_arr)
        print("Class sorted:", class_sorted)
    except Exception as e:
        print("Class error:", e)
