from typing import List


def strand_sort(arr: List[int], reverse: bool = False) -> List[int]:
    """
    Sorts a list using the Strand Sort algorithm.
    
    :param arr: Unordered input list.
    :param reverse: True for descending order, False for ascending order (default).
    :return: The sorted list.
    
    Examples:
    >>> strand_sort([4, 2, 5, 3, 0, 1])
    [0, 1, 2, 3, 4, 5]

    >>> strand_sort([4, 2, 5, 3, 0, 1], reverse=True)
    [5, 4, 3, 2, 1, 0]
    """
    _compare = lambda a, b: a > b if reverse else a < b
    sorted_list = []

    while arr:
        sublist = [arr.pop(0)]
        i = 0
        while i < len(arr):
            if _compare(arr[i], sublist[-1]):
                sublist.append(arr.pop(i))
            else:
                i += 1

        # Merge the sublist into the sorted_list
        if not sorted_list:
            sorted_list.extend(sublist)
        else:
            sorted_list = merge_lists(sorted_list, sublist, _compare)

    return sorted_list


def merge_lists(list1: List[int], list2: List[int], compare_func) -> List[int]:
    """
    Merges two sorted lists while preserving order based on the compare function.
    
    :param list1: First sorted list.
    :param list2: Second sorted list.
    :param compare_func: Function to compare elements.
    :return: Merged sorted list.
    """
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if compare_func(list1[i], list2[j]):
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # Append remaining elements from both lists
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list


if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by a comma:\n").strip()
        unsorted = [int(item) for item in user_input.split(",")]
        
        reverse_input = input("Sort in descending order? (y/n): ").strip().lower()
        reverse_sort = reverse_input == 'y'
        
        sorted_array = strand_sort(unsorted, reverse=reverse_sort)
        print("Sorted Array:", sorted_array)
    except ValueError:
        print("Invalid input. Please enter a list of integers separated by commas.")
