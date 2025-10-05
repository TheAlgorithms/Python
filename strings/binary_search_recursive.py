def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)


if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12]
    target = 10
    result = binary_search(arr, target, 0, len(arr) - 1)
    print(f"Element found at index {result}" if result != -1 else "Not found")
