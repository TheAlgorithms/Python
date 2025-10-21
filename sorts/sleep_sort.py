import threading
import time
from typing import List

def sleep_sort(arr: List[int]) -> List[int]:
    """
    Sleep sort implementation - each element sleeps for n seconds then gets appended
    """
    if not arr:
        return []
    
    result = []
    
    def add_to_result(n):
        time.sleep(n)
        result.append(n)
    
    threads = []
    for num in arr:
        thread = threading.Thread(target=add_to_result, args=(num,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    return result

if __name__ == "__main__":
    # Test the sleep sort
    user_input = input("Enter numbers separated by commas: ")
    if user_input:
        numbers = [int(x) for x in user_input.split(",")]
        print("Original:", numbers)
        sorted_numbers = sleep_sort(numbers)
        print("Sorted:", sorted_numbers)
    else:
        print("No input provided")