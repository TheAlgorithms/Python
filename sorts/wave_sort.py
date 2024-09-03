def wave_sort(arr):
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into smaller sub-arrays
    mid = len(arr) // 2
    left_half = wave_sort(arr[:mid])
    right_half = wave_sort(arr[mid:])

    # Step 2: Sort each sub-array individually
    left_half.sort()
    right_half.sort()

    # Step 3: Shuffle the sorted sub-arrays in a wave-like pattern
    shuffled_array = []
    i, j = 0, 0
    toggle = True
    
    while i < len(left_half) and j < len(right_half):
        if toggle:
            shuffled_array.append(left_half[i])
            i += 1
        else:
            shuffled_array.append(right_half[j])
            j += 1
        toggle = not toggle
    
    # Append remaining elements if any
    shuffled_array.extend(left_half[i:])
    shuffled_array.extend(right_half[j:])

    # Step 4: Merge the sub-arrays back together
    final_array = []
    n = len(shuffled_array)
    for k in range(n):
        if k % 2 == 0:
            final_array.append(shuffled_array[k])
        else:
            final_array.append(shuffled_array[-(k // 2 + 1)])
    
    # Step 5: Final pass to ensure complete sorting
    for l in range(1, len(final_array)):
        key = final_array[l]
        m = l - 1
        while m >= 0 and final_array[m] > key:
            final_array[m + 1] = final_array[m]
            m -= 1
        final_array[m + 1] = key
    
    return final_array

# Test the Wave Sort algorithm
arr = [34, 7, 23, 32, 5, 62, 32, 2, 43]
sorted_arr = wave_sort(arr)
print("Original array:", arr)
print("Sorted array using Wave Sort:", sorted_arr)
