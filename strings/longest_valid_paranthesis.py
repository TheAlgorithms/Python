def longest_valid_paranthesis(self, s: str) -> int:
    """
    Returns the length of the longest valid paranthesis
     >>> longest_valid_paranthesis('(()')
     2
     >>> longest_valid_paranthesis(')()())')
     4
     >>> longest_valid_paranthesis('')
     0
     >>> longest_valid_paranthesis(''(())))((()(()()()())
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
