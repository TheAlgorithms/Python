"""
    In this problem, an expression is specified that can
    contain opening and closing parentheses and optionally
    some characters. There are no other operators for strings.
    A minimum number of parentheses must be removed to make the
    input string valid. If multiple valid outputs are possible,
    remove the same number of brackets to print all of them.

    GeeksforGeeks: https://www.geeksforgeeks.org/remove-invalid-parentheses/

    Below is the Python3 implementation of the above problem.
"""

"""
    'isParenthesis' Method checks if character is parenthesis(open or closed)
"""


def isParenthesis(c):
    return (c == "(") or (c == ")")


"""
    'isValidString' method returns true if contains valid parenthesis
"""


def isValidString(str):
    cnt = 0
    for i in range(len(str)):
        if str[i] == "(":
            cnt += 1
        elif str[i] == ")":
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


"""
    'removeInvalidParenthesis method to remove invalid parenthesis
"""


def removeInvalidParenthesis(str):
    if len(str) == 0:
        return

    # visit set to ignore already visited
    visit = set()

    # queue to maintain BFS
    q = []
    temp = 0
    level = 0

    # pushing given as starting node into queue
    q.append(str)
    visit.add(str)
    while len(q):
        str = q[0]
        q.pop()
        if isValidString(str):
            print(str)
            """
                If answer is found, make level true
                so that valid of only that level
                are processed.
            """
            level = True
        if level:
            continue
        for i in range(len(str)):
            if not isParenthesis(str[i]):
                continue

            """
                Removing parenthesis from str and
                pushing into queue,if not visited already
            """
            temp = str[0:i] + str[i + 1 :]
            if temp not in visit:
                q.append(temp)
                visit.add(temp)


# Driver Code
statement = "((()()prathamwanmode(()()))"
removeInvalidParenthesis(statement)
statement = "(hacktober()((()(()(fest)))"
removeInvalidParenthesis(statement)
