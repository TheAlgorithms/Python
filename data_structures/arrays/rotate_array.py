def rotate_array(arr, k):
    """
    Rotates the array to the right by k steps

    Args:
        arr(list): The input array
        k(int): Number of steps to rotate

    Returns:
        list: Rotated array
    """
    n = len(arr)
    k = k % n if n else 0

    arr.reverse()  # Reverse the entire array
    arr[:k] = reversed(arr[:k])  # Reverse the first k elements
    arr[k:] = reversed(arr[k:])  # Reverse the last (n-k) elements

    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3
    print("Rotated array: ", rotate_array(arr, k))
