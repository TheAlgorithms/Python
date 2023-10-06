def mergesort(arr):
    # Base case: If the list has 1 or 0 elements, it's already sorted.
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0

        # Merge the left and right sublists in sorted order.
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Append any remaining elements from left and right sublists.
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    # Recursively merge and sort the left and right partitions.
    return merge(mergesort(left), mergesort(right))

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = mergesort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 6, 8, 10]
