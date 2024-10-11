import math

def flash_sort(array: list[int]) -> list[int]:
    """
    Perform Flashsort on the given array.

    Flashsort is a distribution-based sorting algorithm. It divides the array
    into buckets based on value ranges and sorts within each bucket.

    Args:
        array (list[int]): List of integers to sort.

    Returns:
        list[int]: The sorted array.

    Example:
    >>> flash_sort([15, 13, 24, 7, 18, 3, 22, 9])
    [3, 7, 9, 13, 15, 18, 22, 24]
    >>> flash_sort([5, 1, 4, 2, 3])
    [1, 2, 3, 4, 5]
    """
    n = len(array)

    # Step 1: Find minimum and maximum values
    min_value, max_value = array[0], array[0]
    for i in range(1, n):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
    if min_value == max_value:
        return array  # All values are the same

    # Step 2: Divide array into m buckets
    m = max(math.floor(0.45 * n), 1)

    # Step 3: Count the number of elements in each class
    def get_bucket_id(value: int) -> int:
        """
        Get the bucket index for the given value.

        Args:
            value (int): The value to assign a bucket to.

        Returns:
            int: The index of the bucket.

        Example:
        >>> get_bucket_id(15)
        2
        >>> get_bucket_id(7)
        0
        """
        return (m * (value - min_value)) // (max_value - min_value + 1)

    bucket_counts = [0] * m
    for value in array:
        bucket_counts[get_bucket_id(value)] += 1

    # Step 4: Convert the count to prefix sum
    for i in range(1, m):
        bucket_counts[i] += bucket_counts[i - 1]

    # Step 5: Rearrange the elements
    def find_swap_index(bucket_id: int) -> int:
        """
        Find the first index of the element in the bucket.

        Args:
            bucket_id (int): The ID of the bucket.

        Returns:
            int: The index of the first element in the bucket.

        Example:
        >>> array = [15, 13, 24, 7, 18, 3, 22, 9]
        >>> find_swap_index(1)
        1
        """
        for ind in range(bucket_counts[bucket_id - 1], bucket_counts[bucket_id]):
            if get_bucket_id(array[ind]) != bucket_id:
                break
        return ind

    def arrange_bucket(i1: int, i2: int, bucket_id: int) -> None:
        """
        Arrange elements into the specified bucket.

        Args:
            i1 (int): Start index.
            i2 (int): End index.
            bucket_id (int): The bucket id to arrange elements for.

        Example:
        >>> array = [15, 13, 24, 7, 18, 3, 22, 9]
        >>> arrange_bucket(0, 4, 1)
        >>> array
        [3, 13, 15, 7, 18, 24, 22, 9]
        """
        for i in range(i1, i2):
            current_bucket_id = get_bucket_id(array[i])
            while current_bucket_id != bucket_id:
                swap_index = find_swap_index(current_bucket_id)
                array[i], array[swap_index] = array[swap_index], array[i]
                current_bucket_id = get_bucket_id(array[i])

    for bucket_id in range(m - 1):
        if bucket_id == 0:
            arrange_bucket(0, bucket_counts[bucket_id], bucket_id)
        else:
            arrange_bucket(bucket_counts[bucket_id - 1], bucket_counts[bucket_id], bucket_id)

    # Step 6: Sort each bucket using insertion sort
    def insertion_sort(sub_array: list[int]) -> list[int]:
        """
        Sort the given array using insertion sort.

        Args:
            sub_array (list[int]): List of integers to sort.

        Returns:
            list[int]: Sorted array.

        Example:
        >>> insertion_sort([4, 3, 2, 1])
        [1, 2, 3, 4]
        """
        for i in range(1, len(sub_array)):
            temp = sub_array[i]
            j = i - 1
            while j >= 0 and temp < sub_array[j]:
                sub_array[j + 1] = sub_array[j]
                j -= 1
            sub_array[j + 1] = temp
        return sub_array

    for i in range(m):
        if i == 0:
            array[0:bucket_counts[i]] = insertion_sort(array[0:bucket_counts[i]])
        else:
            array[bucket_counts[i - 1]:bucket_counts[i]] = insertion_sort(array[bucket_counts[i - 1]:bucket_counts[i]])

    return array
