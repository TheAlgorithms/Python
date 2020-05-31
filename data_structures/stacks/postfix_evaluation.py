"""
Output:

Enter a Postfix Equation (space separated) = 5 6 9 * +
 Symbol  |    Action    | Stack
-----------------------------------
       5 | push(5)      | 5
       6 | push(6)      | 5,6
       9 | push(9)      | 5,6,9
         | pop(9)       | 5,6
         | pop(6)       | 5
       * | push(6*9)    | 5,54
         | pop(54)      | 5
         | pop(5)       |
       + | push(5+54)   | 59

        Result =  59
"""

import operator as op


def Solve(Postfix):
    Stack = []
    Div = lambda x, y: int(x / y)  # noqa: E731 integer division operation
    Opr = {
        "^": op.pow,
        "*": op.mul,
        "/": Div,
        "+": op.add,
        "-": op.sub,
    }  # operators & their respective operation

    # print table header
    print("Symbol".center(8), "Action".center(12), "Stack", sep=" | ")
    print("-" * (30 + len(Postfix)))

    for x in Postfix:
        if x.isdigit():  # if x in digit
            Stack.append(x)  # append x to stack
            # output in tabular format
            print(x.rjust(8), ("push(" + x + ")").ljust(12), ",".join(Stack), sep=" | ")
        else:
            B = Stack.pop()  # pop stack
            # output in tabular format
            print("".rjust(8), ("pop(" + B + ")").ljust(12), ",".join(Stack), sep=" | ")

            A = Stack.pop()  # pop stack
            # output in tabular format
            print("".rjust(8), ("pop(" + A + ")").ljust(12), ",".join(Stack), sep=" | ")

            Stack.append(
                str(Opr[x](int(A), int(B)))
            )  # evaluate the 2 values popped from stack & push result to stack
            # output in tabular format
            print(
                x.rjust(8),
                ("push(" + A + x + B + ")").ljust(12),
                ",".join(Stack),
                sep=" | ",
            )

    return int(Stack[0])


if __name__ == "__main__":
    Postfix = input("\n\nEnter a Postfix Equation (space separated) = ").split(" ")
    print("\n\tResult = ", Solve(Postfix))
