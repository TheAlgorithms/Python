from typing import List

def heapify(arr: List[int], n: int, i: int) -> None:
    largest = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: List[int]) -> None:
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# Example usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted array:", arr)

def heap_sort(arr: List[int]) -> None:
    """
    Sorts the input list in-place using the Heap Sort algorithm.

    >>> arr = [12, 11, 13, 5, 6, 7]
    >>> heap_sort(arr)
    >>> arr
    [5, 6, 7, 11, 12, 13]
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
