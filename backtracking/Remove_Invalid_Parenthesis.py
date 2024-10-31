def isParenthesis(c):
    return (c == "(") or (c == ")")


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


# method to remove invalid parenthesis
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
        q.pop(0)
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


expression = "()())()"
removeInvalidParenthesis(expression)
expression = "()v)"
removeInvalidParenthesis(expression)
