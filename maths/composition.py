"""
Makes function composition possible in a mathematical way.
f( g( x ) ) = (f*g)(x)
f(g) = f*g
https://en.wikipedia.org/wiki/Function_composition
"""


class Compose(object):
    """
    Makes function composable
    >>> @Compose
    ... def f(x):
    ...     return x
    ...
    >>> g = Compose(lambda x: x)
    >>> print((f * g)(2))
    2
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, x):
        return self.func(x)

    def __mul__(self, neighbour):
        return Compose(lambda x: self.func(neighbour.func(x)))


def tests():
    # Syntax 1
    @Compose
    def f(x):
        return x

    # Syntax 2
    g = Compose(lambda x: x)

    print((f * g)(2))

    @Compose
    def log(text):
        return "Log " + text

    @Compose
    def warn(text):
        return " Warn " + text

    print((warn * log)("this"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
