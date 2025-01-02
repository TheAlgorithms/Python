 """
Combination Sum Problem

Description:
Given a list of distinct integers (candidates), find all unique combinations where the sum of elements equals the given target.
An element can be used multiple times in a combination.

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

Time complexity (Average Case): O(n!)
"""

def backtrack(
    candidates: list[int],
    path: list[int],
    answer: list[list[int]],
    target: int,
    start_index: int
) -> None:
    """
    Recursive helper function to find all valid combinations.

    Parameters:
    ----------
    candidates : list[int]
        A list of distinct integers we can use to form combinations.
    path : list[int]
        The current combination being formed.
    answer : list[list[int]]
        The list of valid combinations that sum to the target.
    target : int
        The remaining sum needed to reach the target.
    start_index : int
        The index to start searching from in the candidates list.

    Returns:
    -------
    None
    """
    if target == 0:
        answer.append(path.copy())
        return

    for i in range(start_index, len(candidates)):
        if candidates[i] <= target:
            path.append(candidates[i])
            backtrack(candidates, path, answer, target - candidates[i], i)  # Same index for reuse
            path.pop()  # Backtrack

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Finds all unique combinations of candidates that sum up to the target.

    Parameters:
    ----------
    candidates : list[int]
        A list of distinct integers.
    target : int
        The target sum we want to achieve.

    Returns:
    -------
    list[list[int]]
        A list of all unique combinations.

    Examples:
    --------
    >>> combination_sum([2, 3, 5], 8)
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    >>> combination_sum([2, 3, 6, 7], 7)
    [[2, 2, 3], [7]]
    >>> combination_sum([], 7)
    []
    >>> combination_sum([1], 0)
    []
    """
    if not candidates or target <= 0:
        return []

    answer: list[list[int]] = []
    backtrack(candidates, [], answer, target, 0)
    return answer

def main() -> None:
    """Main function to test the combination_sum function."""
    print("Example 1:", combination_sum([2, 3, 5], 8))
    print("Example 2:", combination_sum([2, 3, 6, 7], 7))
    print("Example 3 (Invalid input):", combination_sum([], 1))  # Should return []

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
