def library_sort(arr):
    n = len(arr)
    gap = 1

    while gap < n:
        gap = gap * 1.247  # Using a constant factor of 1.247, but this can be adjusted.

        if gap < 1:
            gap = 1

        gap = int(gap)

        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr = library_sort(arr)
print(sorted_arr)
