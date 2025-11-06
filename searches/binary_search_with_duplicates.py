def binary_search_first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

if __name__ == "__main__":
    arr = [1, 2, 4, 4, 4, 5, 6]
    target = 4
    print(binary_search_first_occurrence(arr, target))  # Expected output: 2
