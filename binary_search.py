def binary_search(arr, x):
    arr.sort()  # Sort in-place for efficiency
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < x:
            l = mid + 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            return mid  # Found
    return -1  # Not found

# Example usage
arr = [int(x) for x in input().split()]
x = int(input())
result = binary_search(arr, x)
if result == -1:
    print("Not found")
else:
    print(f"Found at index {result}")
