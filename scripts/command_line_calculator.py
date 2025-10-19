"""
Expression Evaluator
--------------------
A Python module that evaluates arithmetic and bitwise expressions.

Supports:
    +  -  *  /  **  <<  >>  &  |  ^  ( )



Usage:
    >>> from evaluator import evaluate
    >>> evaluate("2 + 3 * 4")
    14
    >>> evaluate("(2 + 3) * 4")
    20
    >>> evaluate("2 ** 8")
    256
    >>> evaluate("10 | 6")
    14
    >>> evaluate("10 & 6")
    2
    >>> evaluate("(10 | 6) ^ 5")
    9
    >>> evaluate("10 / 4")
    2.5
"""

import re

def evaluate(expr: str):
    """
    Evaluate an arithmetic/bitwise expression string and return result.

    Args:
        expr (str): Expression to evaluate

    Returns:
        int | float: The computed result, automatically casted.

    Examples:
        >>> evaluate("2 + 3 * 4")
        14
        >>> evaluate("2 ** 10")
        1024
        >>> evaluate("10 / 4")
        2.5
        >>> evaluate("(10 | 6) ^ 5")
        9
    """

    # --- Tokenization ---
    tokens = re.findall(r'\d+\.\d+|\d+|\*\*|<<|>>|[&|^+\-*/()]', expr.replace(" ", ""))

    # --- Handle unary minus (e.g., -5 + 3) and minus in starting ---
    if tokens and tokens[0] == "-":
        tokens.insert(0, "0")

    def clean(lst):
        return [x for x in lst if x is not None]

    def solve_power(z):
        while "**" in z:
            i = z.index("**")
            z[i - 1] = float(z[i - 1]) ** float(z[i + 1])
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_div(z):
        while "/" in z:
            i = z.index("/")
            z[i - 1] = float(z[i - 1]) / float(z[i + 1])
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_mul(z):
        while "*" in z:
            i = z.index("*")
            z[i - 1] = float(z[i - 1]) * float(z[i + 1])
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_minus(z):
        while "-" in z:
            i = z.index("-")
            z[i] = "+"
            z[i + 1] = -1 * float(z[i + 1])
        return z

    def solve_add(z):
        while "+" in z:
            i = z.index("+")
            z[i - 1] = float(z[i - 1]) + float(z[i + 1])
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_lshift(z):
        while "<<" in z:
            i = z.index("<<")
            z[i - 1] = int(float(z[i - 1])) << int(float(z[i + 1]))
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_rshift(z):
        while ">>" in z:
            i = z.index(">>")
            z[i - 1] = int(float(z[i - 1])) >> int(float(z[i + 1]))
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_and(z):
        while "&" in z:
            i = z.index("&")
            z[i - 1] = int(float(z[i - 1])) & int(float(z[i + 1]))
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_xor(z):
        while "^" in z:
            i = z.index("^")
            z[i - 1] = int(float(z[i - 1])) ^ int(float(z[i + 1]))
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_or(z):
        while "|" in z:
            i = z.index("|")
            z[i - 1] = int(float(z[i - 1])) | int(float(z[i + 1]))
            z[i:i + 2] = [None, None]
            z = clean(z)
        return z

    def solve_parentheses(z):
        while "(" in z:
            close = z.index(")")
            open_ = max(i for i, v in enumerate(z[:close]) if v == "(")
            inner = z[open_ + 1:close]
            result = evaluate(" ".join(map(str, inner)))
            z = z[:open_] + [str(result)] + z[close + 1:]
        return z

    tokens = solve_parentheses(tokens)

    # Precedence order
    for func in [solve_power, solve_div, solve_mul, solve_minus, solve_add,
                 solve_lshift, solve_rshift, solve_and, solve_xor, solve_or]:
        tokens = func(tokens)

    result = tokens[0]

    # Return as int if it’s cleanly integer-valued
    if isinstance(result, (int, float)):
        if abs(result - int(result)) < 1e-9:
            return int(result)
        return float(result)

    # If it's a string (edge-case), convert safely
    try:
        f = float(result)
        return int(f) if f.is_integer() else f
    except ValueError:
        raise ValueError("Invalid expression or unsupported syntax.")
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
