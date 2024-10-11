def find_min_max(arr):
    if len(arr) == 0:
        return None, None

    if len(arr) == 1:
        return arr, arr

    if arr > arr:
        max_val = arr
        min_val = arr
    else:
        max_val = arr
        min_val = arr

    for i in range(2, len(arr) - 1, 2):
        if arr[i] > arr[i + 1]:
            max_val = max(max_val, arr[i])
            min_val = min(min_val, arr[i + 1])
        else:
            max_val = max(max_val, arr[i + 1])
            min_val = min(min_val, arr[i])

    if len(arr) % 2 != 0:
        max_val = max(max_val, arr[-1])
        min_val = min(min_val, arr[-1])

    return min_val, max_val


# Example usage:
arr = [3, 5, 1, 2, 4, 8]
min_val, max_val = find_min_max(arr)
print(f"Minimum value: {min_val}, Maximum value: {max_val}")
