def interpolation_search_recursive(arr, low, high, x):
    """Recursive implementation of Interpolation Search."""
    if low <= high and arr[low] <= x <= arr[high]:
        pos = low + ((high - low) * (x - arr[low])) // (arr[high] - arr[low])
        if arr[pos] == x:
            return pos
        if arr[pos] < x:
            return interpolation_search_recursive(arr, pos + 1, high, x)
        return interpolation_search_recursive(arr, low, pos - 1, x)
    return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70]
    x = 50
    result = interpolation_search_recursive(arr, 0, len(arr) - 1, x)
    print(f"Element {x} found at index: {result}" if result != -1 else "Element not found.")
