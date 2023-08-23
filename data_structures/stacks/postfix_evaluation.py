"""
The Reverse Polish Nation also known as Polish postfix notation
or simply postfix notation.
https://en.wikipedia.org/wiki/Reverse_Polish_notation
Classic examples of simple stack implementations
Valid operators are +, -, *, /.
Each operand may be an integer or another expression.

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

# Defining valid unary operator symbols
UNARY_OP_SYMBOLS = ("-", "+")

# Defining valid binary operator symbols
BINARY_OP_SYMBOLS = ("-", "+", "*", "^", "/")


def parse_token(token: str | float) -> float | str:
    """
    Converts the given data to appropriate number if it is indeed a number, else returns
    the data as it is with a False flag. This function also serves as a check of whether
    the input is a number or not.

    Parameters
    ----------
    token : str or float
        The data which needs to be converted to the appropriate number

    Returns
    -------
    float or str
        Returns a float if `token` is a number and returns `token` if it's an operator
    """
    if is_operator(token):
        return token
    try:
        return float(token)
    except ValueError:
        msg = f"{token} is neither a number nor a valid operator"
        raise ValueError(msg)


def is_operator(token: str | float) -> bool:
    """
    Checks whether a given input is one of the valid operators or not.
    Valid operators being '-', '+', '*', '^' and '/'.

    Parameters
    ----------
    token : str
        The value that needs to be checked for operator

    Returns
    -------
    bool
        True if data is an operator else False.
    """
    return token in BINARY_OP_SYMBOLS


def evaluate(post_fix: list[str], verbose: bool = False) -> float:
    """
    Function that evaluates postfix expression using a stack.
    >>> evaluate(["2", "1", "+", "3", "*"])
    9.0
    >>> evaluate(["4", "13", "5", "/", "+"])
    6.6
    >>> evaluate(["2", "-", "3", "+"])
    1.0
    >>> evaluate(["-4", "5", "*", "6", "-"])
    -26.0
    >>> evaluate([])
    0
    >>> evaluate(["4", "-", "6", "7", "/", "9", "8"])
    Traceback (most recent call last):
    ...
    ArithmeticError: Input is not a valid postfix expression

    Parameters
    ----------
    post_fix : list
        The postfix expression tokenized into operators and operands and stored as a
        python list

    verbose : bool
        Display stack contents while evaluating the expression if verbose is True

    Returns
    -------
    float
        The evaluated value
    """
    stack = []
    valid_expression = []
    opr = {
        "^": lambda p, q: p**q,
        "*": lambda p, q: p * q,
        "/": lambda p, q: p / q,
        "+": lambda p, q: p + q,
        "-": lambda p, q: p - q,
    }  # operators & their respective operation
    if len(post_fix) == 0:
        return 0
    # Checking the list to find out whether the postfix expression is valid
    valid_expression = [parse_token(token) for token in post_fix]
    if verbose:
        # print table header
        print("Symbol".center(8), "Action".center(12), "Stack", sep=" | ")
        print("-" * (30 + len(post_fix)))
    for x in valid_expression:
        if not is_operator(x):
            stack.append(x)  # append x to stack
            if verbose:
                # output in tabular format
                print(
                    str(x).rjust(8),
                    ("push(" + str(x) + ")").ljust(12),
                    stack,
                    sep=" | ",
                )
            continue
        # If x is operator
        # If only 1 value is inside stack and + or - is encountered
        # then this is unary + or - case
        if x in UNARY_OP_SYMBOLS and len(stack) < 2:
            b = stack.pop()  # pop stack
            if x == "-":
                b *= -1  # negate b
            stack.append(b)
            if verbose:
                # output in tabular format
                print(
                    "".rjust(8),
                    ("pop(" + str(b) + ")").ljust(12),
                    stack,
                    sep=" | ",
                )
                print(
                    str(x).rjust(8),
                    ("push(" + str(x) + str(b) + ")").ljust(12),
                    stack,
                    sep=" | ",
                )
            continue
        b = stack.pop()  # pop stack
        if verbose:
            # output in tabular format
            print(
                "".rjust(8),
                ("pop(" + str(b) + ")").ljust(12),
                stack,
                sep=" | ",
            )

        a = stack.pop()  # pop stack
        if verbose:
            # output in tabular format
            print(
                "".rjust(8),
                ("pop(" + str(a) + ")").ljust(12),
                stack,
                sep=" | ",
            )
        # evaluate the 2 values popped from stack & push result to stack
        stack.append(opr[str(x)](a, b))
        if verbose:
            # output in tabular format
            print(
                str(x).rjust(8),
                ("push(" + str(a) + str(x) + str(b) + ")").ljust(12),
                stack,
                sep=" | ",
            )
    # If everything executed correctly, the stack will contain
    # only one element which is the result
    if len(stack) != 1:
        raise ArithmeticError("Input is not a valid postfix expression")
    return float(stack[0])


def is_yes(val: str) -> bool:
    """
    Function that checks whether a user has entered any representation of a Yes (y, Y).
    Any other input is considered as a No.

    Parameters
    -----------
    val : str
        The value entered by user

    Returns
    -------
    bool
        True if Yes, otherwise False
    """
    return val in ("Y", "y")


if __name__ == "__main__":
    loop = True
    # Creating a loop so that user can evaluate postfix expression multiple times
    while True:
        expression = input("Enter a Postfix Expression (space separated): ").split(" ")
        choice = input(
            "Do you want to see stack contents while evaluating? [y/N]: "
        ).strip()
        display = is_yes(choice)
        output = evaluate(expression, display)
        print("Result = ", output)
        choice = input("Do you want to enter another expression? [y/N]: ")
        if not is_yes(choice):
            break
