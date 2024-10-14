# Function to implement Quick Sort
def quick_sort(arr: list[int], low: int, high: int) -> None:
    """
    Perform quick sort on the given array in-place.

    Parameters:
    arr (list[int]): The list of integers to sort.
    low (int): The starting index of the portion of the array to sort.
    high (int): The ending index of the portion of the array to sort.

    Returns:
    None: The function sorts the array in-place.

    Doctest:
    >>> arr = [10, 7, 8, 9, 1, 5]
    >>> quick_sort(arr, 0, len(arr) - 1)
    >>> arr
    [1, 5, 7, 8, 9, 10]

    >>> arr = [4, 3, 2, 1]
    >>> quick_sort(arr, 0, len(arr) - 1)
    >>> arr
    [1, 2, 3, 4]
    """

    if low < high:
        # Partitioning index
        pi = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr: list[int], low: int, high: int) -> int:
    """
    Partition function to place the pivot element at its correct position.

    Parameters:
    arr (list[int]): The list of integers to partition.
    low (int): The starting index for the partition.
    high (int): The ending index for the partition.

    Returns:
    int: The partitioning index.
    """
    pivot = arr[high]  # Pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot
    return i + 1


# Driver code to take user-defined input and sort
if __name__ == "__main__":
    # Ask the user for input
    n = int(input("Enter the number of elements in the array: "))

    # Input array elements from the user
    arr = list(map(int, input(f"Enter {n} elements separated by spaces: ").split()))

    print("Original array:", arr)

    # Call quick sort function
    quick_sort(arr, 0, len(arr) - 1)

    # Print sorted array
    print("Sorted array:", arr)
