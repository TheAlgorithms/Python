def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


# Function to handle edge cases and testing
def test_quick_sort():
    test_cases = [
        # Regular case with positive integers
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),
        # Already sorted array
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        # Reverse sorted array
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        # Array with duplicates
        ([4, 2, 4, 1, 2, 1], [1, 1, 2, 2, 4, 4]),
        # Array with negative and positive numbers
        ([-3, 5, -1, 7, 0, -2], [-3, -2, -1, 0, 5, 7]),
        # Single element array
        ([42], [42]),
        # Empty array
        ([], []),
        # Array with all same elements
        ([1, 1, 1, 1], [1, 1, 1, 1]),
    ]

    for i, (arr, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: Original array = {arr}")
        quick_sort(arr, 0, len(arr) - 1)
        assert (
            arr == expected
        ), f"Test case {i+1} failed: Expected {expected}, but got {arr}"
        print(f"Test case {i+1} passed: Sorted array = {arr}")

    print("All test cases passed!")


test_quick_sort()
