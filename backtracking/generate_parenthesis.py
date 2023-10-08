import doctest


def solve(op: str, open: int, close: int, ans: list[str]) -> None:
    if open == 0 and close == 0:
        ans.append(op)
        return
    if open == close:
        op1: str = op
        op1 += "("
        solve(op1, open - 1, close, ans)
    elif open == 0:
        op1: str = op
        op1 += ")"
        solve(op1, open, close - 1, ans)
    elif close == 0:
        op1: str = op
        op1 += "("
        solve(op1, open - 1, close, ans)
    else:
        op1: str = op
        op2: str = op
        op1 += "("
        op2 += ")"
        solve(op1, open - 1, close, ans)
        solve(op2, open, close - 1, ans)


def generate_parenthesis(n: int) -> list[str]:  # n = no. of pairs of parenthesis > 0
    """
    >>> generate_parenthesis(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    >>> generate_parenthesis(4)
    ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
    """
    open: int = n
    close: int = n
    ans: list[str] = []
    op: str = ""
    solve(op, open, close, ans)
    if n > 0:
        return ans


doctest.testmod()
