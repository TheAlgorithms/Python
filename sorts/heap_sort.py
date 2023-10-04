def heapify(arr, root, size):
    """
    Heapify a subtree rooted at 'root' to maintain the max-heap property.

    Args:
        arr (list): The input list.
        root (int): The index of the root element of the subtree.
        size (int): The size of the heap.
    """
    max_index = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2

    if left_child < size and arr[left_child] > arr[max_index]:
        max_index = left_child

    if right_child < size and arr[right_child] > arr[max_index]:
        max_index = right_child

    if max_index != root:
        arr[root], arr[max_index] = arr[max_index], arr[root]
        heapify(arr, max_index, size)


def heap_sort(arr):
    """
    Sorts an input list using the heap sort algorithm.

    Args:
        arr (list): The input list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)

    # Build a max-heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

    # Extract elements one by one and build a sorted array.
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root with the last element.
        heapify(arr, 0, i)  # Call heapify on the reduced heap.

    return arr


if __name__ == "__main__":
    user_input = input("Enter numbers separated by commas: ").strip()
    try:
        unsorted = [int(item) for item in user_input.split(",")]
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by commas.")
        exit()
    print(f"Sorted list: {heap_sort(unsorted)}")
