def heapsort(arr):
    import heapq

    # Convert the list into a min-heap.
    heapq.heapify(arr)
    sorted_arr = []
    while arr:
        # Pop elements from the heap to build the sorted array.
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr


# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = heapsort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
