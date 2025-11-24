"""
In this Combination Problem, we are given a list consisting of distinct integers.
We need to find all the combinations whose sum equals to target given.
We cannot use an element more than one.

Time complexity(Average Case): O(n * 2^(n/2))


Constraints:
    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30
"""


def backtrack(
    candidates: list,
    target: int,
    start_index: int,
    total: int,
    path: list,
    answer: list,
) -> None:
    """
    A recursive function that searches for possible combinations. Backtracks in case
    of a bigger current combination value than the target value and removes the already
    appended values for removing repetition of elements in the solutions.

    Parameters
    ----------
    start_index: Last index from the previous search
    target: The value we need to obtain by summing our integers in the path list.
    answer: A list of possible combinations
    path: Current combination
    candidates: A list of integers we can use.
    total: Sum of elements in path
    """
    if target == 0:
        answer.append(path.copy())
        return
    if total == target:
        answer.append(path.copy())
        return
    for i in range(start_index, len(candidates)):
        if i > start_index and candidates[i] == candidates[i - 1]:
            continue
        if total + candidates[i] > target:
            break
        backtrack(
            candidates,
            target,
            i + 1,
            total + candidates[i],
            path + [candidates[i]],
            answer,
        )


def combination_sum_2(candidates: list, target: int) -> list:
    """
    >>> combination_sum_2([10,1,2,7,6,1,5], 8)
    [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    >>> combination_sum_2([1,2], 2)
    [[2]]
    >>> combination_sum_2([-8, 2.3, 0], 1)
    Traceback (most recent call last):
        ...
    ValueError: All elements in candidates must be non-negative
    >>> combination_sum_2([], 1)
    Traceback (most recent call last):
        ...
    ValueError: Candidates list should not be empty
    """
    if not candidates:
        raise ValueError("Candidates list should not be empty")

    if any(x < 0 for x in candidates):
        raise ValueError("All elements in candidates must be non-negative")
    candidates.sort()
    path = []
    answer = []
    backtrack(candidates, target, 0, 0, path, answer)
    return answer


def main() -> None:
    print(combination_sum_2([-8, 2.3, 0], 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
