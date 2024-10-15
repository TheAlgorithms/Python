def reverse_subarray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def reverse_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        
        
        reverse_subarray(arr, i, max_index)

# Example usage
arr = [64, 88, 96, 1, 11]
reverse_sort(arr)
print("Sorted array:", arr)
