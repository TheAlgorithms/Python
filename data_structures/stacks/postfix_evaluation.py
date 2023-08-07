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


def solve(post_fix):
    stack = []
    div = lambda x, y: int(x / y)  # noqa: E731 integer division operation
    opr = {
        "^": op.pow,
        "*": op.mul,
        "/": div,
        "+": op.add,
        "-": op.sub,
    }  # operators & their respective operation

    # print table header
    print("Symbol".center(8), "Action".center(12), "Stack", sep=" | ")
    print("-" * (30 + len(post_fix)))

    for x in post_fix:
        if x.isdigit():  # if x in digit
            stack.append(x)  # append x to stack
            # output in tabular format
            print(x.rjust(8), ("push(" + x + ")").ljust(12), ",".join(stack), sep=" | ")
        else:
            b = stack.pop()  # pop stack
            # output in tabular format
            print("".rjust(8), ("pop(" + b + ")").ljust(12), ",".join(stack), sep=" | ")

            a = stack.pop()  # pop stack
            # output in tabular format
            print("".rjust(8), ("pop(" + a + ")").ljust(12), ",".join(stack), sep=" | ")

            stack.append(
                str(opr[x](int(a), int(b)))
            )  # evaluate the 2 values popped from stack & push result to stack
            # output in tabular format
            print(
                x.rjust(8),
                ("push(" + a + x + b + ")").ljust(12),
                ",".join(stack),
                sep=" | ",
            )

    return int(stack[0])


if __name__ == "__main__":
    Postfix = input("\n\nEnter a Postfix Equation (space separated) = ").split(" ")
    print("\n\tResult = ", solve(Postfix))
