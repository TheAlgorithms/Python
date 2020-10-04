"""
Author : Syed Faizan ( 3rd Year IIIT Pune )
Github : faizan2700

Purpose : You have one function f(x) which takes float integer and returns
float you have to integrate the function in limits a to b.
The approximation proposed by Thomas Simpsons in 1743 is one way to calculate
integration.

( read article : https://cp-algorithms.com/num_methods/simpson-integration.html )

simpson_integration() takes function,lower_limit=a,upper_limit=b,precision and
returns the integration of function in given limit.
"""

# constants
# the more the number of steps the more accurate
N_STEPS = 1000


def f(x: float) -> float:
    return x * x


"""
Summary of Simpson Approximation :

By simpsons integration :
1. integration of fxdx with limit a to b is =
    f(x0) + 4 * f(x1) + 2 * f(x2) + 4 * f(x3) + 2 * f(x4)..... + f(xn)
where x0 = a
xi = a + i * h
xn = b
"""


def simpson_integration(function, a: float, b: float, precision: int = 4) -> float:

    """
    Args:
        function : the function which's integration is desired
        a : the lower limit of integration
        b : upper limit of integraion
        precision : precision of the result,error required default is 4

    Returns:
        result : the value of the approximated integration of function in range a to b

    Raises:
        AssertionError: function is not callable
        AssertionError: a is not float or integer
        AssertionError: function should return float or integer
        AssertionError: b is not float or integer
        AssertionError: precision is not positive integer

    >>> simpson_integration(lambda x : x*x,1,2,3)
    2.333

    >>> simpson_integration(lambda x : x*x,'wrong_input',2,3)
    Traceback (most recent call last):
        ...
    AssertionError: a should be float or integer your input : wrong_input

    >>> simpson_integration(lambda x : x*x,1,'wrong_input',3)
    Traceback (most recent call last):
        ...
    AssertionError: b should be float or integer your input : wrong_input

    >>> simpson_integration(lambda x : x*x,1,2,'wrong_input')
    Traceback (most recent call last):
        ...
    AssertionError: precision should be positive integer your input : wrong_input
    >>> simpson_integration('wrong_input',2,3,4)
    Traceback (most recent call last):
        ...
    AssertionError: the function(object) passed should be callable your input : ...

    >>> simpson_integration(lambda x : x*x,3.45,3.2,1)
    -2.8

    >>> simpson_integration(lambda x : x*x,3.45,3.2,0)
    Traceback (most recent call last):
        ...
    AssertionError: precision should be positive integer your input : 0

    >>> simpson_integration(lambda x : x*x,3.45,3.2,-1)
    Traceback (most recent call last):
        ...
    AssertionError: precision should be positive integer your input : -1

    """
    assert callable(
        function
    ), f"the function(object) passed should be callable your input : {function}"
    assert isinstance(a, float) or isinstance(
        a, int
    ), f"a should be float or integer your input : {a}"
    assert isinstance(function(a), float) or isinstance(function(a), int), (
        "the function should return integer or float return type of your function, "
        f"{type(a)}"
    )
    assert isinstance(b, float) or isinstance(
        b, int
    ), f"b should be float or integer your input : {b}"
    assert (
        isinstance(precision, int) and precision > 0
    ), f"precision should be positive integer your input : {precision}"

    # just applying the formula of simpson for approximate integraion written in
    # mentioned article in first comment of this file and above this function

    h = (b - a) / N_STEPS
    result = function(a) + function(b)

    for i in range(1, N_STEPS):
        a1 = a + h * i
        result += function(a1) * (4 if i % 2 else 2)

    result *= h / 3
    return round(result, precision)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
