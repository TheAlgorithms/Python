"""
    Given 'n' pairs of parentheses,
    this program generates all combinations of well-formed parentheses.

    Example, n = 3:
    [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
    The number of valid combinations of parentheses (Catalan number) for n pairs is:
    C(n) = (2n)! / ((n + 1)! * n!)

    You can find more information about Catalan numbers and their applications here:
    https://en.wikipedia.org/wiki/Catalan_number

    We use backtracking to solve this problem.
    Time complexity: O(4^n / sqrt(n))
    Space complexity: O(4^n / sqrt(n))
"""

from __future__ import annotations


def generate_parenthesis(n: int) -> list[str]:
    """
    >>> generate_parenthesis(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    >>> generate_parenthesis(1)
    ['()']
    >>> generate_parenthesis(0)
    []
    """

    result: list[str] = []
    generate_all_parenthesis(n, "", result, 0, 0)
    return result


def print_all_parenthesis(total_list: list[str]) -> None:
    for i in total_list:
        print(i)


if __name__ == "__main__":
    n = 3
    total_list = generate_parenthesis(n)
    print_all_parenthesis(total_list)
