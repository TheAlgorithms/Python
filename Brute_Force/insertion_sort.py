def insertion_sort(arr):
    for i in range(1, len(arr)):
        # Get the current element to be compared
        current_element = arr[i]
        j = i - 1
        
        # Move elements of the sorted part of the list that are greater than the current element
        # one position ahead of their current position
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the current element in its correct position within the sorted part of the list
        arr[j + 1] = current_element

# Example usage
arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("Sorted array is:", arr)

