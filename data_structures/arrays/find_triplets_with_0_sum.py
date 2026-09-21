from itertools import combinations


def find_triplets_with_0_sum(nums: list[int]) -> list[list[int]]:
    """
    Given a list of integers, return elements a, b, c such that a + b + c = 0.
    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:
        >>> find_triplets_with_0_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> find_triplets_with_0_sum([])
        []
        >>> find_triplets_with_0_sum([0, 0, 0])
        [[0, 0, 0]]
        >>> find_triplets_with_0_sum([1, 2, 3, 0, -1, -2, -3])
        [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    """
    return [
        list(x)
        for x in sorted({abc for abc in combinations(sorted(nums), 3) if not sum(abc)})
    ]


def find_triplets_with_0_sum_hashing(arr: list[int]) -> list[list[int]]:
    """
    Function for finding the triplets with a given sum in the array using hashing.

    Given a list of integers, return elements a, b, c such that a + b + c = 0.

    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:
        >>> find_triplets_with_0_sum_hashing([-1, 0, 1, 2, -1, -4])
        [[-1, 0, 1], [-1, -1, 2]]
        >>> find_triplets_with_0_sum_hashing([])
        []
        >>> find_triplets_with_0_sum_hashing([0, 0, 0])
        [[0, 0, 0]]
        >>> find_triplets_with_0_sum_hashing([1, 2, 3, 0, -1, -2, -3])
        [[-1, 0, 1], [-3, 1, 2], [-2, 0, 2], [-2, -1, 3], [-3, 0, 3]]

    Time complexity: O(N^2)
    Auxiliary Space: O(N)

    """
    target_sum = 0

    # Initialize the final output array with blank.
    output_arr = []

    # Set the initial element as arr[i].
    for index, item in enumerate(arr[:-2]):
        # to store second elements that can complement the final sum.
        set_initialize = set()

        # current sum needed for reaching the target sum
        current_sum = target_sum - item

        # Traverse the subarray arr[i+1:].
        for other_item in arr[index + 1 :]:
            # required value for the second element
            required_value = current_sum - other_item

            # Verify if the desired value exists in the set.
            if required_value in set_initialize:
                # finding triplet elements combination.
                combination_array = sorted([item, other_item, required_value])
                if combination_array not in output_arr:
                    output_arr.append(combination_array)

            # Include the current element in the set
            # for subsequent complement verification.
            set_initialize.add(other_item)

    # Return all the triplet combinations.
    return output_arr


if __name__ == "__main__":
    from doctest import testmod

    testmod()
