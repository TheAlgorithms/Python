def heapify(arr, index, heap_size):
    """
    Heapify subtree rooted at given index.
    :param arr: List[int] The input list
    :param index: int The index of the root of the subtree
    :param heap_size: int The size of the heap
    :return: None
    """
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index

    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)


def heap_sort(arr):
    """
    Perform heap sort on the given array.
    :param arr: List[int] The input list
    :return: List[int] Sorted list
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr


if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]
        sorted_arr = heap_sort(unsorted)
        print("Sorted array:", sorted_arr)
    except ValueError:
        print("Invalid input. Please enter integers separated by commas.")
