def selectionsort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            # Find the minimum element in the remaining unsorted portion of the array.
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element.
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
selectionsort(arr)
print(arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
