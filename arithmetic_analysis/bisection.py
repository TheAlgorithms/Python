from typing import Callable, Optional


def bisection(
    function: Callable[[float], float], a: float, b: float
) -> Optional[float]:
    """
    finds where function becomes 0 in [a,b] using bolzano
    >>> bisection(lambda x: x ** 3 - 1, -5, 5)
    1.0000000149011612
    >>> bisection(lambda x: x ** 3 - 1, 2, 1000)
    couldn't find root in [ 2 , 1000 ]
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 0, 2)
    1.0
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 2, 4)
    3.0
    >>> bisection(lambda x: x ** 2 - 4 * x + 3, 4, 1000)
    couldn't find root in [ 4 , 1000 ]
    """
    start: float = a
    end: float = b
    if function(a) == 0:  # one of the a or b is a root for the function
        return a
    elif function(b) == 0:
        return b
    elif (
        function(a) * function(b) > 0
    ):  # if none of these are root and they are both positive or negative,
        # then this algorithm can't find the root
        print("couldn't find root in [", a, ",", b, "]")
        return None
    else:
        mid: float = start + (end - start) / 2.0
        while abs(start - mid) > 10 ** -7:  # until precisely equals to 10^-7
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
