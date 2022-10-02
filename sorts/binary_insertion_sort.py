def binary_search(arr: list[int], val: int, start: int, end: int) -> int:

    """
    Algorithm for Binary Search
    """

    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort(arr: list[int]) -> list:

    """
    Algorithm for insertion sort
    >>> insertion_sort([37, 23, 0, 31, 22, 17, 12, 72, 31, 46, 100, 88, 54])
    [0, 12, 17, 22, 23, 31, 31, 37, 46, 54, 72, 88, 100]
    """

    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1 :]
    return arr


if __name__ == "__main__":
    n = int(input("Enter number of elements : ").strip())
    array = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
    print(insertion_sort(array))
