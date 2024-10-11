def flash_sort(array: list[int]) -> list[int]:
    """
    Perform Flashsort on the given array.

    Flashsort is a distribution-based sorting algorithm. It divides the array
    into buckets based on value ranges and sorts within each bucket.

    Arguments:
    array -- list of integers to sort

    Returns:
    Sorted list of integers.

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
    m = max(int(0.45 * n), 1)

    # Step 3: Count the number of elements in each class
    def get_bucket_id(value: int) -> int:
        return (m * (value - min_value)) // (max_value - min_value + 1)
    
    Lb = [0] * m
    for value in array:
        Lb[get_bucket_id(value)] += 1
    
    # Step 4: Convert the count to prefix sum
    for i in range(1, m):
        Lb[i] += Lb[i - 1]

    # Step 5: Rearrange the elements
    def find_swap_index(b_id: int) -> int:
        for ind in range(Lb[b_id - 1], Lb[b_id]):
            if get_bucket_id(array[ind]) != b_id:
                break
        return ind

    def arrange_bucket(i1: int, i2: int, b: int):
        for i in range(i1, i2):
            b_id = get_bucket_id(array[i])
            while b_id != b:
                s_ind = find_swap_index(b_id)
                array[i], array[s_ind] = array[s_ind], array[i]
                b_id = get_bucket_id(array[i])

    for b in range(m - 1):
        if b == 0:
            arrange_bucket(b, Lb[b], b)
        else:
            arrange_bucket(Lb[b - 1], Lb[b], b)

    # Step 6: Sort each bucket using insertion sort
    def insertion_sort(sub_array: list[int]) -> list[int]:
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
            array[i:Lb[i]] = insertion_sort(array[i:Lb[i]])
        else:
            array[Lb[i - 1]:Lb[i]] = insertion_sort(array[Lb[i - 1]:Lb[i]])

    return array


# print(flash_sort([15, 13, 24, 7, 18, 3, 22, 9]))