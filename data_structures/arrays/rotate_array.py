def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n

    if k < 0:
        k += n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

    return arr


if __name__ == "__main__":
    examples = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], -2),
        ([1, 2, 3, 4, 5], 7),
        ([], 3),
    ]

    for arr, k in examples:
        rotated = rotate_array(arr.copy(), k)
        print(f"Rotate {arr} by {k}: {rotated}")