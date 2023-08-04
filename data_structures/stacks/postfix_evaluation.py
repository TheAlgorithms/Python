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


def get_number(data: str) -> int | float | str:
    """
    Converts the given data to appropriate number if it is indeed a number, else returns
    the data as it is with a False flag. This function also serves as a check of whether
    the input is a number or not.

    Parameters
    ----------
    data : str
        The data which needs to be converted to the appropriate number

    Returns
    -------
    bool,  int or float
        Returns a tuple of (a, b) where 'a' is True if data is indeed a number (integer
        or numeric) and 'b' is either an integer of a floating point number.
        If 'a' is False, then b is 'data'
    """
    try:
        return int(data)
    except ValueError:
        try:
            return float(data)
        except ValueError:
            if is_operator(data):
                return data
            msg = f"{data} is neither a number nor a valid operator"
            raise ValueError(msg)


def is_operator(data: str | int | float) -> bool:
    """
    Checks whether a given input is one of the valid operators or not.
    Valid operators being '-', '+', '*', '^' and '/'.

    Parameters
    ----------
    data : str
        The value that needs to be checked for operator

    Returns
    -------
    bool
        True if data is an operator else False.
    """
    return data in BINARY_OP_SYMBOLS


def evaluate(post_fix: list[str], verbose: bool = False) -> int | float | str | None:
    """
    Function that evaluates postfix expression using a stack.
    >>> evaluate(["2", "1", "+", "3", "*"])
    9
    >>> evaluate(["4", "13", "5", "/", "+"])
    6.6
    >>> evaluate(["2", "-", "3", "+"])
    1
    >>> evaluate(["-4", "5", "*", "6", "-"])
    -26
    >>> evaluate([])
    0

    Parameters
    ----------
    post_fix : list
        The postfix expression tokenized into operators and operands and stored as a
        python list

    verbose : bool
        Display stack contents while evaluating the expression if verbose is True

    Returns
    -------
    int
        The evaluated value
    """
    x: str | int | float
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
    for x in post_fix:
        valid_expression.append(get_number(x))
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
        # else:
        #     msg = f"{x} is neither a number nor a valid operator"
        #     raise ValueError(msg)
    # If everything executed correctly, the stack will contain
    # only one element which is the result
    if len(stack) != 1:
        raise ArithmeticError("Input is not a valid postfix expression")
    return stack[0]


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
