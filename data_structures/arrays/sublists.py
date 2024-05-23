def generate_sublists_recursive(lst: list[int]) -> list[list[int]]:
    """
    Generate all sublists of the given list, including the empty sublist using a recursive approach.

    >>> generate_sublists_recursive([1, 2, 3])
    [[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
    """
    def helper(start: int) -> None:
        if start == len(lst):
            return
        for end in range(start + 1, len(lst) + 1):
            result.append(lst[start:end])
        helper(start + 1)
    
    result: list[list[int]] = [[]]
    helper(0)
    return result


def generate_sublists_backtrack(lst: list[int]) -> list[list[int]]:
    """
    Generate all sublists of the given list, including the empty sublist using a backtracking approach.

    >>> generate_sublists_backtrack([1, 2, 3])
    [[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
    """
    def backtrack(start: int, current: list[int]) -> None:
        result.append(current[:])
        for end in range(start, len(lst)):
            current.append(lst[end])
            backtrack(end + 1, current)
            current.pop()
    
    result: list[list[int]] = []
    backtrack(0, [])
    return result


if __name__ == "__main__":
    import doctest

    print(generate_sublists_recursive([1, 2, 3]))
    print(generate_sublists_backtrack([1, 2, 3]))
    doctest.testmod()
