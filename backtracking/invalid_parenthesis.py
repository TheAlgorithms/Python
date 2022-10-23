# Remove Invalid Parenthese
# An expression will be given which can contain open and close parentheses and optionally some characters, No other operator will be there in string. We need to remove minimum number of parentheses to make the input string valid. If more than one valid output are possible removing same number of parentheses then print all such output.


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


def isParenthesis(c):
    return (c == "(") or (c == ")")


def removeInvalidParenthesis(str):
    if len(str) == 0:
        return

    visit = set()

    q = []
    temp = 0
    level = 0

    q.append(str)
    visit.add(str)
    while len(q):
        str = q[0]
        q.pop()
        if isValidString(str):
            print(str)

            level = True
        if level:
            continue
        for i in range(len(str)):
            if not isParenthesis(str[i]):
                continue

            temp = str[0:i] + str[i + 1 :]
            if temp not in visit:
                q.append(temp)
                visit.add(temp)


# main
expression = "()())()(()"
removeInvalidParenthesis(expression)
expression = "()x)())"
removeInvalidParenthesis(expression)
