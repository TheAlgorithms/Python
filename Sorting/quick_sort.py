def quicksort(arr):
    # Base case: If the list has 1 or 0 elements, it's already sorted.
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (typically the middle element).
    pivot = arr[len(arr) // 2]
    
    # Partition the list into three parts: elements less than, equal to, and greater than the pivot.
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort the left and right partitions and concatenate the results.
    return quicksort(left) + middle + quicksort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
