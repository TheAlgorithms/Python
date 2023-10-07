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


def helper_function_to_generate_parenthesis(
    num_pairs: int,
    current_string: str,
    result: list[str],
    num_open: int,
    num_close: int,
) -> None:
    """
    Helper function to generate all combinations of well-formed parentheses.

    Args:
        num_pairs (int): The number of pairs of parentheses to use.
        current_string (str): The current string of parentheses.
        result (list[str]): The list of all possible combinations of parentheses.
        num_open (int): The number of open parentheses.
        num_close (int): The number of close parentheses.

    Returns:
        None, but the result is updated.

    Examples:
        >>> result = []
        >>> helper_function_to_generate_parenthesis(3, "", result, 0, 0)
        >>> result
        ['((()))', '(()())', '(())()', '()(())', '()()()']
        >>> result = []
        >>> helper_function_to_generate_parenthesis(1, "", result, 0, 0)
        >>> result
        ['()']
        >>> result = []
        >>> helper_function_to_generate_parenthesis(0, "", result, 0, 0)
        >>> result
        ['']
    """

    if num_open == num_pairs and num_close == num_pairs:
        result.append(current_string)
        return

    if num_open < num_pairs:
        helper_function_to_generate_parenthesis(
            num_pairs, current_string + "(", result, num_open + 1, num_close
        )

    if num_close < num_open:
        helper_function_to_generate_parenthesis(
            num_pairs, current_string + ")", result, num_open, num_close + 1
        )


def generate_parenthesis(num_pairs: int) -> list[str]:
    """
    Generate all combinations of well-formed parentheses given the number of pairs.

    Args:
        num_pairs (int): The number of pairs of parentheses to use.

    Returns:
        list[str]: A list of all possible combinations of well-formed parentheses.

    Examples:
        >>> generate_parenthesis(num_pairs=3)
        ['((()))', '(()())', '(())()', '()(())', '()()()']
        >>> generate_parenthesis(num_pairs=1)
        ['()']
        >>> generate_parenthesis(num_pairs=0)
        ['']
    """

    result: list[str] = []
    helper_function_to_generate_parenthesis(num_pairs, "", result, 0, 0)
    return result


def print_all_parenthesis(total_list: list[str]) -> None:
    """
    Print all combinations of well-formed parentheses.

    Args:
        total_list (list[str]): A list of all possible combinations of parentheses.

    Returns:
        None, but the result is printed.

    Examples:
        >>> print_all_parenthesis(total_list=['((()))', '(()())', '(())()', '()(())'])
        ((()))
        (()())
        (())()
        ()(())
        >>> print_all_parenthesis(total_list=['()'])
        ()
        >>> print_all_parenthesis(total_list=[''])
        <BLANKLINE>

    """
    for i in total_list:
        print(i)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    n = 3
    print(f"The number of pairs of parentheses is {n}.")
    total_list = generate_parenthesis(n)
    print(f"The total number of combinations is {len(total_list)}.")
    print("The combinations are:")
    print_all_parenthesis(total_list)
