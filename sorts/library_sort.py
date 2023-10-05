def library_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    gap = 1
    while gap < n:
        gap = gap * 2

    gap = gap // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 2

    return arr

arr = [5, 2, 9, 3, 1]
sorted_arr = library_sort(arr)
print(sorted_arr)
