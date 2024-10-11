def flash_sort(array):
    n = len(array)

    # Step 1: Find mininum and maximum values
    min_value, max_value = array[0], array[0]
    for i in range(1, n):
        if array[i] > max_value:
            max_value = array[i]
        if array[i] < min_value:
            min_value = array[i]
    if min_value == max_value:
        return

    # Step 2: Divide array into m buckets
    import math
    m = max(math.floor(0.45 * n), 1)

    # Step 3: Count the number of elements in each class
    def get_bucket_id(value: int) -> int:
        """
        Get the bucket index for the given value.

        >>> get_bucket_id(5)
        1
        >>> get_bucket_id(10)
        2
        >>> get_bucket_id(1)
        0
        """
        return math.floor((m * (value - min_value)) / (max_value - min_value + 1))

    bucket_counts = [0] * m
    for value in array:
        bucket_counts[get_bucket_id(value)] += 1

    # Step 4: Convert the count to prefix sum
    for i in range(1, m):
        bucket_counts[i] = bucket_counts[i - 1] + bucket_counts[i]

    # Step 5: Rearrange the elements
    def find_swap_index(bucket_id: int) -> int:
        """
        Find the index for the first element in the given bucket.

        >>> array = [15, 13, 24, 7, 18, 3, 22, 9]
        >>> find_swap_index(1)  # Modify array as needed before calling
        1  # Update this return value based on the current state of the array
        """
        for ind in range(bucket_counts[bucket_id - 1], bucket_counts[bucket_id]):
            if get_bucket_id(array[ind]) != bucket_id:
                break
        return ind

    def arrange_bucket(i1: int, i2: int, bucket_id: int) -> None:
        """
        Arrange elements into the specified bucket.

        >>> array = [15, 13, 24, 7, 18, 3, 22, 9]
        >>> arrange_bucket(0, 4, 1)  # Modify array as needed before calling
        >>> array
        [3, 13, 15, 7, 18, 24, 22, 9]  # Update this expected result based on your implementation
        """
        for i in range(i1, i2):
            current_bucket_id = get_bucket_id(array[i])
            while current_bucket_id != bucket_id:
                swap_index = find_swap_index(current_bucket_id)
                array[i], array[swap_index] = array[swap_index], array[i]
                current_bucket_id = get_bucket_id(array[i])
        return

    for bucket_id in range(0, m - 1):
        if bucket_id == 0:
            arrange_bucket(bucket_id, bucket_counts[bucket_id], bucket_id)
        else:
            arrange_bucket(bucket_counts[bucket_id - 1], bucket_counts[bucket_id], bucket_id)

    # Step 6: Sort each bucket
    def insertion_sort(array) -> None:
        """
        Sort the array using insertion sort.

        >>> insertion_sort([4, 3, 2, 1])
        >>> array
        [1, 2, 3, 4]
        """
        for i in range(1, len(array)):
            temp = array[i]
            j = i - 1
            while j >= 0 and temp < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = temp
        return

    for i in range(m):
        if i == 0:
            array[i:bucket_counts[i]] = insertion_sort(array[i:bucket_counts[i]])
        else:
            array[bucket_counts[i - 1]:bucket_counts[i]] = insertion_sort(array[bucket_counts[i - 1]:bucket_counts[i]])
    return
