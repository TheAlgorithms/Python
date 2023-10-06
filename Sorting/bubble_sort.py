def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare adjacent elements and swap if they are in the wrong order.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
bubblesort(arr)
print(arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
