def __isNum(input):
    try:
        float(input)
    except ValueError:
        return False
    return True


def __getPrio(char):
    priority = {
        "p0": "(",
        "p1": "+-)",
        "p2": "*/%",
        "p3": "^"
    }
    if char in priority['p0']:
        return 0
    elif char in priority['p1']:
        return 1
    elif char in priority['p2']:
        return 2
    else:
        return 3


def __compPrio(new, old):
    """returns true if priority of new is bigger than priority of the old"""
    return __getPrio(new) > __getPrio(old)


def convertToRPN(inStr: str) -> str:
    """convert string to rpn stack.
    Elements should be separated by spaces.
    Raising to a power should be done using ^, not **.
    """
    sequence = inStr.strip().split(" ")
    auxStack = []
    rpnStack = []
    for elem in sequence:
        if elem.isdigit():
            rpnStack.append(elem)
        elif elem == '(':
            auxStack.append(elem)
        elif elem == ')':
            elem = auxStack.pop()
            while len(auxStack) != 0 and elem != '(':
                rpnStack.append(elem)
                elem = auxStack.pop()
        else:
            if len(auxStack) == 0 or __compPrio(elem, auxStack[len(auxStack) - 1]):
                auxStack.append(elem)
            else:
                while len(auxStack) != 0 and not __compPrio(elem, auxStack[len(auxStack) - 1]):
                    rpnStack.append(auxStack.pop())
                auxStack.append(elem)
    while len(auxStack) != 0:
        rpnStack.append(auxStack.pop())
    return ' '.join(rpnStack)


def evaluateRPN(sequence: str) -> str:
    """gets string in rpn and calculates result, then returns it.
    Elements should be separated by spaces.
    Raising to a power should be done using ^, not **."""
    sequence = sequence.strip().split(" ")
    auxStack = []
    for elem in sequence:
        if __isNum(elem):
            auxStack.append(elem)
        else:
            a = auxStack.pop()
            b = auxStack.pop()
            elem = elem if elem != '^' else '**'
            equation = str(b) + elem + str(a)
            equation = eval(equation)
            auxStack.append(equation)
    return auxStack[0]


if __name__ == '__main__':
    # example
    s = " 2 + 2 * 2 ^ 2 - 2 "
    rpn = convertToRPN(s)
    print(evaluateRPN(rpn))
