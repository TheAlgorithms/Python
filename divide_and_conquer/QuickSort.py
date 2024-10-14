def quicksort(arr):
    # Base case: If the array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choosing the pivot (we pick the last element)
    pivot = arr[-1]

    # Dividing elements into two lists: smaller than pivot and greater than pivot
    smaller = [x for x in arr[:-1] if x <= pivot]
    larger = [x for x in arr[:-1] if x > pivot]

    # Recursively apply quicksort to the smaller and larger parts
    return quicksort(smaller) + [pivot] + quicksort(larger)

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)
