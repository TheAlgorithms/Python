"""
Output:
Enter an infix Equation = a + b ^c
 Symbol  |  Stack  | Postfix
----------------------------
   c     |         | c
   ^     | ^       | c
   b     | ^       | cb
   +     | +       | cb^
   a     | +       | cb^a
         |         | cb^a+
         a+b^c (infix) ->  +a^bc (Prefix)
"""


def infix_2_postfix(infix):
    stack = []
    postfix = []
    priority = {
        "^": 3,
        "*": 2,
        "/": 2,
        "%": 2,
        "+": 1,
        "-": 1,
    }  # Priority of each operator
    print_width = len(infix) if (len(infix) > 7) else 7

    # Print table header for output
    print(
        "Symbol".center(8),
        "Stack".center(print_width),
        "Postfix".center(print_width),
        sep=" | ",
    )
    print("-" * (print_width * 3 + 7))

    for x in infix:
        if x.isalpha() or x.isdigit():
            postfix.append(x)  # if x is Alphabet / Digit, add it to postfix
        elif x == "(":
            stack.append(x)  # if x is "(" push to stack
        elif x == ")":  # if x is ")" pop stack until "(" is encountered
            while stack[-1] != "(":
                postfix.append(stack.pop())  # Pop stack & add the content to postfix
            stack.pop()
        else:
            if len(stack) == 0:
                stack.append(x)  # If stack is empty, push x to stack
            else:  # while priority of x is not > priority of element in the stack
                while (
                    len(stack) > 0
                    and stack[-1] in priority
                    and priority[x] <= priority[stack[-1]]
                ):
                    postfix.append(stack.pop())  # pop stack & add to postfix
                stack.append(x)  # push x to stack

        print(
            x.center(8),
            ("".join(stack)).ljust(print_width),
            ("".join(postfix)).ljust(print_width),
            sep=" | ",
        )  # Output in tabular format

    while len(stack) > 0:  # while stack is not empty
        postfix.append(stack.pop())  # pop stack & add to postfix
        print(
            " ".center(8),
            ("".join(stack)).ljust(print_width),
            ("".join(postfix)).ljust(print_width),
            sep=" | ",
        )  # Output in tabular format

    return "".join(postfix)  # return postfix as str


def infix_2_prefix(infix):
    infix = list(infix[::-1])  # reverse the infix equation

    for i in range(len(infix)):
        if infix[i] == "(":
            infix[i] = ")"  # change "(" to ")"
        elif infix[i] == ")":
            infix[i] = "("  # change ")" to "("

    return (infix_2_postfix("".join(infix)))[
        ::-1
    ]  # call infix_2_postfix on infix, return reverse of postfix


if __name__ == "__main__":
    infix = input("\nEnter an Infix Equation = ")  # Input an infix equation
    infix = "".join(infix.split())  # Remove spaces from the input
    print("\n\t", infix, "(Infix) -> ", infix_2_prefix(infix), "(Prefix)")
