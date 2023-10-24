def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Element not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  # Element found at index 'mid'
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)  # Search in the left half
    else:
        return binary_search(arr, target, mid + 1, high)  # Search in the right half


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
