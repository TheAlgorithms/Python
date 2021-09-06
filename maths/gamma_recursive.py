"""
Gamma function is a very useful tool in physics.
It helps calculating complex integral in a convenient way.
for more info: https://en.wikipedia.org/wiki/Gamma_function
"""

# Importing packages
from math import sqrt, pi
from re import match
from typing import Union


def gamma(num : Union[int, float]) -> Union[int, float]:
    """
    Calculates the value of Gamma function of num
    where num is either an integer (1,2,3..) or a half-integer (0.5,1.5,2.5...).
    Implemented using recursion
    Examples:
    >>> gamma(0.5)
    1.7724538509055159
    >>> gamma(2)
    1
    >>> gamma(3.5)
    3.3233509704478426
    >>> gamma(-4)
    -2
    >>> gamma(-1)
    -2
    """
    if num == 1:
        return 1
    elif num == 0.5:
        return sqrt(pi)
    elif num > 1:
        return (num - 1) * gamma(num - 1)
    # Error
    return -2


def test_gamma() -> None:
    """
    >>> test_gamma()
    """
    assert sqrt(pi) == gamma(0.5)
    assert 1 == gamma(1)
    assert 1 == gamma(2)


if __name__ == "__main__":
    is_number = True
    input_ = input("Gamma of: ")
    # Ensure valid input
    try:
        # Ensure input matches half-integer (float) pattern
        if match(r"^[0-9]*\.5$", input_):
            # Convert string to float
            num = float(input_)
        # Ensure input matches an integer pattern
        elif match(r"^[1-9][0-9]*$", input_):
            # Convert string to int
            num = int(input_)
        # Input is not a valid number
        else:
            # raise an error
            raise ValueError
    # Ensure print an error message
    except ValueError:
        print("Error: Input must be an integer or an half-integer!")
        is_number = False
    finally:
        # Ensure input is a valid number
        if is_number:
            print(f"\u0393({num}) = ", end="")
            # Ensure input is an integer
            if isinstance(gamma(num), int):
                # Print result
                print(gamma(num))
            # Otherwise print results with √π (gamma of 0.5 is √π)
            # Therefore all results will be a number times √π
            else:
                results = f"{gamma(num) / sqrt(pi):.4f}"
                results = results.rstrip("0").rstrip(".")
                if results == "1":
                    results = ""
                print(results + "\u221A\u03c0")

