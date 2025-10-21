"""
Sleep Sort Algorithm Implementation

Sleep sort works by creating a separate thread for each element in the input array,
where each thread sleeps for a duration proportional to the element's value.
When the thread wakes up, the element is appended to the result list.
Smaller values wake up first, resulting in a sorted list.
"""

import threading
import time


def sleep_sort(arr: list[int]) -> list[int]:
    """
    Sort list using sleep sort algorithm.

    Args:
        arr: List of non-negative integers

    Returns:
        Sorted list in ascending order

    Examples:
        >>> sleep_sort([3, 1, 4, 2])
        [1, 2, 3, 4]
        >>> sleep_sort([])
        []
        >>> sleep_sort([5])
        [5]
    """
    if not arr:
        return []

    result: list[int] = []
    lock = threading.Lock()

    def add_to_result(value: int) -> None:
        time.sleep(value)
        with lock:
            result.append(value)

    threads = []
    for num in arr:
        if num < 0:
            raise ValueError("Sleep sort only works with non-negative integers")
        thread = threading.Thread(target=add_to_result, args=(num,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return result


def test_sleep_sort() -> None:
    """Test sleep sort algorithm with various test cases."""
    # Test basic functionality
    assert sleep_sort([3, 1, 4, 2]) == [1, 2, 3, 4]

    # Test edge cases
    assert sleep_sort([]) == []
    assert sleep_sort([5]) == [5]
    assert sleep_sort([1, 1, 1]) == [1, 1, 1]
    assert sleep_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sleep_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    print("All tests passed!")


if __name__ == "_main_":
    # Run automated tests
    test_sleep_sort()

    # Interactive demo
    try:
        user_input = input("Enter non-negative numbers separated by commas: ").strip()
        if user_input:
            numbers = [int(x.strip()) for x in user_input.split(",")]
            print(f"Original list: {numbers}")

            # Validate input
            if any(num < 0 for num in numbers):
                print("Error: Sleep sort only works with non-negative integers")
            else:
                print(
                    "Sorting... (this will take time proportional to the largest number)"
                )
                sorted_numbers = sleep_sort(numbers)
                print(f"Sorted list: {sorted_numbers}")
        else:
            print("No input provided.")
    except ValueError:
        print("Error: Please enter valid integers separated by commas.")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
