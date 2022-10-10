def longest_valid_parenthesis(s: str) -> int:
    """
    Returns the length of the longest valid parenthesis
     >>> longest_valid_parenthesis('(()')
     2
     >>> longest_valid_parenthesis(')()())')
     4
     >>> longest_valid_parenthesis('(()()()()))')
     10
     >>> longest_valid_parenthesis(''(())))((()(()()()())
     8
    """
    stack = []
    preceeding_matched = 0
    res = 0
    for char in s:
        if char == "(":
            stack.append(preceeding_matched)
            preceeding_matched = 0
        else:
            if stack:
                preceeding_matched += 1 + stack.pop()
            else:
                res = max(res, preceeding_matched)
                preceeding_matched = 0
    res = max(res, preceeding_matched)
    while stack:
        res = max(res, stack.pop())
    return res * 2


if __name__ == "__main__":
    s = input()
    print(longest_valid_parenthesis(s))
