"""
author: Aayush Soni
Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.
Input: n = 2
Output: ["(())","()()"]
Leetcode link: https://leetcode.com/problems/generate-parentheses/description/
"""


def backtrack(
    partial: str, open_count: int, close_count: int, n: int, result: list[str]
) -> None:
    """
    Generate valid combinations of balanced parentheses using recursion.

    :param partial: A string representing the current combination.
    :param open_count: An integer representing the count of open parentheses.
    :param close_count: An integer representing the count of close parentheses.
    :param n: An integer representing the total number of pairs.
    :param result: A list to store valid combinations.
    :return: None

    This function uses recursion to explore all possible combinations,
    ensuring that at each step, the parentheses remain balanced.

    Example:
    >>> result = []
    >>> backtrack("", 0, 0, 2, result)
    >>> result
    ['(())', '()()']
    """
    if len(partial) == 2 * n:
        # When the combination is complete, add it to the result.
        result.append(partial)
        return

    if open_count < n:
        # If we can add an open parenthesis, do so, and recurse.
        backtrack(partial + "(", open_count + 1, close_count, n, result)

    if close_count < open_count:
        # If we can add a close parenthesis (it won't make the combination invalid),
        # do so, and recurse.
        backtrack(partial + ")", open_count, close_count + 1, n, result)


def generate_parenthesis(n: int) -> list[str]:
    """
    Generate valid combinations of balanced parentheses for a given n.

    :param n: An integer representing the number of pairs of parentheses.
    :return: A list of strings with valid combinations.

    This function uses a recursive approach to generate the combinations.

    Time Complexity: O(2^(2n)) - In the worst case, we have 2^(2n) combinations.
    Space Complexity: O(n) - where 'n' is the number of pairs.

    Example 1:
    >>> generate_parenthesis(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']

    Example 2:
    >>> generate_parenthesis(1)
    ['()']

    Example 3:
    >>> generate_parenthesis(0)
    ['']
    """

    result: list[str] = []
    backtrack("", 0, 0, n, result)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
