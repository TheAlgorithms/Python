def prefix_infix(prefix):
    stack = []

    i = len(prefix) - 1
    while i >= 0:
        if not is_perator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1

    return stack.pop()


def is_operator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False


if __name__ == "__main__":
    str = "*-A/BC-/ADE"
    print(prefix_infix(str))
