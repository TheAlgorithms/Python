from typing import List


def selection_sort(input_array: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the selection sort algorithm.

    Args:
        input_array (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list in ascending order.
    """
    n = len(input_array)

    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if input_array[j] < input_array[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        input_array[i], input_array[min_idx] = input_array[min_idx], input_array[i]

    return input_array


if __name__ == "__main__":
    # Example usage:
    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
