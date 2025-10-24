'''
In traditional Merge Sort, the array is recursively divided into halves until we reach subarrays of size 1. In 3-way Merge Sort, the array is recursively divided into three parts, reducing the depth of recursion and potentially improving efficiency.
'''
def merge(arr, left, mid1, mid2, right):
    
    # Sizes of three subarrays
    size1 = mid1 - left + 1
    size2 = mid2 - mid1
    size3 = right - mid2
    
    # Temporary arrays for three parts
    left_arr = arr[left:left + size1]
    mid_arr = arr[mid1 + 1:mid1 + 1 + size2]
    right_arr = arr[mid2 + 1:mid2 + 1 + size3]
    
    # Merge three sorted subarrays
    i = j = k = 0
    index = left
    
    while i < size1 or j < size2 or k < size3:
        min_value = float('inf')
        min_idx = -1
        
        # Find the smallest among the three current elements
        if i < size1 and left_arr[i] < min_value:
            min_value = left_arr[i]
            min_idx = 0
        if j < size2 and mid_arr[j] < min_value:
            min_value = mid_arr[j]
            min_idx = 1
        if k < size3 and right_arr[k] < min_value:
            min_value = right_arr[k]
            min_idx = 2
        
        # Place the smallest element in the merged array
        if min_idx == 0:
            arr[index] = left_arr[i]
            i += 1
        elif min_idx == 1:
            arr[index] = mid_arr[j]
            j += 1
        else:
            arr[index] = right_arr[k]
            k += 1
        
        index += 1

def three_way_merge_sort(arr, left, right):
    
    # Base case: If single element, return
    if left >= right:
        return
    
    # Finding two midpoints for 3-way split
    mid1 = left + (right - left) // 3
    mid2 = left + 2 * (right - left) // 3
    
    # Recursively sort first third
    three_way_merge_sort(arr, left, mid1)
    
    # Recursively sort second third
    three_way_merge_sort(arr, mid1 + 1, mid2)
    
    # Recursively sort last third
    three_way_merge_sort(arr, mid2 + 1, right)
    
    # Merge the sorted parts
    merge(arr, left, mid1, mid2, right)

if __name__ == "__main__":
    
    # Input array
    arr = [5, 2, 9, 1, 6, 3, 8, 4, 7]
    
    # Calling 3-way merge sort function
    three_way_merge_sort(arr, 0, len(arr) - 1)
    
    # Printing the sorted array
    print(*arr)