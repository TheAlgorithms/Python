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


def get_number(data: str) -> tuple[bool, int] | tuple[bool, float] | tuple[bool, str]:
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
    int_val = 0
    float_val = 0.0
    try:
        int_val = int(data)
        return True, int_val
    except ValueError:
        try:
            float_val = float(data)
            return True, float_val
        except ValueError:
            return False, data


def is_operator(data: str) -> bool:
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
    return data in ["-", "+", "*", "^", "/"]


def evaluate(post_fix: list, verbose: bool = False) -> int:
    """
    Function that evaluates postfix expression using a stack.
    >>> evaluate(["2", "1", "+", "3", "*"])
    9
    >>> evaluate(["4", "13", "5", "/", "+"])
    6
    >>> evaluate(["2", "-", "3", "+"])
    1
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
    stack = []
    opr = {
        "^": lambda p, q: p**q,
        "*": lambda p, q: p * q,
        "/": lambda p, q: p / q,
        "+": lambda p, q: p + q,
        "-": lambda p, q: p - q,
    }  # operators & their respective operation
    if len(post_fix) > 0:
        if verbose:
            # print table header
            print("Symbol".center(8), "Action".center(12), "Stack", sep=" | ")
            print("-" * (30 + len(post_fix)))
        for x in post_fix:
            is_number, x = get_number(x)
            if is_number:  # if x is a number (integer, float)
                stack.append(x)  # append x to stack
                if verbose:
                    # output in tabular format
                    print(
                        str(x).rjust(8),
                        ("push(" + str(x) + ")").ljust(12),
                        stack,
                        sep=" | ",
                    )
            elif is_operator(x):
                # If only 1 value is inside stack and + or - is encountered
                # then this is unary + or - case
                if x in ["-", "+"] and len(stack) < 2:
                    b = stack.pop()  # pop stack
                    if x == "-":
                        stack.append(-b)  # negate b and push again into stack
                    else:  # when x is unary +
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
                else:
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
                    stack.append(opr[x](a, b))
                    if verbose:
                        # output in tabular format
                        print(
                            str(x).rjust(8),
                            ("push(" + str(a) + str(x) + str(b) + ")").ljust(12),
                            stack,
                            sep=" | ",
                        )
            else:
                print(f"{x} is neither a number, nor a valid operator")
                break
        if len(stack) == 1:  # If everything executed correctly,the stack will contain
            # only one element which is the result
            _, result = get_number(stack[0])
        else:
            result = None
        return result
    return 0


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
    return val in ["Y", "y"]


if __name__ == "__main__":
    loop = True
    # Creating a loop so that user can evaluate postfix expression multiple times
    while loop:
        expression = input("Enter a Postfix Expression (space separated): ").split(" ")
        choice = input("Do you want to see stack contents while evaluating? [y/N]: ")
        display = is_yes(choice)
        output = evaluate(expression, display)
        if output is not None:
            print("Result = ", output)
        choice = input("Do you want to enter another expression? [y/N]: ")
        loop = is_yes(choice)
