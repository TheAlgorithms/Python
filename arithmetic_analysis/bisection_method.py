from sympy import diff
from sympy.abc import x


def bisection_method(function: str, first: float, last: float) -> float:
    """
    finds the root of a function in [a,b] using Bolzano Theorem
    >>> bisection_method("x ** 2 + 2*x + 1",-2,2)
    ['-1.00000', 20]
    >>> bisection_method("x ** 2 - 4 * x + 3", 0, 2)
    ['1.00000', 19]
    >>> bisection_method("x ** 2 - 4 * x + 3", 2, 4)
    ['3.00000', 19]
    >>> bisection_method("x ** 2", -2, 2)
    ['0.00000', 2]
    >>> bisection_method("x ** 2 - 4 * x + 3", 4, 1000)
    Traceback (most recent call last):
        ...
    ValueError: could not find root in given interval.
    """
    rep = 0
    fault = 1
    end: float = first
    start: float = last
    # convert string f,which is our function, to algebraic expression
    f = eval(function)
    # convert string df,which is the derivative of f function, to algebraic expression
    df = diff(function, x)
    med = (end + start) * 0.5
    while fault > 5 * pow(10, -6):
        rep += 1
        if rep > 1:
            pr = med
            med = (end + start) * 0.5
            fault = abs(pr - med)
        # count the value of f for the variables start,end and med
        fstart = f.evalf(subs={x: start})
        fend = f.evalf(subs={x: end})
        fmed = f.evalf(subs={x: med})
        # count the value of df for the variables start,end and med
        dfstart = df.evalf(subs={x: start})
        dfend = df.evalf(subs={x: end})
        dfmed = df.evalf(subs={x: med})
        # if the root is between the start and the med
        if fmed * fend < 0:
            start = med
            continue
        # if the root is between the end and the med
        elif fmed * fstart < 0:
            end = med
            continue
        # if the multipications are positive , we will look for global minimum of function
        elif dfmed * dfend < 0:
            start = med
        elif dfmed * dfstart < 0:
            end = med
    # if the result is not close to 0, the root is not in given internal
    if f.evalf(subs={x: med}) > 5 * pow(10, -6):
        result = ["Could not find root in given interval", 0]
        raise ValueError("could not find root in given interval.")
        return result
    # the function return the root and the repetitions
    result = [f"{med:.5f}", rep]
    return result


if __name__ == "__main__":
    result = bisection_method("x ** 2 + 2*x + 1", -2, 2)
    print(
        "function: x ** 2 + 2*x + 1 ,root : ", result[0], " ,repetitions :", result[1]
    )

    result = bisection_method("x ** 2 - 4 * x + 3", 0, 2)
    print(
        "function: x ** 2 - 4 * x + 3 ,root : ", result[0], " ,repetitions :", result[1]
    )

    result = bisection_method("x ** 2 - 4 * x + 3", 2, 4)
    print(
        "function: x ** 2 - 4 * x + 3 ,root : ", result[0], " ,repetitions :", result[1]
    )

    result = bisection_method("x ** 2", -2, 2)
    print("function: x ** 2 ,root : ", result[0], " ,repetitions :", result[1])

    import doctest

    doctest.testmod()
