def two_sum(array: list[int], target: int) -> list[int]:
    """
    Finds two indices such that the numbers at those indices add up to the target value.

    This function uses a hash map (dictionary) to store the required complement
    for each element while iterating through the list. When a number is found
    that already exists in the dictionary, the indices of the two numbers are returned.

    Parameters:
    ----------
    array : list[int]
        A list of integers to search for the two-sum solution.

    target : int
        The target sum that the two numbers should add up to.

    Returns:
    -------
    list[int]
        A list containing the indices of the two elements whose sum equals the target.

    Examples:
    --------
    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
    >>> two_sum([3, 3], 6)
    [0, 1]

    Notes:
    ------
    - Assumes exactly one valid solution exists.
    - The same element cannot be used twice.

    Time Complexity:
    ----------------
    O(n), where n is the length of the input list.

    Space Complexity:
    -----------------
    O(n), due to the use of a dictionary to store complements.
    """

    dictionary: dict[int, int] = {}

    for i in range(len(array)):
        complement = target - array[i]

        if array[i] in dictionary:
            return [dictionary[array[i]], i]

        dictionary[complement] = i
