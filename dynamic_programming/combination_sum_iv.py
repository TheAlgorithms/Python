"""
Question:
    You are given an array of distinct integers and you have to tell how many
    different ways of selecting the elements from the array are there such that
    the sum of chosen elements is equal to the target number tar.

Example

Input:
    * N = 3
    * target = 5
    * array = [1, 2, 5]

Output:
    9

Approach:
    The basic idea is to go over recursively to find the way such that the sum
    of chosen elements is `target`. For every element, we have two choices

        1. Include the element in our set of chosen elements.
        2. Don't include the element in our set of chosen elements.
"""


def combination_sum_iv(array: list[int], target: int) -> int:
    """
    Function checks the all possible combinations, and returns the count
    of possible combination in exponential Time Complexity.

    >>> combination_sum_iv([1,2,5], 5)
    9
    """

    def count_of_possible_combinations(target: int) -> int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        return sum(count_of_possible_combinations(target - item) for item in array)

    return count_of_possible_combinations(target)


def combination_sum_iv_dp_array(array: list[int], target: int) -> int:
    """
    Function checks the all possible combinations, and returns the count
    of possible combination in O(N^2) Time Complexity as we are using Dynamic
    programming array here.

    >>> combination_sum_iv_dp_array([1,2,5], 5)
    9
    """

    def count_of_possible_combinations_with_dp_array(
        target: int, dp_array: list[int]
    ) -> int:
        if target < 0:
            return 0
        if target == 0:
            return 1
        if dp_array[target] != -1:
            return dp_array[target]
        answer = sum(
            count_of_possible_combinations_with_dp_array(target - item, dp_array)
            for item in array
        )
        dp_array[target] = answer
        return answer

    dp_array = [-1] * (target + 1)
    return count_of_possible_combinations_with_dp_array(target, dp_array)


def combination_sum_iv_bottom_up(n: int, array: list[int], target: int) -> int:
    """
    Function checks the all possible combinations with using bottom up approach,
    and returns the count of possible combination in O(N^2) Time Complexity
    as we are using Dynamic programming array here.

    >>> combination_sum_iv_bottom_up(3, [1,2,5], 5)
    9
    """

    dp_array = [0] * (target + 1)
    dp_array[0] = 1

    for i in range(1, target + 1):
        for j in range(n):
            if i - array[j] >= 0:
                dp_array[i] += dp_array[i - array[j]]

    return dp_array[target]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    target = 5
    array = [1, 2, 5]
    print(combination_sum_iv(array, target))
