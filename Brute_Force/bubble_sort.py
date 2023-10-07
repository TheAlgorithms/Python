def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps were made in this pass
        swapped = False
        
        # Last i elements are already in place, so we don't need to check them again
        for j in range(0, n - i - 1):
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)

