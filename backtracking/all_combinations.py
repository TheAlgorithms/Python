"""
        In this problem, we want to determine all possible combinations of k
        numbers out of 1 ... n. We use backtracking to solve this problem.
        Time complexity: O(C(n,k)) which is O(n choose k) = O((n!/(k! * (n - k)!)))
"""
from typing import List

def generate_all_combinations(n: int, k: int) -> List[List[int]]:
    """
    Generate all possible combinations of k numbers out of 1...n.

    Args:
    n (int): The range of numbers from 1 to n.
    k (int): The number of elements in each combination.

    Returns:
    List[List[int]]: A list of all valid combinations.

    Example:
    >>> generate_all_combinations(n=4, k=2)
    [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """

    result: List[List[int]] = []
    create_all_state(1, n, k, [], result)
    return result


def create_all_state(
    start: int,
    n: int,
    k: int,
    current_combination: List[int],
    all_combinations: List[List[int]],
) -> None:
    if k == 0:
        all_combinations.append(current_combination[:])
        return

    for num in range(start, n - k + 2):
        current_combination.append(num)
        create_all_state(num + 1, n, k - 1, current_combination, all_combinations)
        current_combination.pop()


def print_all_combinations(all_combinations: List[List[int]]) -> None:
    for combination in all_combinations:
        print(*combination)


if __name__ == "__main__":
    n = 4
    k = 2
    all_combinations = generate_all_combinations(n, k)
    print_all_combinations(all_combinations)
