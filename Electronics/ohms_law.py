# Importing doctest for testing our function
from doctest import testmod

# Defining function


def ohms_law(v: float = 0, i: float = 0, r: float = 0) -> float:

    """
    This function calculates the any one
    of the three fundemental value, of
    electronics.
    >>> ohms_law(v=10, r=5)
    2.0
    >>> ohms_law(i=1, r=10)
    10.0
    """
    if v == 0:
        result = float(i * r)
        return result
    elif i == 0:
        result = v / r
        return result
    elif r == 0:
        result = v / i
        return result
    else:
        return 0


if __name__ == "__main__":
    testmod(name="ohms_law", verbose=True)
