"""
In the Combination Sum problem, we are given a list consisting of distinct integers.
We need to find all the combinations whose sum equals to target given.
We can use an element more than one.
Time complexity(Average Case): O(n!),
"""


def backtrack(
    candidates: list, path: list, answer: list, target: int, previous_index: int
) -> None:
    """
    A recursive function that searches for possible combinations. Backtracks in case
    of a bigger current combination value than the target value.

    Parameters
    ----------
    previous_index: Last index from the previous search
    target: The value we need to obtain by summing our integers in the path list.
    answer: A list of possible combinations
    path: Current combination
    candidates: A list of integers we can use.
    """
    if target == 0:
        answer.append(path.copy())
    else:
        for index in range(previous_index, len(candidates)):
            if target >= candidates[index]:
                path.append(candidates[index])
                backtrack(candidates, path, answer, target - candidates[index], index)
                path.pop(len(path) - 1)


def combination_sum(candidates: list, target: int) -> list:
    path = []  # type: list[int]
    answer = []  # type: list[int]
    backtrack(candidates, path, answer, target, 0)
    return answer


def main() -> None:
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
