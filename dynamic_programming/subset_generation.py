from typing import List, Tuple


def get_combinations(arr: List[int], n: int) -> List[Tuple[int, ...]]:
    """
    Returns all possible combinations of n elements from the input array.

    :param arr: The input array
    :param n: The number of elements to combine
    :return: A list of tuples, where each tuple contains n elements from the input array
    """
    if n == 1:
        return [(x,) for x in arr]
    else:
        combinations = []
        for i in range(len(arr)):
            for combination in get_combinations(arr[i + 1 :], n - 1):
                combinations.append((arr[i],) + combination)
        return combinations


# Test the function
arr = [1, 2, 3, 4, 5]
n = 3
print(get_combinations(arr, n))
