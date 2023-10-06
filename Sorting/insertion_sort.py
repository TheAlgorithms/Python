def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key to one position ahead of their current position.
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
insertionsort(arr)
print(arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
