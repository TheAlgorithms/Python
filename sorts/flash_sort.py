# Flash Sort Algorithm
# 
# Flash Sort is a distribution sorting algorithm designed for large arrays with elements
# that are relatively uniformly distributed. The algorithm can achieve close to O(n) time
# complexity under favorable conditions.
#
# Main steps:
# 1. Find the minimum and maximum values in the array.
# 2. Choose the number of classes ("buckets") m. The typical choice is m = int(0.43 * n),
#    where n is the array length. The constant 0.43 is an empirical value shown by the
#    original paper and Wikipedia to provide good performance in practice. The goal is
#    to have enough classes to distribute elements evenly, but not so many that classes
#    become sparse.
# 3. Classify each element into one of the m classes using a linear mapping from the
#    value range to class indices.
# 4. Compute prefix sums of the class counts to determine the class boundaries.
# 5. Rearrange (permute) elements in-place so that all elements belonging to the same
#    class are grouped together. This is performed using a cycle leader algorithm.
# 6. For each class, perform a final sorting step (usually insertion sort), because
#    elements within a class are not guaranteed to be sorted.
#
# Reference:
# https://en.wikipedia.org/wiki/Flashsort

def flash_sort(array):
    """
    Flash Sort algorithm.

    Flash Sort is a distribution sorting algorithm that achieves linear time complexity O(n)
    for uniformly distributed data sets using relatively little additional memory.
    See: https://en.wikipedia.org/wiki/Flashsort

    Args:
        array (list): List of numeric values to be sorted.

    Returns:
        list: Sorted list.
    """
    n = len(array)
    if n == 0:
        return array.copy()

    min_value = min(array)
    max_value = max(array)
    if min_value == max_value:
        return array.copy()

    # Step 2: Choose the number of classes (buckets)
    # Empirically, 0.43 * n gives good performance; see Wikipedia and original papers.
    number_of_classes = max(int(0.43 * n), 2)
    class_boundaries = [0] * number_of_classes

    # Step 3: Classify elements into classes (buckets)
    class_coefficient = (number_of_classes - 1) / (max_value - min_value)
    for value in array:
        class_index = int(class_coefficient * (value - min_value))
        class_boundaries[class_index] += 1

    # Step 4: Compute prefix sums for class boundaries
    for i in range(1, number_of_classes):
        class_boundaries[i] += class_boundaries[i - 1]

    # Step 5: Permute elements into correct classes (cycle leader permutation)
    sorted_array = [0] * n
    for value in reversed(array):
        class_index = int(class_coefficient * (value - min_value))
        class_boundaries[class_index] -= 1
        sorted_array[class_boundaries[class_index]] = value

    # Step 6: Final insertion sort within the sorted array
    for i in range(1, n):
        key = sorted_array[i]
        j = i - 1
        while j >= 0 and sorted_array[j] > key:
            sorted_array[j + 1] = sorted_array[j]
            j -= 1
        sorted_array[j + 1] = key

    return sorted_array
