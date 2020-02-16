"""
Created on Sat Feb  8 19:25:41 2020

@author: MatteoRaso
"""


def false_position(f, lower_bound: float, upper_bound: float, error: float):
    """An implementation of the false position method used for root-finding.
    The algorithm is extremely similar to the secant method in that it uses
    the x-intercept of the line connecting f(lower_bound) and f(upper_bound) 
    in order to approximate the root of the function. The primary difference is that
    the false position method has a defined interval that the root is bounded
    by. This makes this method slightly slower but guarantees convergence.
    
    INPUTS:
    f: The function which who's root we want to find.
    lower_bound: A value at which f(lower_bound) < 0
    upper_bound: A value at which f(upper_bound) > 0
    error: The maximum tolerated error
    
    OUTPUT:
    The approximated root bounded by lower_bound and upper_bound
    """
    if f(lower_bound) > 0:
        print("f(lower_bound) must be less than zero")

    elif f(upper_bound) < 0:
        print("f(upper_bound) must be greater than zero")

    else:
        # It is unlikely that our initial value will actually be a root, but
        # if it is, we must choose a value that we know is in the interval
        # so we don't end up with the wrong root.
        root = (lower_bound + upper_bound) / 2
        while abs(f(root)) >= error:

            root = (
                -f(upper_bound)
                * (upper_bound - lower_bound)
                / (f(upper_bound) - f(lower_bound))
                + upper_bound
            )
            # Narrowing the interval.
            if f(root) > 0:
                upper_bound = root

            else:
                lower_bound = root

        return root


if __name__ == "__main__":
    import doctest

    doctest.testmod()
