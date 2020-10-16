def merge(left_list, right_list, aux_array):
    """
    Receives the two halves of an array and does an ordered merge
    """
    i = 0
    j = 0
    k = 0

    # Sort up to the lower half
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            aux_array[k] = left_list[i]
            i += 1
        else:
            aux_array[k] = right_list[j]
            j += 1
        k += 1

    # Order the rest of the left
    while i < len(left_list):
        aux_array[k] = left_list[i]
        i += 1
        k += 1

    # Order the rest of the right
    while j < len(right_list):
        aux_array[k] = right_list[j]
        j += 1
        k += 1


def merge_sort(array, aux_array=[]) -> list:
    """
    Return the list of n numbers ordereds sorted in increasing order.
    >>> merge_sort([100, 55, 80, 20, 15, 98, 76, 500, 480])
    [15, 20, 55, 76, 80, 98, 100, 480, 500]
    """
    if len(array) > 1:

        half = int(len(array) / 2)

        left_list = array[:half]
        right_list = array[half:]

        # recursive call to the left half of the array
        merge_sort(left_list, array)
        # recursive call to the right half of the array
        merge_sort(right_list, array)
        # merge the two lists when you get to the base case
        merge(left_list, right_list, array)

        return array