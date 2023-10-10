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


def infix_2_postfix(infix):
    """
    >>> infix_2_postfix("a+b^c")  # doctest: +NORMALIZE_WHITESPACE
     Symbol  |  Stack  | Postfix
    ----------------------------
       a     |         | a
       +     | +       | a
       b     | +       | ab
       ^     | +^      | ab
       c     | +^      | abc
             | +       | abc^
             |         | abc^+
    'abc^+'
    >>> infix_2_postfix("1*((-a)*2+b)")
    Traceback (most recent call last):
        ...
    KeyError: '('
    >>> infix_2_postfix("")
     Symbol  |  Stack  | Postfix
    ----------------------------
    ''
    >>> infix_2_postfix("(()")  # doctest: +NORMALIZE_WHITESPACE
     Symbol  |  Stack  | Postfix
    ----------------------------
       (     | (       |
       (     | ((      |
       )     | (       |
             |         | (
    '('
    >>> infix_2_postfix("())")
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
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
            post_fix.append(x)  # if x is Alphabet / Digit, add it to Postfix
        elif x == "(":
            stack.append(x)  # if x is "(" push to Stack
        elif x == ")":  # if x is ")" pop stack until "(" is encountered
            while stack[-1] != "(":
                post_fix.append(stack.pop())  # Pop stack & add the content to Postfix
            stack.pop()
        else:
            if len(stack) == 0:
                stack.append(x)  # If stack is empty, push x to stack
            else:  # while priority of x is not > priority of element in the stack
                while len(stack) > 0 and priority[x] <= priority[stack[-1]]:
                    post_fix.append(stack.pop())  # pop stack & add to Postfix
                stack.append(x)  # push x to stack

        print(
            x.center(8),
            ("".join(stack)).ljust(print_width),
            ("".join(post_fix)).ljust(print_width),
            sep=" | ",
        )  # Output in tabular format

    while len(stack) > 0:  # while stack is not empty
        post_fix.append(stack.pop())  # pop stack & add to Postfix
        print(
            " ".center(8),
            ("".join(stack)).ljust(print_width),
            ("".join(post_fix)).ljust(print_width),
            sep=" | ",
        )  # Output in tabular format

    return "".join(post_fix)  # return Postfix as str


def infix_2_prefix(infix):
    """
    >>> infix_2_prefix("a+b^c")  # doctest: +NORMALIZE_WHITESPACE
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
    Traceback (most recent call last):
        ...
    KeyError: '('

    >>> infix_2_prefix('')
     Symbol  |  Stack  | Postfix
    ----------------------------
    ''

    >>> infix_2_prefix('(()')
    Traceback (most recent call last):
        ...
    IndexError: list index out of range

    >>> infix_2_prefix('())')  # doctest: +NORMALIZE_WHITESPACE
     Symbol  |  Stack  | Postfix
    ----------------------------
       (     | (       |
       (     | ((      |
       )     | (       |
             |         | (
    '('
    """
    infix = list(infix[::-1])  # reverse the infix equation

    for i in range(len(infix)):
        if infix[i] == "(":
            infix[i] = ")"  # change "(" to ")"
        elif infix[i] == ")":
            infix[i] = "("  # change ")" to "("

    return (infix_2_postfix("".join(infix)))[
        ::-1
    ]  # call infix_2_postfix on Infix, return reverse of Postfix


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    Infix = input("\nEnter an Infix Equation = ")  # Input an Infix equation
    Infix = "".join(Infix.split())  # Remove spaces from the input
    print("\n\t", Infix, "(Infix) -> ", infix_2_prefix(Infix), "(Prefix)")
