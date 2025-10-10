import threading
import time

def sleep_sort(arr):
    """
    Sorts a list of positive integers using Sleep Sort.
    
    Args:
        arr (list[int]): List of positive integers to sort.
        
    Returns:
        list[int]: Sorted list in ascending order.
    """
    result = []

    def sleeper(x):
        # Sleep for a duration proportional to the number
        time.sleep(x * 0.01)  # scale down to avoid long delays
        result.append(x)

    threads = [threading.Thread(target=sleeper, args=(num,)) for num in arr]
    
    # Start all threads
    for t in threads:
        t.start()
    
    # Wait for all threads to finish
    for t in threads:
        t.join()

    return result

# Example Usage
if __name__ == "__main__":
    numbers = [4, 1, 3, 2]
    sorted_numbers = sleep_sort(numbers)
    print("Original:", numbers)
    print("Sorted:", sorted_numbers)
