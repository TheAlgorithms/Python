"""
Output:

Enter an Infix Equation = a + b ^c
 Symbol  |  Stack  | Postfix
----------------------------
   c     |         | c
   ^     | ^       | c
   b     | ^       | cb
   +     | +       | cb^
   a     | +       | cb^a
         |         | cb^a+

         a+b^c (Infix) ->  +a^bc (Prefix)
"""


def infix_2_postfix(infix: str) -> str:
    stack = []
    post_fix = []
    priority = {
        "^": 3,
        "*": 2,
        "/": 2,
        "%": 2,
        "+": 1,
        "-": 1,
    }  # Priority of each operator

    print_width = len(infix) if len(infix) > 7 else 7
    # Print table header for output
    print(
        "Symbol".center(8),
        "Stack".center(print_width),
        "Postfix".rjust((print_width - 7) // 2 + 7),
        sep=" | ",
    )
    print("-" * (print_width * 3 + 7))

    for x in infix:
        if x.isalpha() or x.isdigit():
            post_fix.append(x)  # if x is Alphabet / Digit, add it to Postfix
        elif x == "(":
            stack.append(x)  # if x is "(" push to Stack
        elif x == ")":  # if x is ")" pop stack until "(" is encountered
            if len(stack) == 0:  # close bracket without open bracket
                raise ValueError("Invalid bracket position(s)")

            while stack[-1] != "(":
                post_fix.append(stack.pop())  # Pop stack & add the content to Postfix
            stack.pop()
        else:
            if len(stack) == 0:
                stack.append(x)  # If stack is empty, push x to stack
            else:  # while priority of x is not > priority of element in the stack
                while (
                    len(stack) > 0
                    and stack[-1] != "("
                    and priority[x] <= priority[stack[-1]]
                ):
                    post_fix.append(stack.pop())  # pop stack & add to Postfix
                stack.append(x)  # push x to stack

        if post_fix != []:
            print(
                x.center(8),
                ("".join(stack)).ljust(print_width),
                "".join(post_fix),
                sep=" | ",
            )  # Output in tabular format

        else:  # Post_fix is empty -> remove trailing space in table
            print(
                x.center(8) + " | " + ("".join(stack)).ljust(print_width) + " |"
            )  # Output in tabular format

    while len(stack) > 0:  # while stack is not empty
        if stack[-1] == "(":  # open bracket with no close bracket
            raise ValueError("Invalid bracket position(s)")

        post_fix.append(stack.pop())  # pop stack & add to Postfix
        print(
            " ".center(8),
            ("".join(stack)).ljust(print_width),
            "".join(post_fix),
            sep=" | ",
        )  # Output in tabular format

    return "".join(post_fix)  # return Postfix as str


def infix_2_prefix(infix: str) -> str:
    """
    >>> infix_2_prefix("a+b^c")
     Symbol  |  Stack  | Postfix
    ----------------------------
       c     |         | c
       ^     | ^       | c
       b     | ^       | cb
       +     | +       | cb^
       a     | +       | cb^a
             |         | cb^a+
    '+a^bc'

    >>> infix_2_prefix("1*((-a)*2+b)")
     Symbol  |    Stack     |   Postfix
    -------------------------------------------
       (     | (            |
       b     | (            | b
       +     | (+           | b
       2     | (+           | b2
       *     | (+*          | b2
       (     | (+*(         | b2
       a     | (+*(         | b2a
       -     | (+*(-        | b2a
       )     | (+*          | b2a-
       )     |              | b2a-*+
       *     | *            | b2a-*+
       1     | *            | b2a-*+1
             |              | b2a-*+1*
    '*1+*-a2b'

    >>> infix_2_prefix('')
     Symbol  |  Stack  | Postfix
    ----------------------------
    ''

    >>> infix_2_prefix('(()')
    Traceback (most recent call last):
        ...
    ValueError: Invalid bracket position(s)

    >>> infix_2_prefix('())')
    Traceback (most recent call last):
        ...
    ValueError: Invalid bracket position(s)
    """
    new_infix = list(infix[::-1])  # reverse the infix equation

    for i in range(len(new_infix)):
        if new_infix[i] == "(":
            new_infix[i] = ")"  # change "(" to ")"
        elif new_infix[i] == ")":
            new_infix[i] = "("  # change ")" to "("

    return (infix_2_postfix("".join(new_infix)))[
        ::-1
    ]  # call infix_2_postfix on Infix, return reverse of Postfix


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    Infix = input("\nEnter an Infix Equation = ")  # Input an Infix equation
    Infix = "".join(Infix.split())  # Remove spaces from the input
    print("\n\t", Infix, "(Infix) -> ", infix_2_prefix(Infix), "(Prefix)")
