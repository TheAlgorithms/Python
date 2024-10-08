def reverse_selection_sort(arr):
    n = len(arr)

    # Iterate over each position of the array
    for i in range(n - 1):
        # Find the index of the minimum element in the unsorted portion
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # If the minimum is not already at position i, reverse the subarray
        if min_index != i:
            # Reverse the subarray from position i to min_index
            arr[i:min_index + 1] = reversed(arr[i:min_index + 1])

    return arr

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = reverse_selection_sort(arr)
print("Sorted array:", sorted_arr)

# Sorted array: [11, 12, 22, 25, 64]

# Explanation:
# Find the Minimum: For each position i in the array, find the minimum element in the unsorted portion.
# Reverse Subarray: After finding the minimum element, reverse the subarray starting from i up to the position of the minimum element (min_index).
# Repeat: This process repeats for each subsequent position, progressively sorting the array.
