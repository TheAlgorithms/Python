"""
Given 'n' pairs of parentheses,
this program generates all combinations of parentheses.

Example, n = 3 :
[
   "((()))",
   "(()())",
   "(())()",
   "()(())",
   "()()()"
]

This problem can be solved using the concept of "BACKTRACKING".

By adding an open parenthesis to the solution and
recursively add more till we get 'n' open parentheses.

Then we start adding close parentheses until the solution is valid
(open parenthesis is closed).

If we reach a point where we can not add more parentheses to the solution,
we backtrack to the previous step and try a different path.
"""


def generate_parentheses(number: int = 3):
    """

    >>> generate_parentheses(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']

    >>> generate_parentheses(1)
    ['()']

    >>> generate_parentheses(0)
    ['']

    """

    def backtrack(x: str = "", left: int = 0, right: int = 0):
        if len(x) == 2 * number:
            result.append(x)
            return
        if left < number:
            backtrack(x + "(", left + 1, right)
        if right < left:
            backtrack(x + ")", left, right + 1)

    result = []
    backtrack()
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{generate_parentheses() = }")
